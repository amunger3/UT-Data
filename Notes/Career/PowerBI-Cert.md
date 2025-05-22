# PowerBI Certification Practice Questions

## Question Types:

    - Multiple choice questions (advanced scenarios)
    - True/False questions (conceptual understanding)
    - Fill-in-the-blank questions (DAX and technical knowledge)
    - Complex scenario-based questions (real-world applications)

1. You have a Power BI dataset with a fact table containing 50 million rows. Users report slow query performance when filtering by date ranges. The date column is stored as text in 'MM/DD/YYYY' format. What is the BEST approach to optimize performance?
    (A) Create a calculated column to convert text to date format
    (B) Create a separate Date dimension table with proper relationships
    *(C)* Use Power Query to transform the text column to Date data type
    (D) Create a measure using DATEVALUE function

2. In a composite model, you have DirectQuery tables from SQL Server and Import tables from Excel. A user needs a report showing real-time sales data (DirectQuery) alongside historical trends (Import). What limitation must you consider?
    (A) Cross-source relationships are not supported
    (B) DirectQuery tables cannot be used in the same report as Import tables
    *(C)* Aggregations across different storage modes have limitations
    (D) Row-level security cannot be applied to composite models

3. You need to implement row-level security where sales managers can only see data for their assigned territories. The security logic requires checking multiple conditions across different tables. Which approach is MOST secure and efficient?
    (A) Create a calculated table with security mappings
    (B) Use USERNAME() function in a measure
    (C) Implement dynamic RLS using USERPRINCIPALNAME() with filter tables
    (D) Create separate datasets for each territory

4. *True or False*: In Power BI, you can create a many-to-many relationship between two tables without using a bridge table if both tables contain duplicate values in the relationship columns. *True*

5. *True or False*: When using incremental refresh, the partition function parameters must be declared as Date/Time data type in Power Query.

6. *True or False*: A calculated column can reference measures, but a measure cannot reference calculated columns. *False*

7. To create a time intelligence measure that shows sales for the same period last year, you would use the _______ function. The complete DAX formula would be: `Sales LY = CALCULATE([Total Sales], _______('Date'[Date], -1, YEAR))`

8. When implementing a calculated table for date dimension, the function `CALENDAR` is commonly used to generate a continuous range of dates. To ensure the table refreshes properly with new data, you should reference `min` and `max` values from your fact table.

9. To optimize a DirectQuery model with complex calculations, you should push computations to the *database* level using *stored procedures* rather than complex DAX measures.

10. You're building a Power BI solution for a retail company with the following requirements:
    - Sales data from multiple regions (50GB+ each)
    - Real-time inventory updates needed
    - Historical trend analysis going back 5 years
    - Users need to slice by product hierarchy (Category > Subcategory > Product)
    - Regulatory requirement to audit all data access
    - Question: Design the optimal data architecture and explain your storage mode choices.
To design an optimal Power BI solution for a retail company with these requirements, consider the following data architecture and storage mode choices:

**Claude Answer**

**1. Data Source and Storage Architecture:**

- **Data Warehouse Layer:**
  - Use a scalable cloud-based or on-premises data warehouse (e.g., Azure Synapse Analytics, Snowflake, or SQL Server Large Scale) to centralize and store raw data.
  - Data from multiple regions can be ingested via ETL/ELT pipelines, ensuring data normalization and consistency.

- **Data Modeling Layer:**
  - Implement a Data Mart or Layered Data Model (Star Schema) tailored for reporting:
    - **Fact tables:** Sales, Inventory Levels, Transactions
    - **Dimension tables:** Product Hierarchy, Region, Time, Customer, etc.

- **Historical Data:**
  - Store detailed historical data up to 5 years.
  - Use partitioning (by date) to optimize query performance.

