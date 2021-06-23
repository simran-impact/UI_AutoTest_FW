@attribute_smart @uploadProcess_batch @dashboard_page
Feature: Upload and Process Batch
  Attribute Smart Upload and Process Batch

  @dashboard_test
  Scenario: User logs into the application and validates the available columns in the batch table
    Given User logs into the application
    When User clicks on "AttributeSmart" button in IA Smart Platform application page
    And User lands on Attribute Smart Dashboard Page
    Then User validates the columns available in the batch table
      | Column Names    |
      | Batch Name      |
      | Products Uploaded |
      | Products Tagged   |
      | Tags Generated  |
      | Tags Edited   |
      | Tags Reviewed  |
      | Actions         |

  @upload_csv_test
  Scenario: User downloads the sample CSV required to create a batch
    Given User logs into the application
    When User clicks on "AttributeSmart" button in IA Smart Platform application page
    And User lands on Attribute Smart Dashboard Page
    Then User clicks on Upload button on the Dashboard Page
    Then User clicks on the download input template button on the create batch tab
    And checks if the file is downloaded successfully

  @upload_csv_test @batch_action_test
  Scenario: User creates a batch by uploading a CSV file in the expected format successfully and deletes the batch successfully
    Given User logs into the application
    When User clicks on "AttributeSmart" button in IA Smart Platform application page
    And User lands on Attribute Smart Dashboard Page
    Then User clicks on Upload button on the Dashboard Page
    And Enters the new batch name in the Create Batch Tab and uploads CSV file
      | Test Condition         | Upload File        |
      | CSV in Expected Format | expectedFormat.csv |
    Then User validates if "Batch created successfully." success message pops up
    Then User checks if the created batch name is displayed in the batch table on Dashboard Page with following
      | Test Condition         | Values to Check |
      | Batch Name             | Present         |
      | Num of images uploaded | 10              |
      | Num of broken urls     | 0               |
      | Images Uploaded        | 10              |
      | Images Tagged          | 10              |
      | Tags Generated         | 0               |
      | Tags Reviewed          | 0               |
      | Tags Finalized         | 0               |
      | Actions                | Present         |
    Then User performs "DELETE :: YES" action on the created Batch present in the batch table
    And User validates if "Batch deleted successfully." success message pops up
    And checks if the Batch is deleted from the batch table


  @upload_csv_test
  Scenario: User validates error when trying to create batch by not entering batch name and uploading the CSV
    Given User logs into the application
    When User clicks on "AttributeSmart" button in IA Smart Platform application page
    And User lands on Attribute Smart Dashboard Page
    Then User clicks on Upload button on the Dashboard Page
    And Does not enter batch name in the Create Batch Tab and uploads CSV file
      | Test Condition         | Upload File        |
      | CSV in Expected Format | expectedFormat.csv |
    Then User validates if "Batch Name: This field may not be blank." error message pops up

  @upload_csv_test
  Scenario: User try to create a batch by uploading a CSV file in an incorrect format and validates error message
    Given User logs into the application
    When User clicks on "AttributeSmart" button in IA Smart Platform application page
    And User lands on Attribute Smart Dashboard Page
    Then User clicks on Upload button on the Dashboard Page
    And Enters the new batch name in the Create Batch Tab and uploads CSV file
      | Test Condition             | Upload File         |
      | CSV in an incorrect format | incorrectFormat.csv |
    Then User validates if "File: Columns does not match to sample sheet. Please check for sample file." error message pops up

  @upload_csv_test
  Scenario: User try to create a batch by uploading a CSV file with more then 10000 rows and validates error message
    Given User logs into the application
    When User clicks on "AttributeSmart" button in IA Smart Platform application page
    And User lands on Attribute Smart Dashboard Page
    Then User clicks on Upload button on the Dashboard Page
    And Enters the new batch name in the Create Batch Tab and uploads CSV file
      | Test Condition       | Upload File       |
      | CSV with 10000+ rows | 10000PlusRows.csv |
    Then User validates if "File: The number of rows are too large, Must be less than 10000." error message pops up

  @upload_csv_test
  Scenario: User try to create a batch by uploading a CSV file which contains zero images and validates error message
    Given User logs into the application
    When User clicks on "AttributeSmart" button in IA Smart Platform application page
    And User lands on Attribute Smart Dashboard Page
    Then User clicks on Upload button on the Dashboard Page
    And Enters the new batch name in the Create Batch Tab and uploads CSV file
      | Test Condition       | Upload File  |
      | CSV with zero images | emptyCSV.csv |
    Then User validates if "File: The file must contain at least one image." error message pops up

  @upload_csv_test @batch_action_test
  Scenario: User creates a batch by uploading a CSV file containing broken urls successfully and clicks on the warning to download the broken urls
    Given User logs into the application
    When User clicks on "AttributeSmart" button in IA Smart Platform application page
    And User lands on Attribute Smart Dashboard Page
    Then User clicks on Upload button on the Dashboard Page
    And Enters the new batch name in the Create Batch Tab and uploads CSV file
      | Test Condition      | Upload File      |
      | CSV with broken url | brokenUrlCSV.csv |
    Then User validates if "Batch created successfully." success message pops up
    Then User checks if the created batch name is displayed in the batch table on Dashboard Page with following
      | Test Condition         | Values to Check |
      | Batch Name             | Present         |
      | Num of images uploaded | 14              |
      | Num of broken urls     | 5               |
      | Images Uploaded        | 9               |
      | Images Tagged          | 9               |
      | Tags Generated         | 0               |
      | Tags Reviewed          | 0               |
      | Tags Finalized         | 0               |
      | Actions                | Present         |
    Then User performs "WARNING" action on the created Batch present in the batch table
    And User validates if "5 broken URL's from <Batch Name> batch have been downloaded successfully." success message pops up
    And checks if the file is downloaded successfully
    Then User performs "DELETE :: YES" action on the created Batch present in the batch table
    And User validates if "Batch deleted successfully." success message pops up

  @upload_csv_test @batch_action_test
  Scenario: User creates a batch successfully and downloads the batch once all the images are uploaded successfully
    Given User logs into the application
    When User clicks on "AttributeSmart" button in IA Smart Platform application page
    And User lands on Attribute Smart Dashboard Page
    Then User clicks on Upload button on the Dashboard Page
    And Enters the new batch name in the Create Batch Tab and uploads CSV file
      | Test Condition         | Upload File        |
      | CSV in Expected Format | expectedFormat.csv |
    Then User validates if "Batch created successfully." success message pops up
    Then User checks if the created batch name is displayed in the batch table on Dashboard Page with following
      | Test Condition         | Values to Check |
      | Batch Name             | Present         |
      | Num of images uploaded | 10              |
      | Num of broken urls     | 0               |
      | Images Uploaded        | 10              |
      | Images Tagged          | 10              |
      | Tags Generated         | 0               |
      | Tags Reviewed          | 0               |
      | Tags Finalized         | 0               |
      | Actions                | Present         |
    Then User performs "DOWNLOAD" action on the created Batch present in the batch table
    And User validates if "Batch downloaded successfully." success message pops up
    And checks if the file is downloaded successfully
    Then User performs "DELETE :: YES" action on the created Batch present in the batch table
    And User validates if "Batch deleted successfully." success message pops up