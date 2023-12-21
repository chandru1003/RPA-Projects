# IT Support Task Automation Bot 

## Overview

This repository contains the implementation of an IT Support Task Automation Bot designed to streamline and enhance various aspects of IT support operations. The bot automates routine tasks, improves response times, and contributes to overall operational efficiency

## Features
1. **Null Value Handling:** Checks for null values in ticket data and removes them.

2. **Ticket Status Update:** Updates ticket status based on resolutions and customer ratings, automatically closing resolved tickets.

3. **Ticket Categorization:** Assigns tickets to specialist employees based on categorization criteria.

4. **Individual Employee Assignment:** Sends individualized lists of tickets to respective specialist employees.

5. **Customer Rating Collection:** Requests customer ratings for closed tickets and sends reminders if not provided.

6. **Employee Rating Feedback:** Sends employee performance ratings collected from customers.

## Identified Repetitive Tasks for RPA Automation

1. **Ticket Categorization and Routing:**
    - Automated the categorization of tickets into specific types and routed them to relevant teams based on predefined categories, as outlined in the provided designation-to-category mapping table.

##### Ticket Categories and Assigned Designation


| S. No. | Designation                          | Ticket Categories                                       |
|--------|--------------------------------------|---------------------------------------------------------|
| 1      | Installation Expert                  | {"Installation support"}                                |
| 2      | Peripheral Compatibility Specialist | {"Peripheral compatibility"}                           |
| 3      | Product Recommendation Specialist    | {"Product recommendation"}                              |
| 4      | Refund and Payment Specialist        | {"Payment issue", "Refund request"}     |
| 5      | Display and Product Setup Expert     | {"Display issue", "Product setup"}                      |
| 6      | Technical Analyst                    | {"Account access", "Product Compatibility"}             |
| 7      | Software Engineer                    | {"Software bug","Data loss"}                       |
| 8      | Hardware Specialist                  | {"Hardware issue","Battery life"}          |
| 9      | Network Engineer                      | {"Network problem"}                                     |
| 10     | General Specialist                   | {"Delivery problem", "Cancellation request"}            |

2. **Ticket Status Updates:**
   - Implemented a bot to streamline the process of automatically updating ticket statuses, ensuring timely and accurate status changes based on resolutions or customer responses.

3. **Ticket Priority Assessment:**
   - Developed a bot to analyze ticket details and assign priority levels based on predefined criteria for efficient issue resolution.

4. **Customer Satisfaction Survey Analysis:**
   - Created a bot for aggregating and analyzing customer satisfaction ratings to gather insights for service improvement.

5. **Ticket Escalation Handling:**
   - Developed a bot to automatically analyze ticket details and escalate tickets based on predefined criteria for prompt issue resolution.

6. **Tickets Report**
   - Implemented a reporting system to generate comprehensive reports on ticket data, offering insights into support operations and performance.

7. Customer Reminder: 
 -Sends an email prompt to customers requesting necessary details if any essential information is found to be null.
## How to Use

1. Download or clone the repository.
2. Explore the dataset file [Kaggle](https://www.kaggle.com/datasets/suraj520/customer-support-ticket-dataset).
3. Consider the identified repetitive tasks for potential RPA implementation.
4. Adapt and customize the RPA solutions based on your specific requirements.

Feel free to contribute or provide feedback!

### License
This project is licensed under the [MIT](https://opensource.org/license/mit/) License. See the LICENSE file for details.

Happy Automating!