- **Real-time Inventory Updates:**
  - For near real-time updates, integrate a **streaming layer**:
    - Use a message broker (e.g., Kafka, Azure Event Hub) to capture inventory updates.
    - Load these updates into a **dedicated Operational Data Store (ODS)** or staging area.
    - Alternatively, use data warehouse features supporting real-time data (e.g., Azure Synapse's Materialized Views).

---

**2. Storage Mode Choices in Power BI:**

- **Import Mode:**
  - Suitable for historical and aggregated data.
  - Benefits:
    - Fast query performance.
    - Better compression.
  - Use for:
    - Historical trend analysis.
    - Date-based aggregations.

- **DirectQuery / Live Connection:**
  - Necessary for real-time inventory updates.
  - Benefits:
    - Always current data.
    - No need to refresh cache.
  - Use for:
    - Dashboard views displaying inventory levels.
    - Critical operational reports with real-time data.

- **Composite Models:**
  - Combine Import and DirectQuery to optimize performance:
    - Import historical data for analysis.
    - Use DirectQuery for real-time operational data.

---

**3. Security and Auditing:**

- Implement Row-Level Security (RLS) based on user roles for data access control.
- Configure Power BI Audit Logs:
  - Capture user interactions with reports.
  - Use Power BI's audit logging features or integrate with Azure Monitor/Audit logs.
- Enforce data access policies at source or via Power BI security settings.

---

**Summary:**

- Use a centralized data warehouse with partitioned historical data.
- Implement streaming pipelines for real-time inventory updates.
- Model data in star schema for efficient slicing by product hierarchy.
- Deploy a hybrid storage mode: Import for historical data, DirectQuery for real-time data, possibly combined as composite models.
- Enforce robust security and data auditing on all access points.

This architecture balances performance, scalability, real-time requirements, and compliance, enabling effective slice-and-dice analysis across large datasets.

### Official Answer

Fact Tables: Use composite model with DirectQuery for current year (real-time) and Import for historical data (performance)
Dimension Tables: Import mode for product hierarchy (stable, enables proper relationships)
Incremental Refresh: Implement on historical fact tables with 2-year rolling window
Aggregations: Create summary tables at category level for trending reports
Security: Implement RLS with audit table tracking using calculated columns storing USERNAME()
Partitioning: Partition large tables by region and time periods

### Scenario 2: Performance Optimization

A Power BI report takes 45+ seconds to load with the following characteristics:
15 visuals on one page
Multiple slicers with ALL values selected by default
Complex measures using SUMX and FILTER
Star schema with 8 dimension tables
Question: Identify the likely performance bottlenecks and provide optimization strategies.

Bottlenecks:
Too many visuals triggering simultaneous queries
Expensive SUMX/FILTER measures
Slicers loading all values upfront
Optimizations:
Page Design: Split into multiple pages or use bookmarks for different views
DAX Optimization: Replace SUMX/FILTER with CALCULATE and proper filter context
Slicer Settings: Disable "Show items with no data" and limit initial load
Measures: Create base measures and build upon them rather than complex nested calculations
Relationships: Verify proper relationships and avoid bidirectional filters unless necessary
Aggregations: Implement aggregation tables for common summarizations

### Scenario 3

You need to configure automatic page refresh for a DirectQuery report monitoring real-time manufacturing data. What are the key considerations and limitations?

Considerations:
    - *Refresh Interval*: Minimum 30 seconds for DirectQuery, balance between freshness and source system load
    - *Premium Capacity*: Required for refresh intervals under 30 minutes
    - *Data Source Performance*: Ensure source can handle frequent queries
    - *Visual Optimization*: Limit visuals per page to reduce query load
    - *Change Detection*: Configure change detection to only refresh when data actually changes

Limitations:
    - Not available in shared capacity for frequent intervals
    - Increases load on source systems
    - May impact other reports using same data source
    - Limited to specific visual types
    - Requires proper indexing on source tables

### Scenario 4

You're connecting to a SQL Server database with 20 million rows. The report needs to show current data but users complain about slow performance. Which combination provides the best balance of performance and data freshness?

    (A) Import mode with scheduled refresh every hour
    (B) DirectQuery mode with query reduction settings
    *(C)* Composite model with aggregation tables
    (D) Live connection with cached visuals

### Scenario 5

You're connecting Power BI to a SQL Server database using DirectQuery. The source table has 10 million rows and users need to filter by date ranges. What's the BEST approach to optimize query performance?

    (A) Create a Power BI calculated column for date filtering
    (B) Create a clustered index on the date column in SQL Server
    (C) Use Import mode instead of DirectQuery
    (D) Create a view in SQL Server with pre-filtered data

### Scenario 6

PL-300 Power BI Questions for Data Analyst Job Scenarios
Section 1: Business Requirements & Stakeholder Management
Question 1
Your marketing manager asks: "I need to see which campaigns drive the most revenue, but I also want to understand the customer journey from first click to purchase." What's your approach to gathering complete requirements?
    (A) Create a dashboard showing campaign revenue and add click tracking later
    *(B)* Schedule requirements meeting to understand KPIs, user personas, and decision-making process
    (C) Build a comprehensive report with all available marketing data
    (D) Ask IT to provide all marketing database tables

### Scenario 7

A finance director says your Power BI report shows different numbers than their Excel spreadsheet. How do you handle this situation?
    (A) Explain that Power BI is more accurate than Excel
    *(B)* Document data sources, calculations, and arrange validation meeting
    (C) Recreate their Excel formulas exactly in Power BI
    (D) Ask them to use Power BI instead of Excel

### Scenario 8

Your CEO wants a "single pane of glass" dashboard for the entire company. What's the biggest challenge you need to address first?

    (A) Technical integration of multiple data sources
    *(B)* Defining what metrics matter most to different stakeholders
    (C) Getting access to all company databases
    (D) Choosing the right visualizations

### Scenario 9

You're analyzing sales data and notice that Q3 revenue dropped 40% compared to Q2, but your colleagues haven't mentioned any business issues. What's your immediate next step?

    (A) Report the finding to management immediately
    *(B)* Investigate data quality issues and validate the calculation
    (C) Check if it's a seasonal pattern by looking at previous year
    (D) Create a detailed breakdown by product and region

## Senior Questions

### Question 1: Data Strategy & Business Impact (Business Analyst here vs. Data Scientist other questions)

Scenario: Your company's revenue has been flat for 6 months despite increased marketing spend. The CEO asks you to "figure out what's really happening and recommend a path forward."

How would you approach this comprehensive business analysis?

### Section 1: Data Governance Framework & Strategy Question 2: Establishing Data Governance

Scenario: Your organization has 500+ Power BI reports created by different departments with inconsistent metrics, no data lineage tracking, and conflicting business definitions. Design a comprehensive data governance framework.
How would you establish enterprise-wide data governance for Power BI?
