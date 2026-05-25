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

### 2.1 UC179-184 (Chấm dứt hoạt động ĐTRNN - Mẫu I.20) — v1.4

| #  | Tên File (Link) | Vị trí | Lỗi / Bất đồng bộ phát hiện | Current Text | Target Text | Trạng thái |
| -- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ---------------- |
| 24 | [UC179-184_ChamDutHoatDongDTRNN.md](../../UC179-184/UC179-184_ChamDutHoatDongDTRNN.md) | UC179-184.2 — Field 7 (Số văn bản chấp thuận chấm dứt) | **[CMR_13_INCONSISTENCY]** Field "Số văn bản" chỉ tham chiếu CMR_06, không CMR_13 — mâu thuẫn với UC209-214 | "Tham chiếu: CMR_06" | Hoặc bổ sung CMR_13, hoặc ghi rõ "Không áp dụng CMR_13" | Need confirmation |
| 25 | [UC179-184_ChamDutHoatDongDTRNN.md](../../UC179-184/UC179-184_ChamDutHoatDongDTRNN.md) | UC179-184.2 — Field 8 (Date Picker) | **[CMR_WRONG_REF]** "Văn bản chấp thuận — Ngày" (Date Picker) tham chiếu CMR_05 (CMR_05 cho Numeric) | "Tham chiếu: CMR_05" | Bỏ CMR_05 — Date Picker không phải Numeric | Need to fix |
| 26 | [UC179-184_ChamDutHoatDongDTRNN.md](../../UC179-184/UC179-184_ChamDutHoatDongDTRNN.md) | UC179-184.2 — Field 12 (Date Picker) | **[CMR_WRONG_REF]** "Ngày chấm dứt hoạt động" (Date Picker) tham chiếu CMR_05 | "Tham chiếu: CMR_05" | Bỏ CMR_05 — Date Picker không phải Numeric | Need to fix |
| 27 | [UC179-184_ChamDutHoatDongDTRNN.md](../../UC179-184/UC179-184_ChamDutHoatDongDTRNN.md) | UC179-184.2 — Field 9 (Numeric) | **[CMR_WRONG_REF + CMR_MISSING_REF]** "Vốn đầu tư ra nước ngoài (USD)" tham chiếu CMR_11 (Tooltip) nhưng KHÔNG có tooltip; cũng thiếu CMR_05 | "Tham chiếu: CMR_11" | Bỏ CMR_11, thêm CMR_05 (Numeric) — hoặc bổ sung tooltip để giữ CMR_11 | Need to fix |
| 28 | [UC179-184_ChamDutHoatDongDTRNN.md](../../UC179-184/UC179-184_ChamDutHoatDongDTRNN.md) | UC179-184.2 — Fields 10, 11 (Numeric với tooltip) | **[NO_DEFECT]** CMR_05 + CMR_11 (có tooltip) đúng | "Tham chiếu: CMR_05, CMR_11" | N/A | OK |
| 29 | [UC179-184_ChamDutHoatDongDTRNN.md](../../UC179-184/UC179-184_ChamDutHoatDongDTRNN.md) | UC179-184.2 — Field 13 (Lý do chấm dứt) | **[NO_DEFECT]** Textarea max 3000 | "Max 3000 ký tự" | N/A | OK |
| 30 | [UC179-184_ChamDutHoatDongDTRNN.md](../../UC179-184/UC179-184_ChamDutHoatDongDTRNN.md) | UC179-184.2 — Buttons | **[CMR_CONFLICT]** Buttons "Luôn Enabled" (SRS) không đúng CMR_03. SRS hiện: "Luôn Enabled". CMR_03 quy định: Lưu nháp chỉ Enabled khi Lưu nháp; Nộp chỉ Enabled khi Lưu nháp hoặc Yêu cầu chỉnh sửa (sau Edit+Save) | "Luôn Enabled" (SRS UC179-184.2) | CMR_03: Lưu nháp → chỉ Enabled khi Lưu nháp; Nộp → chỉ Enabled khi Lưu nháp hoặc Yêu cầu chỉnh sửa (sau khi Edit+Save) | Need confirmation |
| 31 | [UC179-184_ChamDutHoatDongDTRNN.md](../../UC179-184/UC179-184_ChamDutHoatDongDTRNN.md) | UC179-184.1 — Filter Trạng thái báo cáo, Dự án | **[NO_DEFECT]** CMR_16 đã có | "Tham chiếu: CMR_07, CMR_16" | N/A | OK |
| 32 | [UC179-184_ChamDutHoatDongDTRNN.md](../../UC179-184/UC179-184_ChamDutHoatDongDTRNN.md) | UC179-184.1 — Search bar (Field 4) | **[NO_DEFECT]** Placeholder "Tìm kiếm nhanh theo mã báo cáo" | "Tìm kiếm nhanh theo mã báo cáo" | N/A | OK |

---

## 3. Tổng hợp

| Loại Issue | Số lượng |
|---|---|
| CMR_13_INCONSISTENCY | 1 |
| CMR_WRONG_REF | 3 |
| NO_DEFECT (OK) | 5 |
| **Tổng cần xử lý** | **4** |
| **Tổng OK** | **5** |

---

## 4. Priority Actions

### P1 - Need to fix (Lỗi CMR refer SAI):
1. **UC179-184 L144 (Field 8 Date Picker):** Bỏ CMR_05
2. **UC179-184 L148 (Field 12 Date Picker):** Bỏ CMR_05
3. **UC179-184 L145 (Field 9 Numeric):** Bỏ CMR_11 (không có tooltip), thêm CMR_05

### P2 - Cần BA xác nhận:
4. **UC179-184 Field 7 "Số văn bản (Chấp thuận chấm dứt)":** CMR_13 inconsistency — cần quyết định chính sách

---

## N. CMR v3.7 Key Rules Reference

| CMR | Rule chính | Ảnh hưởng |
|-----|-----------|-----------|
| CMR_05 | Numeric: max 15 nguyên + 5 thập phân = 21 tổng | Decimal fields phải tham chiếu |
| CMR_06 | Text: max 255, Textarea: max 3000, Search: max 255 | Text fields phải có placeholder/error messages |
| CMR_07 | Dropdown: placeholder "Chọn [tên trường]" | Form dropdowns phải tham chiếu |
| CMR_11 | Tooltip: Chỉ áp dụng khi field thực sự có Tooltip icon (ℹ️) | Numeric fields có tooltip |
| CMR_16 | Filter dropdown phải có option "Tất cả" | Filter dropdowns |
| CMR_19 | Trường Mã: max 50 ký tự, không khoảng trắng, không ký tự có dấu | Trường "Mã..." |

---

*Document generated by Global Impact Analyzer*