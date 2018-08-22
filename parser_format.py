def excel_formatting(workbook, worksheet, cond="rune"):
    """
    Get excel formatting for displaying output
    :param workbook:
    :type workbook:
    :param worksheet:
    :type worksheet:
    :return:
    :rtype:
    """
    if cond == "rune":
        format_legend = workbook.add_format({'bg_color': '#f9e7a9', 'font_color': '#2B2925'})
        format_hero = workbook.add_format({'bg_color': '#f4d9f9', 'font_color': '#2B2925'})
        format_rare = workbook.add_format({'bg_color': '#d5f0f2', 'font_color': '#2B2925'})
        format_flat = workbook.add_format({'bg_color': '#dfdee2', 'font_color': '#0d0133'})
        format_del_candidate = workbook.add_format({'bg_color': '#6d5f5c', 'font_color': '#ffd2c9'})
        format_header = workbook.add_format({'bg_color': '#30305e', 'font_color': '#FFFFFF', 'valign': 'vcenter', 'align': 'center', 'bold': True})

        format_center = workbook.add_format({'valign': 'vcenter', 'align': 'center'})

        worksheet.conditional_format('D1:E1600', {'type': 'text',
                                                  'criteria': 'containing',
                                                  'value': 'L',
                                                  'format': format_legend})
        worksheet.conditional_format('D1:E1600', {'type': 'text',
                                                  'criteria': 'containing',
                                                  'value': 'H',
                                                  'format': format_hero})
        worksheet.conditional_format('D2:E1600', {'type': 'text',
                                                  'criteria': 'containing',
                                                  'value': 'R',
                                                  'format': format_rare})
        worksheet.conditional_format('L1:L1600', {'type': 'bottom',
                                                  'criteria': '%',
                                                  'value': '20',
                                                  'format': format_del_candidate})
        worksheet.conditional_format('N1:N1600', {'type': 'bottom',
                                                  'criteria': '%',
                                                  'value': '20',
                                                  'format': format_del_candidate})
        worksheet.conditional_format('J1:J1600', {'type': 'text',
                                                  'criteria': 'containing',
                                                  'value': 'flat',
                                                  'format': format_flat})
        worksheet.conditional_format('G1:G1600', {'type': '3_color_scale'})

        worksheet.set_column('A:G', None, format_center)
        worksheet.set_column('K:M', None, format_center)
        worksheet.set_column('A:A', 4)
        worksheet.set_column('B:B', 9)
        worksheet.set_column('C:C', 4)
        worksheet.set_column('D:D', 3.2)
        worksheet.set_column('E:E', 3.2)
        worksheet.set_column('F:F', 3.33)
        worksheet.set_column('G:G', 3.33)
        worksheet.set_column('H:H', 14.6)
        worksheet.set_column('I:I', 12)
        worksheet.set_column('J:J', 45)
        worksheet.set_column('K:K', 6.2)
        worksheet.set_column('L:L', 6.2)
        worksheet.set_column('M:M', 6.2)
        worksheet.set_column('N:N', 6.2)
        worksheet.set_column('O:O', 9)

        worksheet.autofilter('A1:O1600')
        worksheet.set_row(0, None, format_header)
        worksheet.freeze_panes(1, 0)

    elif cond == "mons":

        format_center = workbook.add_format({'valign': 'vcenter', 'align': 'center'})
        format_header = workbook.add_format({'bg_color': '#30305e', 'font_color': '#FFFFFF', 'valign': 'vcenter', 'align': 'center', 'bold': True})

        worksheet.set_column('A:D', None, format_center)
        worksheet.set_column('A:A', 4)
        worksheet.set_column('B:B', 13)
        worksheet.set_column('C:C', 13.2)
        worksheet.set_column('D:D', 13.2)

        worksheet.set_row(0, None, format_header)
        worksheet.freeze_panes(1, 0)
