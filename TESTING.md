# TESTING.md


## Table of Contents
* Introduction
* Lighthouse Score
* Code Validation
* Manual Testing
* Conclusion

## Introduction
This document provides a comprehensive overview of the testing strategies employed for the Botanica Essentials project. Ensuring the robustness, reliability, and user-friendliness of the application was paramount. Both automated and manual testing methods were utilized, encompassing code validation, continuous integration, performance testing, and thorough functionality checks against user stories and pass criteria.


## Flake8 Integration
Flake8 is integrated within the CI/CD pipeline for linting and checking the Python code for errors. This tool helps maintain code quality and consistency, automatically flagging potential issues like syntax errors, undefined variables, and style violations.


## Lighthouse Score
Google Lighthouse was used to assess the website's performance, accessibility, best practices, and SEO.


Scores Overview
Performance: 91
Accessibility: 82
Best Practices: 95
SEO: 90
These scores guided optimizations, such as improving image loading times, enhancing accessibility features, and refining the site's SEO strategies.


## Code Validation
The codebase underwent rigorous validation to ensure compliance with current standards.


## HTML Validation
The HTML code for key pages including blog, blog detail, contact, FAQ, homepage (index), products, product detail, wishlist, user profile, bag, checkout, and our philosophy was validated using the W3C Markup Validation Service. All these important files passed with no issues, confirming adherence to web standards and enhancing the website's reliability and user experience.

<img width="1512" alt="blog_code_validation" src="https://github.com/Sofia-Bourdon/Botanica-Essentials/assets/112895499/030afb26-a700-423c-b449-af21ad4246c5">

<img width="1512" alt="blog_detail_code_validation" src="https://github.com/Sofia-Bourdon/Botanica-Essentials/assets/112895499/bd2cab0e-b615-45ab-b8d6-a6dfcb60e94d">

<img width="1512" alt="contact_code_valdaton" src="https://github.com/Sofia-Bourdon/Botanica-Essentials/assets/112895499/807a025a-7350-4b56-beaf-d2e633ae7a38">

<img width="1512" alt="faq_code_validation" src="https://github.com/Sofia-Bourdon/Botanica-Essentials/assets/112895499/afb4296d-8d96-474e-a1f8-f1667ddd9778">

<img width="1512" alt="homepage_code_validation" src="https://github.com/Sofia-Bourdon/Botanica-Essentials/assets/112895499/2dcdee8a-73f3-409d-b4af-3eb3670c4fa4">

<img width="1512" alt="product_detail_code_validation" src="https://github.com/Sofia-Bourdon/Botanica-Essentials/assets/112895499/161ff3ec-ccdf-45ba-9187-5711d628195a">

<img width="1512" alt="products_code_validation" src="https://github.com/Sofia-Bourdon/Botanica-Essentials/assets/112895499/2122caae-4688-45c0-a8cb-c5cfddaa5255">

<img width="1512" alt="wishlist_code_validation" src="https://github.com/Sofia-Bourdon/Botanica-Essentials/assets/112895499/af0b93a5-9c51-4a29-a1ef-9f159cdd4b10">


## CSS Validation
The CSS code was validated using the W3C Jigsaw CSS Validator. It passed with no issues, ensuring that the styling of the website adheres to the latest web standards and is consistent across different browsers and devices.

<img width="1512" alt="css_validation" src="https://github.com/Sofia-Bourdon/Botanica-Essentials/assets/112895499/5bf2bacc-9e50-458f-bf0f-807c606d1c37">


## JavaScript Validation
JavaScript validation was conducted using JSLint. The base.js file and all JavaScript code within <script> tags in the templates passed through the JSLint validator without any issues. This ensures that our JavaScript code is free from errors, follows best practices, and maintains a high standard of code quality.

<img width="1512" alt="js_lint_validation" src="https://github.com/Sofia-Bourdon/Botanica-Essentials/assets/112895499/ad8f55dc-a648-4a64-969d-1c7dedbdccd6">


