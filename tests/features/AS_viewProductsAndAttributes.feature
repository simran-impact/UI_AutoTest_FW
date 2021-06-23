@attribute_smart @viewProducts_andAttributes
Feature: View Products and Attributes
  Attribute Smart View Products and Attributes

  @explore_batch
  Scenario: User creates a batch successfully by uploading a CSV file with 100 images and products assigned to it clicks on the batch to explore it
    Given User logs into the application
    When User clicks on "AttributeSmart" button in IA Smart Platform application page
    And User lands on Attribute Smart Dashboard Page
    Then User creates a batch and uploads a csv with "100 images" and products assigned to it
      | Test Condition           | Test Value           |
      | CSV to upload            | exploreBatchData.csv |
      | Num of products uploaded | 100                  |
      | Products Uploaded        | 100                  |
      | Products Tagged          | 100                  |
      | Tags Generated           |                      |
    When User clicks on the batch which was created
    And User lands on the Explore Batch Page

  @explore_batch
  Scenario: User checks if the created batch can be exported from the explore batch page
    Given User logs into the application
    When User clicks on "AttributeSmart" button in IA Smart Platform application page
    And User lands on Attribute Smart Dashboard Page
    When User clicks on the batch which was created
    And User lands on the Explore Batch Page
    Then User clicks on Export button on the Explore Batch Page
    And checks if the file is downloaded successfully

  @explore_batch
  Scenario: User checks if L1 and L2 categories are grouped as per the csv which was uploaded
    Given User logs into the application
    When User clicks on "AttributeSmart" button in IA Smart Platform application page
    And User lands on Attribute Smart Dashboard Page
    When User clicks on the batch which was created
    And User lands on the Explore Batch Page
    Then User checks if the L1 categories are created as per the csv which was uploaded
    Then User checks if the L2 categories are created under the respective L1's as per the csv which was uploaded

#  @explore_batch
#  Scenario: User checks if the Sort by  Dropdown is working for respective L1 and L2 categories
#    Given User logs into the application
#    When User clicks on "AttributeSmart" button in IA Smart Platform application page
#    And User lands on Attribute Smart Dashboard Page
#    When User clicks on the batch which was created
#    And User lands on the Explore Batch Page
#    Then User checks if the SortBy option is available for all the L1's
#    And User checks if the SortBy options are working as expected in the explore batch for the respective L1's
#      | Sort By      |
#      | A TO Z ORDER |
#      | NO OF IMAGES |
#      | NO OF TAGS   |

  @explore_batch
  Scenario: User checks if the Number of products are uploaded and tagged as expected on the respective L2 categories on explore batch page
    Given User logs into the application
    When User clicks on "AttributeSmart" button in IA Smart Platform application page
    And User lands on Attribute Smart Dashboard Page
    When User clicks on the batch which was created
    And User lands on the Explore Batch Page
    Then User checks if the number products are uploaded and tagged as expected on the respective L2 categories on explore batch page
    And checks if the progress bar is displayed

  @explore_category
  Scenario: User validates if he is taken to the explore category page as expected once he clicks on a respective category in explore batch page
    Given User logs into the application
    When User clicks on "AttributeSmart" button in IA Smart Platform application page
    And User lands on Attribute Smart Dashboard Page
    When User clicks on the batch which was created
    And User lands on the Explore Batch Page
    Then User selects <L2 Category> under the respective <L1 Level>
    Then User should be land on Explore Category page
    Then User validates if the filter options are open with the attribute
    And validates if the product number in displayed in the top like "Showing 1-40 of 246"

  @explore_product
  Scenario: User validates if he is taken to the explore product page as expected once he clicks on a product in explore category page
    Given User logs into the application
    When User clicks on "AttributeSmart" button in IA Smart Platform application page
    And User lands on Attribute Smart Dashboard Page
    When User clicks on the batch which was created
    And User lands on the Explore Batch Page
    Then User selects <L2 Category> under the respective <L1 Level>
    Then User should be land on Explore Category page
    Then User clicks on a product in the explore category page
    And validates if he is taken to the explore product page
    Then User checks if the attributes are displayed as expected
    And checks if the image is displayed of the product
    And checks if the other images in the same product are displayed as a thumbnail

  @explore_product
  Scenario: User validates if Save, Cancel and Go back buttons are working as expected in the explore product page
    Given User logs into the application
    When User clicks on "AttributeSmart" button in IA Smart Platform application page
    And User lands on Attribute Smart Dashboard Page
    When User clicks on the batch which was created
    And User lands on the Explore Batch Page
    Then User selects <L2 Category> under the respective <L1 Level>
    Then User should be land on Explore Category page
    Then User clicks on a product in the explore category page
    And validates if he is taken to the explore product page
    Then User makes few changes in the attributes
    And Clicks on "CANCEL" button in explore product page
    And checks if the attribute changes made are reversed successfully in explore product page
    Then User makes few changes in the attributes
    And Clicks on "SAVE" button in explore product page
    Then User validates if "Success: Changes saved successfully" success message pops up
    And checks if the attribute changes made are saved successfully in explore product page
    Then Clicks on "GO BACK" button in explore product page
    Then User is redirected to the explore category page


  @explore_product
  Scenario: User validates if Go Back scenario are working as expected in the explore product page
    Given User logs into the application
    When User clicks on "AttributeSmart" button in IA Smart Platform application page
    And User lands on Attribute Smart Dashboard Page
    When User clicks on the batch which was created
    And User lands on the Explore Batch Page
    Then User selects <L2 Category> under the respective <L1 Level>
    Then User should be land on Explore Category page
    Then User clicks on a product in the explore category page
    And validates if he is taken to the explore product page
    Then User makes few changes in the attributes
    And Clicks on "GO BACK" button in explore product page
    Then validates if "Leave Page" pop up tab appears
    When User clicks on "NO" button on the leave page tab
    Then User stays on the same explore product page where attribute changes made are the same
    And Clicks on "GO BACK" button in explore product page
    Then validates if "Leave Page" pop up tab appears
    When User clicks on "YES" button on the leave page tab
    Then User is redirected to the explore category page

