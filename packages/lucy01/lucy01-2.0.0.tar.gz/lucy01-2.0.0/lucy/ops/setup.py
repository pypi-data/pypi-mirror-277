from concurrent import futures
from concurrent.futures import ThreadPoolExecutor
from typing import Generator, Tuple

from selenium.webdriver.common.by import By

from lucy import utils
from lucy.browser import Browser
from lucy.config.config import config, Website
from lucy.types import Contest, Task, Test


class SetupOps:  # pylint: disable=too-few-public-methods

    def __init__(self, n_threads: int = 1, auth: bool = False, force: bool = False):
        self.n_threads = n_threads
        self.auth = auth
        self.force = force

    def parse_tasks(self, contest: Contest) -> list[Task]:
        if contest.site == Website.ATCODER:
            return list(self.__parse_atcoder_tasks(contest))
        raise NotImplementedError()

    def __parse_atcoder_tasks(self, contest: Contest) -> Generator[Task, None, None]:
        browser = Browser()

        tasks_page_url = f'{config.website[contest.site].host}/contests/{contest.contest_id}/tasks'
        browser.driver.get(tasks_page_url)
        tasks_page = browser.get_soup()

        tasks_table = tasks_page.select('table.table tbody tr')
        for row in tasks_table:
            data = row.find_all('td')
            task_id = data[0].text
            task_url = f"{config.website[contest.site].host}{row.find_all('a')[0].get('href')}"
            task = Task(contest.site, contest.contest_id, task_id)
            setattr(task, 'url', task_url)
            yield task

    def parse_samples(self, task: Task) -> Tuple[Task, list[Tuple[str, str]]]:
        browser = Browser(authenticate=task.site if self.auth else None)
        if task.site == Website.ATCODER:
            return task, list(self.__parse_atcoder_samples(task, browser))
        raise NotImplementedError()

    def __parse_atcoder_samples(self, task: Task,
                                browser: Browser) -> Generator[Tuple[str, str], None, None]:
        browser.driver.get(getattr(task, 'url'))
        task_page = browser.get_soup()

        for input_, output in utils.batched(task_page.select('pre[id]'), 2):
            yield input_.text, output.text

    def run(self, target: Contest) -> Generator[Tuple[Task, int], None, None]:
        assert not isinstance(target, Test)
        tasks = self.parse_tasks(target)
        if isinstance(target, Task):
            tasks = [task for task in tasks if task.task_id == target.task_id]
        print(f'Found {len(tasks)} task(s).')
        if not self.force:
            skipped_tasks = [task.task_id for task in tasks if task.exists()]
            if skipped_tasks:
                print(
                    f"Skipping existing task(s) - {', '.join(skipped_tasks)}. Use `-f` to force update."  # pylint: disable=line-too-long
                )
            tasks = [task for task in tasks if not task.exists()]

        with ThreadPoolExecutor(max_workers=self.n_threads) as executor:
            threads = [executor.submit(self.parse_samples, task) for task in tasks]
            for thread in futures.as_completed(threads):
                task, tests = thread.result()
                yield task, len(tests)
                task.delete_tests()
                task.store_tests(tests)

        for task in tasks:
            task.create_impl_file()

    def __get_atcoder_hidden(self, task: Task, test_id: str) -> Generator[str, None, None]:
        config.storage.clear_tmp()
        browser = Browser()
        browser.driver.get(
            'https://www.dropbox.com/sh/nx3tnilzqz7df8a/AAAYlTq2tiEHl5hsESw6-yfLa?dl=0')
        browser.sleep(2)
        contest_link = browser.driver.find_element(
            by=By.CSS_SELECTOR, value=f"a[aria-label='{task.contest_id}' i]").get_attribute('href')
        assert isinstance(contest_link, str)
        yield f'Fetching {task.contest_id} folder ...'
        browser.driver.get(contest_link)
        task_link = browser.driver.find_element(
            by=By.CSS_SELECTOR, value=f"a[aria-label='{task.task_id}' i]").get_attribute('href')
        assert isinstance(task_link, str)
        yield f'Fetching {task.task_id} folder ...'
        browser.driver.get(task_link)
        in_link = browser.driver.find_element(by=By.CSS_SELECTOR,
                                              value="a[aria-label='in' i]").get_attribute('href')
        out_link = browser.driver.find_element(by=By.CSS_SELECTOR,
                                               value="a[aria-label='out' i]").get_attribute('href')
        assert isinstance(in_link, str)
        yield 'Fetching input samples folder ...'
        browser.driver.get(in_link)
        file_link = browser.driver.find_element(
            by=By.CSS_SELECTOR, value=f"a[aria-label='{test_id}']").get_attribute('href')
        assert isinstance(file_link, str)
        yield 'Fetching input file ...'
        browser.driver.get(file_link)
        browser.driver.find_element(by=By.CSS_SELECTOR,
                                    value="button[aria-label='Download']").click()
        browser.sleep(3)
        browser.wait_get(By.CSS_SELECTOR, 'div.dig-Modal-footer>span>button').click()
        yield f'Downloading {test_id} input file ...'
        browser.sleep(5)
        in_txt = browser.read_downloaded(test_id)
        assert isinstance(out_link, str)
        yield 'Fetching output samples folder ...'
        browser.driver.get(out_link)
        file_link = browser.driver.find_element(
            by=By.CSS_SELECTOR, value=f'a[aria-label="{test_id}"]').get_attribute('href')
        assert isinstance(file_link, str)
        yield 'Fetching output file ...'
        browser.driver.get(file_link)
        browser.driver.find_element(by=By.CSS_SELECTOR,
                                    value="button[aria-label='Download']").click()
        browser.sleep(3)
        browser.wait_get(By.CSS_SELECTOR, 'div.dig-Modal-footer>span>button').click()
        yield f'Downloading {test_id} output file ...'
        browser.sleep(5)
        out_txt = browser.read_downloaded(test_id)
        idx = task.store_test((in_txt, out_txt))
        yield ''
        yield f'{test_id} setup as Test#{idx:02d}.'

    def get_hidden(self, task: Task, test_id: str) -> Generator[str, None, None]:
        if task.site == Website.ATCODER:
            return self.__get_atcoder_hidden(task, test_id)
        raise NotImplementedError()
