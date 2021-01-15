# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import moodle_api
import requests

import config

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    moodle_api.URL = config.URL
    moodle_api.KEY = config.KEY

    courseids = [56631]
    for courseid in courseids:
        course = moodle_api.call('core_course_get_contents', courseid=courseid)

        course_general = course[0]
        modules = course_general.get('modules')

        if not modules:
            print('error')

        for module in modules:
            if module.get('name') == 'syllabus':
                try:
                    contents = module.get('contents')[0]
                    filename = contents.get('filename')
                    url = contents.get('fileurl')
                    url = '{}&token={}'.format(url, moodle_api.KEY)

                    response = requests.get(url)

                    with open(config.DOWNLOADPATH.format(filename), 'wb') as f:
                        f.write(response.content)

                    break

                except:
                    print('error')

        x = 1