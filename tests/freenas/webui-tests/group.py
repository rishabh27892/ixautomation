# Author: Rishabh Chauhan
# License: BSD
# Location for tests  of FreeNAS new GUI
#Test case count: 2

from source import *
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


import time
import unittest
import xmlrunner
import random
try:
    import unittest2 as unittest
except ImportError:
    import unittest


xpaths = {
         'newGroupName' : "//*[@id='1']/form-input/div/md-input-container/div/div[1]/div/input",
         'submenuGroup' : "//*[@id='1-0']",
        'deleteConfirm' : "/html/body/div[3]/div[3]/div[2]/md-dialog-container/confirm-dialog/div[1]/md-checkbox/label/div",
        'fabTrigger' : "//*[@id='entity-table-component']/div[1]/app-entity-table-add-actions/div/smd-fab-speed-dial/div/smd-fab-trigger/button",
        'fabAction' : "//*[@id='entity-table-component']/div[1]/app-entity-table-add-actions/div/smd-fab-speed-dial/div/smd-fab-actions/button"
        }

class create_group_test(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        driver.implicitly_wait(30)
        pass

    #Test navigation Account>Users>Hover>New User and enter username,fullname,password,confirmation and wait till user is  visibile in the list
    def test_01_create_newgroup(self):
        print (" creating a new group without root access")
        time.sleep(5)
        #Click Group submenu
        driver.find_element_by_xpath(xpaths['submenuGroup']).click()
        #scroll down to find hover tab
        driver.find_element_by_tag_name('html').send_keys(Keys.END)
        time.sleep(2)
        #Perform hover to show menu
        hover_element = driver.find_element_by_xpath(xpaths['fabTrigger'])
        hover = ActionChains(driver).move_to_element(hover_element)
        hover.perform()
        time.sleep(1)
        #Click create new group option
        driver.find_element_by_xpath(xpaths['fabAction']).click()
        #Enter New Groupname
        time.sleep(1)
        driver.find_element_by_xpath(xpaths['newGroupName']).send_keys(newgroupname)
        #Click on save new Group button
        driver.find_element_by_xpath("/html/body/app-root/app-admin-layout/md-sidenav-container/div[6]/div/app-group-form/entity-form/md-card/div/form/md-card-actions/button[1]").click()
        #wait to confirm new user in the list visually
        time.sleep(20)

    def test_02_create_supergroup(self):
        print (" creating a new Super group with root access")
        #Click Group submenu
        driver.find_element_by_xpath(xpaths['submenuGroup']).click()
        #Perform hover to show menu
        hover_element = driver.find_element_by_xpath(xpaths['fabTrigger'])
        hover = ActionChains(driver).move_to_element(hover_element)
        hover.perform()
        time.sleep(1)
        #Click create new group option
        driver.find_element_by_xpath(xpaths['fabAction']).click()
        #Enter New Groupname
        time.sleep(1)
        driver.find_element_by_xpath(xpaths['newGroupName']).send_keys(supergroupname)
        #Check Permit Sudo  checkbox
        driver.find_element_by_xpath("//*[@id='2']/form-checkbox/div/md-checkbox/label/div").click()
        #Click on save new Group button
        driver.find_element_by_xpath("/html/body/app-root/app-admin-layout/md-sidenav-container/div[6]/div/app-group-form/entity-form/md-card/div/form/md-card-actions/button[1]").click()
        #wait to confirm new user in the list visually
        time.sleep(20)



    # Next step-- To check if the new user is present in the list via automation


    #method to test if an element is present
    def is_element_present(self, how, what):
        """
        Helper method to confirm the presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try: driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True

    @classmethod
    def tearDownClass(inst):
        #driver.close()
        pass


def run_create_group_test(webdriver):
    global driver
    driver = webdriver
    suite = unittest.TestLoader().loadTestsFromTestCase(create_group_test)
    xmlrunner.XMLTestRunner(output=results_xml, verbosity=2).run(suite)