## Python Validation with Flake8
Flake8 played a crucial role in maintaining the quality of Python code. All Python files, except for the env.py file, were thoroughly checked. The env.py file, which is not included in the repository and is only available in the development environment, had minor issues related to the 80-character line length limit. However, these do not affect the overall code quality and functionality.


## Manual Testing

This section outlines the manual tests performed for each user story, including preconditions, steps, expected results, actual results, status, and any additional notes.

## Viewing and Navigation

| ID | User Story | Preconditions | Test Steps | Expected Result | Actual Result | Status |
|----|------------|---------------|------------|-----------------|---------------|--------|
| 1  | View list of products | User is on the homepage. | 1. Navigate to the 'Products' section. | A list of products is displayed for purchase. | Pass |  Pass
| 2  | View Product Details | User is on the list of products. | 1. Click on a product to view details. | Detailed information about the product is displayed. | Pass |  Pass
| 3  | Identify deals and best sellers | User is on the homepage or products page. | 1. Look for sections or labels identifying deals and best sellers. | Deals and best-selling products are highlighted or labeled. | Pass |  Pass
| 4  | View the total of my purchase at any time | Products are added to the shopping cart. | 1. View the cart to see the total price of the items. | The total purchase amount is correctly displayed in the cart. | Pass |  Pass
| 5  | Access the Privacy Policy Page | User is on any page of the website. | 1. Navigate to the Privacy Policy link and click it. | The Privacy Policy page is displayed, and content is readable. | Pass |  Pass
| 6  | Contact customer support | User is on any page of the website. | 1. Navigate to the 'Contact Us' or support section. | Contact options for customer support are available and functional. | Pass |  Pass

## Registration and User Accounts

| ID | User Story | Preconditions | Test Steps | Expected Result | Actual Result | Status |
|----|------------|---------------|------------|-----------------|---------------|--------|
| 7  | Easily register for an account | User is on the registration page. | 1. Complete the registration form and submit it. | User account is created, and the profile page is displayed. | Pass |  Pass
| 8  | Easily log in or out | User has an account. | 1. Enter login credentials and submit.<br>2. Log out from the account. | User can log in and out successfully. | Pass |  Pass
| 9  | Easily recover my password | User has an account and is on the login page. | 1. Click 'Forgot password' and follow the process. | Password recovery instructions are provided. | Pass |  Pass
| 10 | Have a personalized user profile | User is logged in. | 1. Navigate to the profile page. | Personalized user profile details are displayed. | Pass |  Pass
| 11 | Sign up to the newsletter | User is on the homepage or in profile settings. | 1. Enter email into newsletter signup and submit. | Confirmation of subscription to the newsletter is received. | Pass |  Pass

## Sorting and Searching

| ID | User Story | Preconditions | Test Steps | Expected Result | Actual Result | Status |
|----|------------|---------------|------------|-----------------|---------------|--------|
| 12 | Sort a specific category of products | User is on the category page. | 1. Select sorting criteria from the available options. | Products are sorted according to the selected criteria. | Pass |  Pass
| 13 | Filter the list of products | User is on the category page. | 1. Apply different filters to the product list. | Products are filtered according to selected attributes. | Pass |  Pass
| 14 | Search for a product by name or description | User is on the homepage or products page. | 1. Use the search function to find a product. | Search results for the product are displayed. | Pass |  Pass
| 15 | Easily see what I searched for and the number of results | After performing a search. | 1. Review the search results and count. | The search term and number of results are clearly displayed. | Pass |  Pass
| 16 | Heart the Products I Wish to "Save" | User is on the products page. | 1. Click the 'Heart' or save icon on a product. | Product is added to the wishlist or saved items. | Pass |  Pass

## Purchasing and Checkout

