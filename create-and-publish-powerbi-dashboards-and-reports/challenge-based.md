# Challenge: Create and Publish Power BI Dashboards & Reports (Dashboard-in-a-Day)

**Estimated Time:** 4 Hours  

**Industry Focus:** Cross-Industry (Business Intelligence)

## Problem Statement
Teams struggle to turn data into clear, executive-ready insights; reports lack consistent branding, storytelling flow, and actionable dashboards; publishing/sharing is inconsistent, and features like Q&A/Insights and drill-through are underused.

In this challenge, you will enhance a pre-built Power BI report with conditional formatting, branding, custom visuals, mobile layout, selection panes, and bookmarks; publish to Power BI Service, organize in a workspace, and construct an executive dashboard by pinning key visuals, applying filters, using Q&A/Quick Insights, and (optionally) setting alerts.

## Goals
By the end of this challenge, you will deliver an **executive-ready dashboard and a published report in Power BI Service with consistent branding, interactive storytelling (bookmarks/drill-through), Q&A visuals, and organized tiles ready for sharing and stakeholder review** including:

- Set up and sign in to Power BI Desktop & Service
- Apply conditional formatting, themes, logos, and custom visuals
- Configure mobile layout and selection panes
- Create bookmarks and drill-through
- Publish to a workspace and manage content
- Build/organize a dashboard with pinned visuals, Q&A, Quick Insights, and optional alerts

## Prerequisites
- **Skill Level:** Basic Power BI knowledge, understanding of report design principles
- **Audience:** Business analysts, data professionals, operations leads, decision makers
- **Technology Stack:** Power BI Desktop, Power BI Service, Power Platform tools

## Datasets
Use the following sample datasets provided in lab files:

- **Pre-built Power BI Report:** VanArsdel manufacturing sales data with multiple visualizations
- **Corporate Assets:** Company logos and branding elements for consistent visual identity
- **Sample Data:** Revenue, market share, and performance metrics across multiple regions

