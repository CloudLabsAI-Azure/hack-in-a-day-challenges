# Challenge: Create and Publish Power BI Dashboards & Reports using Power BI Desktop and Power BI Service

**Estimated Time:** 4 Hours

## Problem Statement
In this challenge, you will learn how to create and publish Power BI dashboards and reports using a pre-built report. You will enhance the report by applying conditional formatting, adding logos, importing custom visuals, and using bookmarks to tell a data story. You will then publish the report to Power BI Service and construct a dashboard by pinning key visuals to effectively visualize and present data.  

This lab provides hands-on experience with Power BI features to improve report presentation, dashboard organization, and analytical storytelling.

---

## Goals
- Customize and enhance a pre-built Power BI report.
- Apply conditional formatting, custom visuals, and themes.
- Build and organize a Power BI dashboard.
- Utilize features like bookmarks, drill-through, and quick insights.
- Publish and share reports in Power BI Service.

---

## Pre-requisites
- Basic knowledge of Power BI.
- Access to Power BI Desktop and Power BI Service.
- Understanding of report design principles.

---

## Architecture
The workflow for this challenge involves:
1. Starting with a pre-built Power BI report.
2. Applying conditional formatting to highlight key data points.
3. Adding logos, filters, and custom visuals.
4. Applying a custom theme for design consistency.
5. Using bookmarks to enhance storytelling.
6. Publishing the report to Power BI Service.
7. Pinning key visuals to construct an interactive dashboard.

---

## Challenge Objectives

### **Task 1: Power BI Service – Publishing Report**
1. Open File Explorer in the Lab VM and navigate to `C:\DIAD\DIADL4\Reports`.
2. Open the `DIAD Final Report.pbix` file in Power BI Desktop.
3. Close any pop-ups if they appear.
4. Enable Map and Filled Map visuals:
   - File → Options and settings → Options → Security → Check `Use Map and Filled Map visuals`.
5. Adjust the mobile layout:
   - View → Mobile layout → Move visuals to top of canvas as needed.
6. Enable Selection pane and turn off Gridlines and Snap to Grid.
7. Save the workbook.
8. In the browser, navigate to Power BI Service → Workspaces → + New Workspace → Create workspace named `DIAD_`.
9. Upload `VanArsdel_WSLogo` from `C:\DIAD\DIADL4\Data` to workspace.
10. Publish the report:
    - Home → Publish → Select `DIAD_` workspace → Wait for success message.

---

### **Task 2: Power BI – Building a Dashboard**
1. Open the published `DIAD Final Report` in Power BI Service.
2. Enable drill-down in map visual, drill to State level (e.g., Australia).
3. Pin visuals to a new dashboard `VanArsdel`:
   - VanArsdel Market Share
   - % Growth by Manufacturer
   - Revenue by Year and Manufacturer
   - Revenue and PY Sales (gauge)
   - Revenue by Country
4. Ensure “Use destination theme” is selected when pinning visuals.
5. Apply filters using slicers and ensure visuals reflect the filtered data.

---

### **Task 3: Organize Dashboard**
1. Resize and move tiles as required.
2. Add new tiles:
   - Edit → + Add a tile → Image → Add URL `https://raw.githubusercontent.com/CharlesSterling/DiadManu/master/Vanarsdel.png`.
3. Rename visuals and tiles for clarity (e.g., `VanArsdel Revenue`).
4. Use Q&A to create visuals:
   - Ask natural language questions like `VanArsdel market share by country` → Pin generated visuals.
5. Explore insights:
   - Hover over a visual → ellipsis → View Insights → Pin to dashboard if needed.
6. Set alerts (optional) for thresholds on key metrics.
7. Use Drill-through for detailed exploration (e.g., Australia → By Manufacturer).
8. Use Bookmarks:
   - View bookmarks → Navigate through report bookmarks to explore storytelling.
9. Quick insights:
   - Select report → ellipsis → Quick insights → View insights → Pin visuals if required.

---

## Validation Check
1. Verify all visuals are pinned to the `VanArsdel` dashboard.
2. Check filters and drill-through options work as expected.
3. Ensure all Q&A visuals are correctly generated.
4. Confirm that the report is visible and accessible in the Power BI Service workspace.

---

## Success Criteria
- Report is enhanced with conditional formatting, custom visuals, and logos.
- Dashboard is created with pinned visuals and organized tiles.
- Bookmarks, drill-through, and Q&A functionalities are working.
- Report is successfully published to Power BI Service.
- Insights and alerts are configured correctly (optional).

---

## Additional Resources
- [Power BI Documentation | Microsoft Learn](https://learn.microsoft.com/power-bi/)
- [Power BI Courses | Microsoft Learn](https://learn.microsoft.com/training/powerbi)
- [Power BI Support](https://support.microsoft.com/power-bi)
- [Power Platform Tools](https://learn.microsoft.com/power-platform/)

---

## Conclusion
In this challenge, you have successfully:
- Customized a Power BI report with conditional formatting, logos, and themes.
- Published the report to Power BI Service.
- Created a dashboard with pinned visuals, organized tiles, and interactive elements.
- Explored bookmarks, drill-through, Q&A, and insights features to enhance storytelling and analysis.
 
