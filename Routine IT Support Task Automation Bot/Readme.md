# IT Support Automation with RPA - Ticket Dataset

## Overview

This repository contains a dataset related to customer support tickets in an IT environment. The dataset includes various fields such as customer information, ticket details, and resolution data. The goal is to identify repetitive tasks within this dataset that can be automated using Robotic Process Automation (RPA) to enhance the efficiency of IT support processes.


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

## How to Use

1. Download or clone the repository.
2. Explore the dataset file [Kaggle](https://www.kaggle.com/datasets/suraj520/customer-support-ticket-dataset).
3. Consider the identified repetitive tasks for potential RPA implementation.
4. Adapt and customize the RPA solutions based on your specific requirements.

Feel free to contribute or provide feedback!
