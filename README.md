# Overview
## Test Description
Select a standing desk and test "Design My Own" flow,by:
- Test 1: Clicking on "Design my own" primary button.
- Test 2: clicking on "Design my own" button on sticky bar.
  To make sure that users are able to see Complete Setup option before checking out their purchase (Add to Cart button should not be visible in adjustable page).

## Test environment
- Selenium webdriver using Python 3
- Test is running on Chrome using Chrome Webdriver.

# Usage
## Installation
Uses virtualenv for python dependencies. Activate and install by running
1. Install chrome webdriver to `%USERPROFILE%\SeleniumWebDrivers\chromedriver.exe`
1. Install dependencies via pip
```
> cd Fully-SampleTest\
> venv\Scripts\activate
> pip install -r requirements.txt
```

## Running Tests
Execute via nose2 test framework
```

(venv) C:\Users\kim\PycharmProjects\Fully-SampleTest>nose2

DevTools listening on ws://127.0.0.1:58304/devtools/browser/d9c72903-278b-4345-a82c-019609f25301
F
DevTools listening on ws://127.0.0.1:50836/devtools/browser/e8b9e3d6-a0c5-4657-ae8b-4041af32ad16
[20120:8392:0909/101438.244:ERROR:device_event_log_impl.cc(214)] [10:14:38.244] USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection: A device attached to the system is not functioning. (0x1F)
[20120:8392:0909/101438.287:ERROR:device_event_log_impl.cc(214)] [10:14:38.286] USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection: A device attached to the system is not functioning. (0x1F)
[20120:8392:0909/101438.288:ERROR:device_event_log_impl.cc(214)] [10:14:38.288] USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection: A device attached to the system is not functioning. (0x1F)
F
======================================================================
FAIL: test_complete_your_setup_primary_button_flow (test_design_my_own_flow.BasicTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\kim\PycharmProjects\Fully-SampleTest\tests\test_design_my_own_flow.py", line 81, in test_complete_your_setup_primary_button_flow
    assert not DesignPage(self.chrome).is_add_to_cart_visible(), "Make sure add to cart is not visible"
AssertionError: Make sure add to cart is not visible

======================================================================
FAIL: test_complete_your_setup_stick_button_flow (test_design_my_own_flow.BasicTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\kim\PycharmProjects\Fully-SampleTest\tests\test_design_my_own_flow.py", line 75, in test_complete_your_setup_stick_button_flow
    assert not DesignPage(self.chrome).is_add_to_cart_visible(), "Make sure add to cart is not visible"
AssertionError: Make sure add to cart is not visible

----------------------------------------------------------------------
Ran 2 tests in 83.916s

FAILED (failures=2)
```
