@attribute_smart @singleEdit
Feature: Single Edit
  Single Edit functionalities

  @AS-183
  Scenario Outline: User validates the display and filter options in explore category page
    Given User is on the Explore Batch Page
    Then User selects <L2 Category> under the respective <L1 Level>
    Then User should be land on Explore Category page
    Then User should see the status tabs
      | Status Tabs |
      | All         |
      | Pending     |
      | Reviewed    |
    Then User should be able to see the filter options with confidence and the <attributes>
    Then User clicks on <attributes> dropdown and get a list of dynamic <sub-attributes>
    Examples:
      | L1 Level | L2 Category | attributes                | sub-attributes                                             |
      | Mens     | Shirts      | Sleeve Length, Print Type | Sleeve Length:Long Sleeve + 3/4 Sleeve, Print Type:Graphic |
      | Mens     | Pants       | Pant Length, Leg Fit      | Pant Length:Full Length, Leg Fit:Straight                  |
      | Womens   | Tops        | Sleeve Length, Print Type | Sleeve Length:Long Sleeve + 3/4 Sleeve, Print Type:Graphic |
      | Womens   | Pants       | Pant Length, Leg Fit      | Pant Length:Full Length, Leg Fit:Straight                  |

  @AS-183
  Scenario Outline: User validates filter functionalities in explore category page when performing single edit
    Given User is on the Explore Batch Page
    Then User selects <L2 Category> under the respective <L1 Level>
    Then User should be land on Explore Category page
    When User selects a single <existing sub-attribute> under an <attribute> in filters
    Then User should get Single Edit feature enabled
    And  The selected "Filters Applied" should appear at the top with a <new sub-attribute> value and cross
    And User will be able to see the changed breadcrumbs on top as "Single edit"
    When User changes the <existing sub-attribute> to a <new sub-attribute> which was not available
    And User clicks on "Save Edits" button
    Then User validates if "Changes Saved Successfully " success message pops up
    And User validates whether the <new sub-attribute> value gets added to the list of <attribute>
    When User clicks on the <existing sub-attribute> in the "Filters Applied"
    Then The filter should disappear
    Examples:
      | L1 Level | L2 Category | attribute     | existing sub-attribute | new sub-attribute |
      | Mens     | Shirts      | Sleeve Length | Long Sleeve            | 3/4 Sleeve        |
      | Mens     | Pants       | Pant Length   | Full Length            | Capri             |
      | Womens   | Tops        | Sleeve Length | Long Sleeve            | Short Sleeve      |
      | Womens   | Pants       | Leg Fit       | Straight               | Wide Leg          |

  @AS-184
  Scenario Outline: User validates the behavior in explore category page when performing single edit
    Given User is on the Explore Batch Page
    Then User selects <L2 Category> under the respective <L1 Level>
    Then User should be land on Explore Category page
    When User selects a single <existing sub-attribute> under an <attribute> in filters
    And User changes the <existing sub-attribute> to a <new sub-attribute> which was not available
    Then Dropdown box will be displayed with yellow border before saving
    And User clicks on "Save Edits" button
    Then Yellow border should go to default
    And "Edited" tag appears on the top left of that image
    When User hovers over the image
    Then The enlarged form of the image should be displayed
    Examples:
      | L1 Level | L2 Category | attribute     | existing sub-attribute | new sub-attribute |
      | Mens     | Shirts      | Sleeve Length | Long Sleeve            | 3/4 Sleeve        |
      | Mens     | Pants       | Pant Length   | Full Length            | Capri             |
      | Womens   | Tops        | Sleeve Length | Long Sleeve            | Short Sleeve      |
      | Womens   | Pants       | Leg Fit       | Straight               | Wide Leg          |

  @AS-185
  Scenario Outline: User validates the behavior in explore category page when clicking on save edits
    Given User is on the Explore Batch Page
    Then User selects <L2 Category> under the respective <L1 Level>
    Then User should be land on Explore Category page
    When User selects a single <existing sub-attribute> under an <attribute> in filters
    And User changes the <existing sub-attribute> to a <new sub-attribute> which was not available
    Then User clicks on "Save Edits" button
    And User clicks on "Clear All" button
    And User selects a single <new sub-attribute> under an <attribute> in filters
    Then User will be able to see only the edited image with Edited tag at top left
    When User makes no changes in the <new sub-attribute>
    And User clicks on "Save Edits" button
    Then User validates "You have not made any changes" toast message pops up
    Examples:
      | L1 Level | L2 Category | attribute     | existing sub-attribute | new sub-attribute |
      | Mens     | Shirts      | Sleeve Length | Long Sleeve            | 3/4 Sleeve        |
      | Mens     | Pants       | Pant Length   | Full Length            | Capri             |
      | Womens   | Tops        | Sleeve Length | Long Sleeve            | Short Sleeve      |
      | Womens   | Pants       | Leg Fit       | Straight               | Wide Leg          |

  @AS-185
  Scenario Outline: User validates the behavior in explore category page when clicking on save all
    Given User is on the Explore Batch Page
    Then User selects <L2 Category> under the respective <L1 Level>
    Then User should be land on Explore Category page
    When User selects a single <existing sub-attribute> under an <attribute> in filters
    And User changes the <existing sub-attribute> to a <new sub-attribute> which was not available for few products
    And User clicks on "Save All" button
    Then User gets a confirmation pop up with the message "Do you want to save all the products? All Products displayed on this page (edited or not edited) will be considered as reviewed. Do you want to proceed?"
    When User clicks on "Yes" button on the confirmation popup
    Then All the images of that page will be finalized
    And User will get a pop up message "Changes made successfully"
    And All the images of that page will have "Reviewed" tag at the top left of the images
    And User clicks on "Clear All" button
    When User selects a single <new sub-attribute> under an <attribute> in filters
    And User changes the <new sub-attribute> to a <existing sub-attribute> which was not available for few products
    When User clicks on "No" button on the confirmation popup
    Then User remains on the same Explore Category page and no changes implemented
    Examples:
      | L1 Level | L2 Category | attribute     | existing sub-attribute | new sub-attribute |
      | Mens     | Shirts      | Sleeve Length | Long Sleeve            | 3/4 Sleeve        |
      | Mens     | Pants       | Pant Length   | Full Length            | Capri             |
      | Womens   | Tops        | Sleeve Length | Long Sleeve            | Short Sleeve      |
      | Womens   | Pants       | Leg Fit       | Straight               | Wide Leg          |

  @AS-186
  Scenario Outline: User validates top-bar functionalities in explore category page
    Given User is on the Explore Batch Page
    Then User selects <L2 Category> under the respective <L1 Level>
    Then User should be land on Explore Category page
    And User should be able to see the Images toggle at the top
    And User will be able to see the Breadcrumbs
    When User clicks on the Breadcrumbs of "Explore"
    Then User can navigate to category and batch pages
    Examples:
      | L1 Level | L2 Category |
      | Mens     | Shirts      |
      | Mens     | Pants       |
      | Womens   | Tops        |
      | Womens   | Pants       |

  @AS-187
  Scenario Outline: User validates if he can move across the application during single edit
    Given User is on the Explore Batch Page
    Then User selects <L2 Category> under the respective <L1 Level>
    Then User should be land on Explore Category page
    When User selects a single <existing sub-attribute> under an <attribute> in filters
    And User changes the <existing sub-attribute> to a <new sub-attribute> which was not available for few products
    When User clicks on the Breadcrumbs of "Explore"
    Then User should get a confirmation popup "Are you sure you want to leave this page without saving the changes ?"
    When User clicks on "No" button on the confirmation popup
    Then User will still be on the current page
    When User clicks on the Breadcrumbs of "Explore"
    Then User should get a confirmation popup "Are you sure you want to leave this page without saving the changes ?"
    When User clicks on "Yes" button on the confirmation popup
    Then User will be moved to the destination page
    Then User selects <L2 Category> under the respective <L1 Level>
    Then User should be land on Explore Category page
    When User has made no edits on the page
    And User clicks on the dashboard
    Then No confirmation popup will appear
    And User lands on Attribute Smart Dashboard Page
    Examples:
      | L1 Level | L2 Category | attribute     | existing sub-attribute | new sub-attribute |
      | Mens     | Shirts      | Sleeve Length | Long Sleeve            | 3/4 Sleeve        |
      | Mens     | Pants       | Pant Length   | Full Length            | Capri             |
      | Womens   | Tops        | Sleeve Length | Long Sleeve            | Short Sleeve      |
      | Womens   | Pants       | Leg Fit       | Straight               | Wide Leg          |


  @AS-188 @AS-183
  Scenario Outline: User validates the behavior of the application when multiple attributes are selected in the filters in explore category page
    Given User is on the Explore Batch Page
    Then User selects <L2 Category> under the respective <L1 Level>
    When clicks on the <multiple attributes> in the filter option
    Then validates single edit functionality is not be allowed
    Then validates if on clicking the product image the application is directed to explore product page
    Then validates Save and Save all buttons will not be present in the explore category page
    Then validates Top bar functionalities remain functional
    Then All the selected sub-attributes should appear at the top
    And User clicks on "Clear All" button
    Then All the filters should be removed
    Examples:
      | L1 Level | L2 Category | multiple attributes                                        |
      | Mens     | Shirts      | Sleeve Length:Long Sleeve + 3/4 Sleeve, Print Type:Graphic |
      | Mens     | Pants       | Pant Length:Full Length, Leg Fit:Straight                  |
      | Womens   | Tops        | Sleeve Length:Long Sleeve + 3/4 Sleeve, Print Type:Graphic |
      | Womens   | Pants       | Pant Length:Full Length, Leg Fit:Straight                  |
