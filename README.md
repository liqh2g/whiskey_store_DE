
## **Data Engineering Project - Whiskey Store**
---
# **Overview**
- In this simulated project, I have devised a comprehensive data architecture for an imaginary whiskey retail store, allowing shop managers to utilize their data for informed decision-making.
- Data used in the project:
    - Data in the process of collection from alcohol exchange website.
    - Randomly generated data, consistent with the data collected above.
---
# **Project Architecture**
![Alt text](/image/image-2.png)

# About the ETL processing
The process consits of:   
- The first part of the process is web scraping method, in which I use Selenium, BeautifulSoup for ingesting data from the whiskey exchange website.
- The second part covers data processing and transformation and designing Database. 
    - In this section, data is generated using Faker library, the above random data generation is optional, this data can be used for data visualization and analysis. 
    - Before designing the central database, the data corresponding to each table will be normalized to minimize redundancy in the database and maximize database integrity. Each table will be normalized to meet the requirements of the first, second and then third normal form(3NF). Only when everything is done, the entire schema will be loaded to the database.
- The final part is the process of designing a Data Warehouse:
    - For this project, the main business process is simply the collection of actions required for selling whiskey to clients. So the grain in this case will describe a customer buying a single product at a specific time. Based on the above factors, I will build a suitable data warehouse. The star schema design model is used to apply dimensionality to the Data Warehouse.
    - Several triggers are created that will load data from central databse into the Data Warehouse and sync the database and the Data Warehouse when certain situation occur in the organization.