| ID | User Story | Preconditions | Test Steps | Expected Result | Actual Result | Status |
|----|------------|---------------|------------|-----------------|---------------|--------|
| 17 | Add Product to Shopping Bag | User is viewing a product. | 1. Select a product and add it to the shopping bag. | Product is added to the shopping bag. | Pass |  Pass
| 18 | Select the Amount of Product | User is adding a product to the bag. | 1. Specify the quantity before adding to the bag. | The correct quantity of the product is added to the shopping bag. | Pass |  Pass
| 19 | View All Products Added to Shopping Bag | Products are in the shopping bag. | 1. View the shopping bag. | All added products and their details are visible. | Pass |  Pass
| 20 | Easily enter my payment information | User is at the checkout page. | 1. Enter payment details in the provided fields. | Payment information is accepted without errors. | Pass |  Pass
| 21 | Feel personal information is safe and secure | User is on the payment page. | 1. Review the security features and encryption indicators. | The site provides assurance of security for personal information. | Pass | Pass 
| 22 | View order confirmation after checkout | User has completed a purchase. | 1. Complete the checkout process. | An order confirmation is displayed with purchase details. | Pass |  Pass
| 23 | Receive an email confirmation after checkout | User has completed a purchase. | 1. Check the email account used for registration after purchase. | An email confirmation of the purchase is received. | Pass |  Pass

## Admin and Management

| ID | User Story | Preconditions | Test Steps | Expected Result | Actual Result | Status |
|----|------------|---------------|------------|-----------------|---------------|--------|
| 24 | Add a product | Admin is logged into the dashboard. | 1. Navigate to the 'Add Product' section.<br>2. Enter product details and save. | New product is added to the store and is visible on the website. | Pass | Pass 
| 25 | Edit/Update products | Admin is logged into the dashboard and is on the products page. | 1. Select a product to edit.<br>2. Update the details and save changes. | The product details are updated on the website. | Pass |  Pass
| 26 | Delete a product | Admin is logged into the dashboard and is on the products page. | 1. Select a product and delete it. | The product is removed from the store and is no longer visible on the website. | Pass | Pass 
| 27 | View lists of products on the admin page | Admin is logged into the dashboard. | 1. Navigate to the 'Products' section. | A list of all products with management options is displayed. | Pass |  Pass
| 28 | View list of categories for products | Admin is logged into the dashboard. | 1. Navigate to the 'Categories' section. | A list of product categories is displayed with options to manage them. | Pass |  Pass
| 29 | View list of messages sent by the users in 'customer support' | Admin is logged into the dashboard. | 1. Navigate to the 'Customer Support' messages section. | A list of messages from users is displayed with options to respond or manage. | Pass |  Pass
| 30 | Add a new product through the product admin panel | Admin is on the product addition page. | 1. Enter details for a new product and submit. | The new product is added and listed in the store. | Pass |  Pass
| 31 | Add a new message in the customer support page | Admin is on the customer support page. | 1. Enter a response to a user's message and submit. | The response is recorded and, if applicable, sent to the user. | Pass |  Pass
| 32 | View a list of wishlists and sort as needed | Admin is logged into the dashboard. | 1. Navigate to the 'Wishlists' section. | Admin can view and manage wishlists created by users. | Pass |  Pass
| 33 | Make a blog post | Admin is logged into the dashboard with blogging privileges. | 1. Navigate to the 'Blog' section.<br>2. Create a new post and publish it. | The new blog post is live on the website. | Pass | Pass 
| 34 | Delete a blog post | Admin is logged into the dashboard and is on the blog page. | 1. Select a blog post and delete it. | The blog post is removed from the website. | Pass |  Pass
| 35 | View blog posts on the blog page | User is on the blog page. | 1. Navigate to the 'Blog' section from the main menu or homepage link. | A list of blog posts is displayed with titles, excerpts, and publication dates. | Pass | Pass
| 36 | View blog detail when clicking "Read More" | User is on the blog page. | 1. Find a blog post.<br>2. Click the 'Read More' link associated with a blog post. | The detailed view of the blog post is displayed, including full content and images if present. | Pass |  Pass


## Conclusion
The testing procedures applied to the Botanica Essentials project have ensured that each feature functions as intended and adheres to the design requirements. Automated checks for code quality and performance have complemented manual user story validation, providing a well-rounded examination of the project's capabilities. As the project evolves, the testing framework established here will serve as a cornerstone for ongoing quality assurance and will be adapted to meet future needs.
