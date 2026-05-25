# Impact Matrix - CMR v3.7 vs UC Documents
## Ngày tạo: 2026-05-24
## Agent: BA-skills/Global-Impact-Analyzer

---

## 1. Tổng quan phân tích

**CMR v3.7 các thay đổi chính cần chú ý:**
- **CMR_05 (Numeric):** Max 15 chữ số nguyên + 5 chữ số thập phân = 21 tổng cộng
- **CMR_06 (Text/Search):** Max 255 ký tự (text thường), 3000 ký tự (textarea); placeholder chuẩn "Nhập [tên trường]"
- **CMR_07 (Dropdown):** Phải có option "Tất cả" đầu danh sách
- **CMR_13 (Số công văn):** Format validation mới
- **CMR_19 (Trường Mã):** Quy tắc mới về mã

---

## 2. Chi tiết Impact

### 2.1 UC089-094 (Cấp mới GCNĐKĐT) - v1.7

| # | Tên File (Link) | Vị trí | Lỗi / Bất đồng bộ phát hiện | Current Text | Target Text | Trạng thái |
|---|---|---|---|---|---|---|
| 1 | [UC089-094_CapMoiGCNDKDT.md](../UC089-094/UC089-094_CapMoiGCNDKDT.md) | UC089-094.2, C2 (Mã số dự án/Số GCNĐT), row 118 | **[CMR_CONFLICT]** C2 max 255 + thiếu CMR_19 reference | "Tối đa 255 ký tự"; chỉ CMR_05 | Thống nhất "Tối đa 50 ký tự" + Thêm CMR_19 + Error maxlength | Need to fix |
| 2 | [UC089-094_CapMoiGCNDKDT.md](../UC089-094/UC089-094_CapMoiGCNDKDT.md) | UC089-094.2, C6 (Vốn pháp định), row 122 | **[CMR_CONFLICT]** C6 thừa CMR_08 (CMR_08 chỉ cho Kỳ hạn báo cáo display, không liên quan Decimal) | Tham chiếu CMR_08 (sai) | Bỏ CMR_08, chỉ tham chiếu CMR_05 | Need to fix |
| 3 | [UC089-094_CapMoiGCNDKDT.md](../UC089-094/UC089-094_CapMoiGCNDKDT.md) | UC089-094.2, C7 (Vốn góp Bên Việt Nam), row 123 | **[CMR_CONFLICT]** C7 thừa CMR_08 | Tham chiếu CMR_08 (sai) | Bỏ CMR_08, chỉ tham chiếu CMR_05 | Need to fix |
| 4 | [UC089-094_CapMoiGCNDKDT.md](../UC089-094/UC089-094_CapMoiGCNDKDT.md) | UC089-094.2, C8 (Vốn góp Tổng), row 124 | **[CMR_CONFLICT]** C8 thừa CMR_12 (Calculated field, không phải Decimal precision) | Tham chiếu CMR_12 (sai) | Tham chiếu CMR_05 (Decimal precision) | Need to fix |
| 5 | [UC089-094_CapMoiGCNDKDT.md](../UC089-094/UC089-094_CapMoiGCNDKDT.md) | UC089-094.2, T (Tổng cộng), row 137 | **[CMR_CONFLICT]** T thừa CMR_06 (Calculated Decimal, không phải Text) | Tham chiếu CMR_06 (sai) | Tham chiếu CMR_05 (Decimal precision) | Need to fix |
| 6 | [UC089-094_CapMoiGCNDKDT.md](../UC089-094/UC089-094_CapMoiGCNDKDT.md) | UC089-094.2, C3 (Ngày cấp), row 119 | **[CMR_CONFLICT]** C3 thừa CMR_08 (CMR_08 chỉ cho Kỳ hạn display, không liên quan Date) | Tham chiếu CMR_05, CMR_08 | Bỏ CMR_08, chỉ tham chiếu CMR_05 | Need to fix |
| 7 | [UC089-094_CapMoiGCNDKDT.md](../UC089-094/UC089-094_CapMoiGCNDKDT.md) | UC089-094.2, C5 (Vốn đầu tư đăng ký), row 121 | **[CMR_CONFLICT]** C5 thừa CMR_08 | Tham chiếu CMR_05, CMR_08 | Bỏ CMR_08, chỉ tham chiếu CMR_05 | Need to fix |
| 8 | [UC089-094_CapMoiGCNDKDT.md](../UC089-094/UC089-094_CapMoiGCNDKDT.md) | UC089-094.2, C15 (Nước đăng ký), row 131 | **[CMR_CONFLICT]** C15 thiếu CMR_07 (Dropdown placeholder) | Chỉ tham chiếu CMR_05 | Thêm CMR_07 (placeholder "Chọn [tên trường]") | Need to fix |
| 9 | [UC089-094_CapMoiGCNDKDT.md](../UC089-094/UC089-094_CapMoiGCNDKDT.md) | UC089-094.2, C4 (Tên dự án/doanh nghiệp), row 120 | **[INTRA_DOC_CONFLICT]** C4 thiếu error maxlength message | "Tối đa 255 ký tự" (không có error) | Thêm error maxlength message | Need to fix |
| 10 | [UC089-094_CapMoiGCNDKDT.md](../UC089-094/UC089-094_CapMoiGCNDKDT.md) | UC089-094.2, C11 (Thời hạn thực hiện dự án), row 127 | **[INTRA_DOC_CONFLICT]** C11 thiếu error maxlength message | "Tối đa 255 ký tự" (không có error) | Thêm error maxlength message | Need to fix |
| 11 | [UC089-094_CapMoiGCNDKDT.md](../UC089-094/UC089-094_CapMoiGCNDKDT.md) | UC089-094.2, C12 (Địa chỉ trụ sở DN), row 128 | **[INTRA_DOC_CONFLICT]** C12 thiếu error maxlength message | "Tối đa 255 ký tự" (không có error) | Thêm error maxlength message | Need to fix |
| 12 | [UC089-094_CapMoiGCNDKDT.md](../UC089-094/UC089-094_CapMoiGCNDKDT.md) | UC089-094.2, C13 (Nhà đầu tư NN - Tên), row 129 | **[INTRA_DOC_CONFLICT]** C13 thiếu error maxlength message | "Tối đa 255 ký tự" (không có error) | Thêm error maxlength message | Need to fix |
| 13 | [UC089-094_CapMoiGCNDKDT.md](../UC089-094/UC089-094_CapMoiGCNDKDT.md) | UC089-094.2, C14 (Nhà đầu tư NN - Địa chỉ), row 130 | **[INTRA_DOC_CONFLICT]** C14 thiếu error maxlength message | "Tối đa 255 ký tự" (không có error) | Thêm error maxlength message | Need to fix |

