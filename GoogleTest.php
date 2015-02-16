<?php
require_once 'Testing/Selenium.php';
require_once 'PHPUnit/Framework/TestCase.php';
 
class SeleniumTest extends PHPUnit_Framework_TestCase {
    private $selenium;
 
    public function setUp()     {
        $this->selenium = new Testing_Selenium("*firefox", "http://yahoo.com");
        $this->selenium->start();
    }
 
    public function tearDown()     {
        $this->selenium->stop();
    }
 
    public function testSite()     {
        $this->selenium->open("/");
        $this->selenium->type("q", "hello world");
        $this->selenium->click("btnG");
        $this->selenium->waitForPageToLoad(10000);
        $this->assertRegExp("/Поиск в Google/", $this->selenium->getTitle());
    }
}
