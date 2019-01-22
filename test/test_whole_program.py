import os
from unittest import TestCase
from lib import (
    class_loader,
    thread,
    run_time_data
)


class TestAsAWholeProgramm(TestCase):
    def setUp(self):
        class_loader.jrelibpath = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            '..'
        )

    def tearDown(self):
        self.class_struct = None

    def load_main(self, klass_path, klass_name):
        class_loader.classpath = klass_path
        self.class_struct = class_loader.load_class(klass_name)
        self.main_thread = thread.Thread(
            klass_name, 'main', '([Ljava/lang/String;)V', [''])
        run_time_data.thread_pool.append(self.main_thread)

    def test_local_static_func_return_6(self):
        self.load_main(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                'local_static_func'
            ),
            'LocalStaticFunc'
        )

        final_index_1_value = None

        def func(idx, value):
            print(f'ID: {idx}, value: {value}')
            nonlocal final_index_1_value
            if idx == 1:
                final_index_1_value = value
        class_loader.local_variable_callbacks['LocalStaticFunc.main'] = func
        self.main_thread.run()
        self.assertEqual(
            final_index_1_value, 6, 'Local static func return value wrong.')

    def test_simple_loop(self):
        self.load_main(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                'simple_loop'
            ),
            'SimpleLoop'
        )

        final_index_1_value = None

        def func(idx, value):
            print(f'ID: {idx}, value: {value}')
            nonlocal final_index_1_value
            if idx == 1:
                final_index_1_value = value

        class_loader.local_variable_callbacks['SimpleLoop.main'] = func
        self.main_thread.run()
        self.assertEqual(
            final_index_1_value, 30, 'Simple loop calculate get wrong result.')