Ensure all datasets are stored in your local directory: `C:\DIAD\DIADL4\`

| File Path | Description |
|-----------|-------------|
| `C:\DIAD\DIADL4\Reports\DIAD Final Report.pbix` | Pre-built Power BI report template |
| `C:\DIAD\DIADL4\Data\VanArsdel_WSLogo` | Corporate logo for branding |
| Sample data includes revenue, market share, and manufacturing performance metrics |


## Challenge Objectives

### **Challenge 1: Foundation - Power BI Setup and Report Enhancement**
**Estimated Duration:** 90 Minutes

#### Objective
Establish Power BI environment and enhance pre-built report with professional branding, formatting, and mobile optimization.

#### Tasks
1. **Configure Power BI Environment:**
   - Set up Power BI Desktop and Service accounts with proper authentication
   - Enable advanced visual features including Map and Filled Map visuals
   - Configure security settings and data source permissions
   - Verify connectivity between Power BI Desktop and Service

2. **Enhance Report Design and Branding:**
   - Open pre-built VanArsdel report (`DIAD Final Report.pbix`) in Power BI Desktop
   - Apply conditional formatting to highlight key performance indicators and trends
   - Import and configure corporate logos and branding elements for consistent visual identity
   - Implement custom themes and color schemes aligned with corporate standards
   - Add custom visuals from Power BI marketplace to enhance data storytelling

3. **Optimize for Mobile and Accessibility:**
   - Configure mobile layout with optimized visual positioning and sizing
   - Enable Selection pane for better report navigation and visual management
   - Configure gridlines and snap-to-grid settings for precise visual alignment
   - Test mobile responsiveness and adjust layouts for different screen sizes

4. **Prepare for Publication:**
   - Create Power BI Service workspace with appropriate naming convention (`DIAD_<uniqueID>`)
   - Upload corporate branding assets to workspace for consistent theming
   - Validate report functionality and visual consistency before publication
   - Configure workspace permissions and access controls

#### Validation Check
- Power BI Desktop and Service are properly configured with all necessary features enabled
- Pre-built report is enhanced with conditional formatting, branding, and custom visuals
- Mobile layout is optimized and responsive across different device sizes
- Power BI Service workspace is created and ready for content publication

### **Challenge 2: Publication & Interactive Storytelling - Deploy and Enhance Report**
**Estimated Duration:** 75 Minutes

#### Objective
Publish enhanced report to Power BI Service and implement advanced interactive features including bookmarks and drill-through capabilities.

#### Tasks
1. **Publish Report to Power BI Service:**
   - Publish enhanced report from Power BI Desktop to designated workspace
   - Verify successful publication and data source connectivity
   - Configure data refresh schedules and gateway settings if required
   - Test report functionality in Power BI Service environment

2. **Implement Interactive Storytelling Features:**
   - **Create Bookmarks:** Design narrative flow with bookmarks for guided data exploration
   - **Configure Drill-Through:** Set up drill-through pages for detailed analysis (e.g., country → state → city)
   - **Enable Cross-Filtering:** Configure visual interactions for dynamic data exploration
   - **Add Navigation Elements:** Implement buttons and navigation aids for user-friendly experience

3. **Build Executive Dashboard:**
   - Create new dashboard (`VanArsdel Executive Dashboard`) in Power BI Service
   - Pin key performance visuals including:
     - **Market Share Analysis:** VanArsdel market position and competitive landscape
     - **Growth Metrics:** Percentage growth by manufacturer and time periods
     - **Revenue Analytics:** Revenue trends by year, manufacturer, and geographic region
     - **Performance Gauges:** Revenue vs. prior year sales with target indicators
     - **Geographic Insights:** Revenue distribution by country and region

4. **Optimize Dashboard User Experience:**
   - Apply consistent theming across all pinned visuals ("Use destination theme")
   - Configure interactive filters and slicers for dynamic data exploration
   - Test drill-down functionality in map visuals (country → state level analysis)
   - Validate that all visuals respond correctly to filter selections

#### Validation Check
- Report is successfully published to Power BI Service with all features functional
- Bookmarks and drill-through navigation work seamlessly for interactive storytelling
- Executive dashboard contains all key visuals with consistent branding and theming
- Interactive features including filters, drill-down, and cross-filtering operate correctly

### **Challenge 3: Advanced Analytics & Collaboration - Q&A, Insights, and Dashboard Organization**
**Estimated Duration:** 75 Minutes

#### Objective
Implement advanced Power BI features including Q&A natural language queries, AI-powered insights, and comprehensive dashboard organization for executive stakeholder consumption.

#### Tasks
1. **Organize and Optimize Dashboard Layout:**
   - Resize and reposition tiles for optimal executive dashboard viewing experience
   - Add corporate branding elements including logos and custom imagery
   - Rename visuals and tiles with clear, business-friendly labels (e.g., "VanArsdel Revenue Performance")
   - Configure tile grouping and logical flow for intuitive dashboard navigation

2. **Implement Natural Language Analytics (Q&A):**
   - **Enable Q&A Visual:** Add Q&A tile to dashboard for natural language data exploration
   - **Test Query Scenarios:** Execute business-relevant queries such as:
     - "VanArsdel market share by country"
     - "Revenue trends over the last 3 years"
     - "Top performing manufacturers by growth rate"
   - **Pin Generated Visuals:** Save valuable Q&A insights as permanent dashboard tiles
   - **Configure Q&A Settings:** Optimize natural language understanding and synonyms

3. **Leverage AI-Powered Quick Insights:**
   - **Generate Automatic Insights:** Use Quick Insights feature to discover hidden patterns
   - **Explore Insight Categories:** Analyze trends, correlations, and anomalies identified by AI
   - **Pin Valuable Insights:** Add relevant AI-generated visuals to executive dashboard
   - **Validate Insight Accuracy:** Review and contextualize AI findings for business relevance

4. **Configure Advanced Features and Collaboration:**
   - **Set Data Alerts:** Configure threshold-based alerts for key performance metrics (optional)
   - **Test Drill-Through Functionality:** Validate detailed exploration paths (e.g., Australia → By Manufacturer)
   - **Bookmark Navigation:** Demonstrate storytelling flow using configured bookmarks
   - **Mobile Optimization:** Verify dashboard responsiveness on mobile devices
   - **Sharing and Permissions:** Configure workspace sharing for stakeholder collaboration

5. **Final Dashboard Validation and Testing:**
   - Test all interactive features including filters, drill-down, and cross-filtering
   - Validate Q&A functionality with various business questions and scenarios
   - Confirm Quick Insights generate relevant and actionable business intelligence
   - Verify dashboard loading performance and visual rendering quality

#### Validation Check
- Dashboard is professionally organized with intuitive layout and clear labeling
- Q&A functionality works effectively with natural language business queries
- Quick Insights generate valuable AI-powered analytics and actionable recommendations
- All advanced features (alerts, drill-through, bookmarks) function correctly
- Dashboard is optimized for executive consumption with appropriate sharing permissions

## Success Criteria
**You will have successfully completed this challenge when you deliver:**

An **executive-ready dashboard and a published report in Power BI Service with consistent branding, interactive storytelling (bookmarks/drill-through), Q&A visuals, and organized tiles ready for sharing and stakeholder review**.

### **Technical Deliverables:**
- **Enhanced Report:** Professional report with conditional formatting, custom visuals, and corporate branding
- **Mobile Optimization:** Responsive design configured for mobile and tablet viewing experiences
- **Interactive Features:** Bookmarks, drill-through, and cross-filtering implemented for guided storytelling
- **Executive Dashboard:** Organized dashboard with key performance visuals and intuitive layout
- **Natural Language Analytics:** Q&A functionality working with business-relevant queries
- **AI-Powered Insights:** Quick Insights generating valuable analytical recommendations
- **Collaboration Ready:** Published workspace with appropriate sharing permissions and access controls

### **Business Outcomes:**
- **Executive Communication:** Clear, branded reports ready for C-level stakeholder presentation
- **Self-Service Analytics:** Q&A enables business users to explore data independently
- **Mobile Accessibility:** Dashboard accessible and functional across all device types
- **Automated Intelligence:** Quick Insights surface hidden patterns and business opportunities

## Additional Resources
- [Power BI Documentation](https://learn.microsoft.com/power-bi/)
- [Power BI Learning Path](https://learn.microsoft.com/training/powerbi/)
- [Power BI Community](https://community.powerbi.com/)
- [Power BI Best Practices](https://learn.microsoft.com/power-bi/guidance/)
- [Power Platform Tools](https://learn.microsoft.com/power-platform/)

## Conclusion
By completing this challenge, you will have built an **executive-ready Power BI solution** with professional branding and advanced analytics features.

You learned how to:
- Transform basic reports into executive-ready dashboards with consistent branding and mobile optimization
- Implement interactive storytelling using bookmarks, drill-through, and advanced navigation features
- Leverage AI-powered features including Q&A natural language queries and Quick Insights
- Configure Power BI Service workspaces for enterprise collaboration and content management

This solution demonstrates how Power BI enables **data-driven decision making** through intuitive, self-service analytics accessible to business stakeholders at all levels.