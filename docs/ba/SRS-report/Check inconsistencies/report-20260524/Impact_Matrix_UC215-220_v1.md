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

### 2.1 UC215-220 (Chuyển vốn ĐTRNN - Mẫu II.6) — v1.4

| #  | Tên File (Link) | Vị trí | Lỗi / Bất đồng bộ phát hiện | Current Text | Target Text | Trạng thái |
| -- | ----------------------------------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ---------------- |
| 65 | [UC215-220_ChuyenVonDTRNN.md](../../UC215-220/UC215-220_ChuyenVonDTRNN.md) | UC215-220.2 — Số văn bản (field 2) | **[CROSS_UC_CONFLICT]** CROSS-UC conflict: UC215-220 ghi "Tham chiếu: CMR_06" (không CMR_13), UC209-214 (cùng dòng NHNN) ghi "Tham chiếu: CMR_13" | "(SRS UC215-220.2: "Tham chiếu: CMR_06")" vs "(UC209-214.2: "Tham chiếu: CMR_13")" | [Phương án A: theo UC215-220 — giữ CMR_06, ghi rõ "Không áp dụng CMR_13"] / [Phương án B: theo UC209-214 — bổ sung CMR_13] | Need confirmation |
| 66 | [UC215-220_ChuyenVonDTRNN.md](../../UC215-220/UC215-220_ChuyenVonDTRNN.md) | UC215-220.2 — Field 3 (Yearpicker - Năm báo cáo) | **[CMR_WRONG_REF]** "Năm báo cáo" (Yearpicker) tham chiếu cả CMR_05 và CMR_06 (CMR_05 cho Numeric, CMR_06 cho Text) | "Tham chiếu: CMR_05, CMR_06" | Bỏ cả CMR_05 và CMR_06 — Yearpicker dùng CS_01 Mục 2 | Need to fix |
| 67 | [UC215-220_ChuyenVonDTRNN.md](../../UC215-220/UC215-220_ChuyenVonDTRNN.md) | UC215-220.2 — Numeric fields (13, 25) | **[CMR_REDUNDANT_REF]** Numeric tham chiếu cả CMR_05 và CMR_06 | "Tham chiếu: CMR_05, CMR_06" | Cân nhắc bỏ CMR_06 | Optional |
| 68 | [UC215-220_ChuyenVonDTRNN.md](../../UC215-220/UC215-220_ChuyenVonDTRNN.md) | UC215-220.2 — Numeric fields | **[NO_DEFECT]** Numeric 15+5 đã align | "Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số" | N/A | OK |
| 69 | [UC215-220_ChuyenVonDTRNN.md](../../UC215-220/UC215-220_ChuyenVonDTRNN.md) | UC215-220.2 — Textbox fields | **[NO_DEFECT]** Textbox max 255 | "Max 255 ký tự" | N/A | OK |
| 70 | [UC215-220_ChuyenVonDTRNN.md](../../UC215-220/UC215-220_ChuyenVonDTRNN.md) | UC215-220.2 — Đề xuất, kiến nghị (Textarea) | **[NO_DEFECT]** Textarea max 3000 | "Max 3000 ký tự" | N/A | OK |
| 71 | [UC215-220_ChuyenVonDTRNN.md](../../UC215-220/UC215-220_ChuyenVonDTRNN.md) | UC215-220.2 — Buttons (Lưu nháp, Nộp) | **[CMR_CONFLICT]** Buttons "Luôn Enabled" (SRS) không đúng CMR_03. SRS hiện: "Luôn Enabled". CMR_03 quy định: Lưu nháp chỉ Enabled khi Lưu nháp; Nộp chỉ Enabled khi Lưu nháp hoặc Yêu cầu chỉnh sửa (sau Edit+Save) | "Luôn Enabled" (SRS UC215-220.2) | CMR_03: Lưu nháp → chỉ Enabled khi Lưu nháp; Nộp → chỉ Enabled khi Lưu nháp hoặc Yêu cầu chỉnh sửa (sau khi Edit+Save) | Need confirmation |
| 72 | [UC215-220_ChuyenVonDTRNN.md](../../UC215-220/UC215-220_ChuyenVonDTRNN.md) | UC215-220.2 — CMR_18 Tab Navigation | **[NO_DEFECT]** CMR_18 đã tham chiếu | "Tab key / Shift+Tab" | N/A | OK |
| 73 | [UC215-220_ChuyenVonDTRNN.md](../../UC215-220/UC215-220_ChuyenVonDTRNN.md) | UC215-220.1 — Search bar (Field 4) | **[NO_DEFECT]** Placeholder "Tìm kiếm nhanh theo mã báo cáo" | "Tìm kiếm nhanh theo mã báo cáo" | N/A | OK |

---

## 3. Tổng hợp

| Loại Issue | Số lượng |
|---|---|
| CMR_13_INCONSISTENCY | 1 |
| CMR_WRONG_REF | 1 |
| CMR_REDUNDANT_REF | 1 |
| CMR_CONFLICT | 1 |
| NO_DEFECT (OK) | 5 |
| **Tổng cần xử lý** | **4** |
| **Tổng OK** | **5** |

---

## 4. Priority Actions

### P1 - Need to fix:
1. **UC215-220 L103 (Field 3 Yearpicker):** Bỏ cả CMR_05 và CMR_06 — Yearpicker dùng CS_01 Mục 2
2. **UC215-220.2 Buttons:** Sửa "Luôn Enabled" → theo CMR_03: Lưu nháp chỉ Enabled khi Lưu nháp; Nộp chỉ Enabled khi Lưu nháp hoặc Yêu cầu chỉnh sửa (sau khi Edit+Save)

### P2 - Cần BA xác nhận:
2. **UC215-220 Số văn bản:** CMR_13 inconsistency — mâu thuẫn với UC209-214

### P3 - Optional cleanup:
3. **UC215-220 Numeric fields:** Có thể bỏ CMR_06 trong tham chiếu Numeric (CMR_05 đã đủ)

---

## N. CMR v3.7 Key Rules Reference

| CMR | Rule chính | Ảnh hưởng |
|-----|-----------|-----------|
| CMR_05 | Numeric: max 15 nguyên + 5 thập phân = 21 tổng | Decimal fields phải tham chiếu |
| CMR_06 | Text: max 255, Textarea: max 3000, Search: max 255 | Text fields phải có placeholder/error messages |
| CMR_07 | Dropdown: placeholder "Chọn [tên trường]" | Form dropdowns phải tham chiếu |
| CMR_13 | Số công văn: format, max 50 ký tự | Fields "Số văn bản" |
| CMR_16 | Filter dropdown phải có option "Tất cả" | Filter dropdowns |
| CMR_18 | Tab Navigation | Form navigation |
| CS_01 Mục 2 | Yearpicker là date picker, không phải numeric | Yearpicker KHÔNG reference CMR_05 hoặc CMR_06 |

---

*Document generated by Global Impact Analyzer*