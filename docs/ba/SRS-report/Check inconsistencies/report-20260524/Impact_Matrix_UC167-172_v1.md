# Impact Matrix - CMR v3.7 vs UC Documents (UC161-220)
## Ngày tạo: 2026-05-24
## Agent: BA-skills/Global-Impact-Analyzer

---

## 1. Tổng quan phân tích

**CMR v3.7 các thay đổi chính cần chú ý:**
- **CMR_05 (Numeric):** Max 15 chữ số nguyên + 5 chữ số thập phân = 21 tổng cộng. **Chỉ áp dụng cho trường Numeric — KHÔNG áp dụng cho Date Picker / Yearpicker.**
- **CMR_06 (Text/Search):** Max 255 ký tự (text thường), 3000 ký tự (textarea); placeholder chuẩn "Nhập [tên trường]". **Chỉ áp dụng cho Textbox / Textarea / Search box — KHÔNG áp dụng cho Date Picker / Yearpicker / Numeric.**
- **CMR_07 (Dropdown):** Single/Multi/Searchable dropdown — KHÔNG áp dụng cho Yearpicker (nên dùng CS_01 Mục 2).
- **CMR_11 (Tooltip):** Chỉ áp dụng khi field thực sự có Tooltip / Information icon (ℹ️).
- **CMR_13 (Số công văn):** Format `[Số/][Ký hiệu1]-[Ký hiệu2]`, max 50 ký tự, auto-uppercase, block ký tự không hợp lệ.
- **CMR_16 (Filter):** Filter dropdown phải có option "Tất cả" đầu danh sách.
- **CMR_19 (Trường Mã):** max 50 ký tự, không khoảng trắng, không ký tự có dấu.

---

## 2. Chi tiết Impact

### 2.1 UC167-172 (Thông báo ĐTRNN - Mẫu I.10) — v1.4

| #  | Tên File (Link) | Vị trí | Lỗi / Bất đồng bộ phát hiện | Current Text | Target Text | Trạng thái |
| -- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ---------------- |
| 8  | [UC167-172_ThongBaoDTRNN.md](../../UC167-172/UC167-172_ThongBaoDTRNN.md) | UC167-172.1 — Filter Trạng thái kỳ hạn | **[NO_DEFECT]** CMR_16 đã có | "Tham chiếu: CMR_04, CMR_07, CMR_16" | N/A | OK |
| 9  | [UC167-172_ThongBaoDTRNN.md](../../UC167-172/UC167-172_ThongBaoDTRNN.md) | UC167-172.2 — Field 9 (Số văn bản chấp thuận) | **[CMR_13_INCONSISTENCY]** "Số văn bản chấp thuận" chỉ tham chiếu CMR_06, không CMR_13 — cần BA quyết định | "Tham chiếu: CMR_06" | Hoặc bổ sung CMR_13, hoặc giữ nguyên + ghi rõ "Không áp dụng CMR_13" (như UC203-208) | Need confirmation |
| 10 | [UC167-172_ThongBaoDTRNN.md](../../UC167-172/UC167-172_ThongBaoDTRNN.md) | UC167-172.2 — Field 5, 10 (Datepicker) | **[CMR_WRONG_REF]** Date Picker tham chiếu CMR_06 (CMR_06 chỉ cho Textbox/Textarea/Search) | "Tham chiếu: CMR_06, CMR_12" / "Tham chiếu: CMR_06" | Bỏ CMR_06 cho Date Picker — Date Picker có rule riêng (chưa định nghĩa trong CMR, có thể inline UC) | Need confirmation |
| 11 | [UC167-172_ThongBaoDTRNN.md](../../UC167-172/UC167-172_ThongBaoDTRNN.md) | UC167-172.2 — Field 15 (MonthYearPicker) | **[CMR_WRONG_REF]** MonthYearPicker tham chiếu CMR_06 | "Tham chiếu: CMR_06" | Bỏ CMR_06 — cần rule riêng cho MonthYearPicker | Need confirmation |
| 12 | [UC167-172_ThongBaoDTRNN.md](../../UC167-172/UC167-172_ThongBaoDTRNN.md) | UC167-172.2 — Field 17 (Nút Hủy) | **[CMR_REDUNDANT_REF]** Nút Hủy tham chiếu CMR_17 (Upload File) — không phù hợp | "Tham chiếu: CF_01, CMR_18, CMR_17" | Bỏ CMR_17 khỏi nút Hủy (CMR_17 chỉ cho vùng upload, không cho nút thao tác) | Need to fix |
| 13 | [UC167-172_ThongBaoDTRNN.md](../../UC167-172/UC167-172_ThongBaoDTRNN.md) | UC167-172.2 — Field 13 (Số tài khoản vốn ĐTRNN) | **[NO_DEFECT]** Textbox max 255 | "Max 255 ký tự" | N/A | OK |
| 14 | [UC167-172_ThongBaoDTRNN.md](../../UC167-172/UC167-172_ThongBaoDTRNN.md) | UC167-172.2 — Field 12 (Địa chỉ trụ sở) | **[NO_DEFECT]** Textarea max 3000 | "Max 3000 ký tự" | N/A | OK |
| 15 | [UC167-172_ThongBaoDTRNN.md](../../UC167-172/UC167-172_ThongBaoDTRNN.md) | UC167-172.1 — Search bar (Field 5) | **[NO_DEFECT]** Placeholder "Tìm kiếm nhanh theo mã báo cáo" | "Tìm kiếm nhanh theo mã báo cáo" | N/A | OK |

---

## 3. Tổng hợp

| Loại Issue | Số lượng |
|---|---|
| CMR_13_INCONSISTENCY | 1 |
| CMR_WRONG_REF | 2 |
| CMR_REDUNDANT_REF | 1 |
| NO_DEFECT (OK) | 4 |
| **Tổng cần xử lý** | **4** |
| **Tổng OK** | **4** |

---

## 4. Priority Actions

### P1 - Need to fix:
1. **UC167-172 L156 (Nút Hủy):** Bỏ CMR_17 (không liên quan upload)

### P2 - Cần BA xác nhận (mâu thuẫn cross-UC / chính sách CMR_13):
2. **UC167-172 Field 9 "Số văn bản chấp thuận":** CMR_13 inconsistency — cần quyết định có áp dụng CMR_13 hay không
3. **UC167-172 Date Picker / MonthYearPicker fields:** Bổ sung rule chuẩn hoặc inline UC

---

## N. CMR v3.7 Key Rules Reference

| CMR | Rule chính | Ảnh hưởng |
|-----|-----------|-----------|
| CMR_05 | Numeric: max 15 nguyên + 5 thập phân = 21 tổng | Decimal fields phải tham chiếu |
| CMR_06 | Text: max 255, Textarea: max 3000, Search: max 255 | Text fields phải có placeholder/error messages |
| CMR_07 | Dropdown: placeholder "Chọn [tên trường]" | Form dropdowns phải tham chiếu |
| CMR_16 | Filter dropdown phải có option "Tất cả" | Filter dropdowns |
| CMR_19 | Trường Mã: max 50 ký tự, không khoảng trắng, không ký tự có dấu | Trường "Mã..." |
| CS_01 Mục 2 | Yearpicker là date picker, không phải numeric | Yearpicker KHÔNG reference CMR_05 |

---

*Document generated by Global Impact Analyzer*