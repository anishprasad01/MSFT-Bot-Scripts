import BuildComposer.src.buildcomposer as bc_script
import unittest
import unittest.mock
import io
import os

class Test_TestDirectoryOperations(unittest.TestCase):
    def setUp(self):
        # release, path, wipe, verbose, start
        self.args = bc_script.Arguments("v2.0.0", "C:\ComposerTests", True, False, False)
        self.dir = "Composer %s" % self.args.release
        bc_script.change_dir(self.args)

    def test_mkdir_new(self):
        bc_script.make_composer_dir(self.args)
        self.assertTrue(os.path.isdir(os.path.join(self.args.path, self.dir)))

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_mkdir_prev_exists(self, mock_stdout):
        bc_script.make_composer_dir(self.args)
        expected = "[Composer %s directory already exists. Please specify -w/--wipe to delete and reinstall this release.]\n" % self.args.release
        self.assertEquals(mock_stdout.getvalue(), expected)

    def test_wipe(self):
        bc_script.wipe(self.args)
        self.assertFalse(os.path.isdir(os.path.join(self.args.path, self.dir)))

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_wipe_flag_not_set(self, mock_stdout):
        falseArg = bc_script.Arguments("v2.0.0", "C:\ComposerTests", False, False, False)
        bc_script.wipe(falseArg)
        expected = "\n[Wipe flag not set. Skipping Deletion]\n"
        self.assertEquals(mock_stdout.getvalue(), expected)

