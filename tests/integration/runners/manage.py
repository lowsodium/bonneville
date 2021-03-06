'''
Tests for the salt-run command
'''
# Import Salt Testing libs
from salttesting.helpers import ensure_in_syspath
ensure_in_syspath('../../')

# Import bonneville libs
import integration


class ManageTest(integration.ShellCase):
    '''
    Test the manage runner
    '''
    def test_up(self):
        '''
        manage.up
        '''
        ret = self.run_run_plus('manage.up')
        self.assertIn('minion', ret['fun'])
        self.assertIn('sub_minion', ret['fun'])
        self.assertIn('minion', ret['out'])
        self.assertIn('sub_minion', ret['out'])

    def test_down(self):
        '''
        manage.down
        '''
        ret = self.run_run_plus('manage.down')
        self.assertNotIn('minion', ret['fun'])
        self.assertNotIn('sub_minion', ret['fun'])
        self.assertNotIn('minion', ret['out'])
        self.assertNotIn('sub_minion', ret['out'])


if __name__ == '__main__':
    from integration import run_tests
    run_tests(ManageTest)