---

## 3. Tổng hợp

| Loại Issue | Số lượng |
|---|---|
| CMR_CONFLICT (sai/quá tham chiếu) | 8 |
| INTRA_DOC_CONFLICT | 5 |
| **Tổng cần xử lý** | **13** |

---

## 4. Priority Actions

### P1 - Need to fix (CMR v3.7 alignment):
1. **UC089-094 C2:** Mã số dự án/Số GCNĐT — đổi max 50 ký tự + thêm CMR_19 + error maxlength
2. **UC089-094 C3:** Ngày cấp — bỏ CMR_08 (sai), chỉ giữ CMR_05
3. **UC089-094 C5:** Vốn đầu tư đăng ký — bỏ CMR_08 (sai), chỉ giữ CMR_05
4. **UC089-094 C6:** Vốn pháp định — bỏ CMR_08 (sai), thêm CMR_05
5. **UC089-094 C7:** Vốn góp Bên Việt Nam — bỏ CMR_08 (sai), thêm CMR_05
6. **UC089-094 C8:** Vốn góp Tổng — bỏ CMR_12 (sai), thêm CMR_05
7. **UC089-094 C15:** Nước đăng ký — thêm CMR_07
8. **UC089-094 T:** Tổng cộng — bỏ CMR_06 (sai), thêm CMR_05
9. **UC089-094 C4, C11, C12, C13, C14:** Bổ sung error maxlength message

---

## N. CMR v3.7 Key Rules Reference

| CMR | Rule chính | Ảnh hưởng |
|-----|-----------|-----------|
| CMR_05 | Numeric: max 15 nguyên + 5 thập phân = 21 tổng | Decimal fields phải tham chiếu |
| CMR_06 | Text: max 255, Textarea: max 3000, Search: max 255 (block) | Text fields phải có error messages |
| CMR_07 | Dropdown phải có placeholder "Chọn [tên trường]" | Form dropdowns phải tham chiếu |
| CMR_16 | Filter dropdown phải có option "Tất cả" đầu danh sách | Filter dropdowns |
| CMR_19 | Trường Mã: max 50 ký tự, không khoảng trắng, không ký tự có dấu | Trường "Mã..." |

---

*Document generated by Global Impact Analyzer*