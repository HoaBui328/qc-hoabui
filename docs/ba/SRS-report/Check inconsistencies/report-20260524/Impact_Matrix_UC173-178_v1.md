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

### 2.1 UC173-178 (Kéo dài thời hạn chuyển lợi nhuận - Mẫu I.11) — v1.3

| #  | Tên File (Link) | Vị trí | Lỗi / Bất đồng bộ phát hiện | Current Text | Target Text | Trạng thái |
| -- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ---------------- |
| 16 | [UC173-178_KeoThoiHanChuyenLoiNhuan.md](../../UC173-178/UC173-178_KeoThoiHanChuyenLoiNhuan.md) | UC173-178.2 — Field 7 (Date Picker) | **[CMR_WRONG_REF]** "Ngày có quyết định chia lợi nhuận" (Date Picker) tham chiếu CMR_05 (CMR_05 cho Numeric) | "Tham chiếu: CMR_05" | Bỏ CMR_05 — Date Picker không phải Numeric, cần inline rule | Need to fix |
| 17 | [UC173-178_KeoThoiHanChuyenLoiNhuan.md](../../UC173-178/UC173-178_KeoThoiHanChuyenLoiNhuan.md) | UC173-178.2 — Field 16 (Date Picker) | **[CMR_WRONG_REF]** "Hạn chuyển tiền mới" (Date Picker) tham chiếu CMR_05 | "Tham chiếu: CMR_05, CMR_11" | Bỏ CMR_05 — giữ CMR_11 (có tooltip) | Need to fix |
| 18 | [UC173-178_KeoThoiHanChuyenLoiNhuan.md](../../UC173-178/UC173-178_KeoThoiHanChuyenLoiNhuan.md) | UC173-178.2 — Fields 14, 15 (Numeric với Tooltip) | **[NO_DEFECT]** CMR_05 + CMR_11 (có tooltip) đúng | "Tham chiếu: CMR_05, CMR_11" | N/A | OK |
| 19 | [UC173-178_KeoThoiHanChuyenLoiNhuan.md](../../UC173-178/UC173-178_KeoThoiHanChuyenLoiNhuan.md) | UC173-178.2 — Fields 8, 9, 11, 12 | **[NO_DEFECT]** Numeric 15+5 đã align | "Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số" | N/A | OK |
| 20 | [UC173-178_KeoThoiHanChuyenLoiNhuan.md](../../UC173-178/UC173-178_KeoThoiHanChuyenLoiNhuan.md) | UC173-178.2 — Field 17 (Lý do kéo dài) | **[NO_DEFECT]** Textarea max 3000 | "Max 3000 ký tự" | N/A | OK |
| 21 | [UC173-178_KeoThoiHanChuyenLoiNhuan.md](../../UC173-178/UC173-178_KeoThoiHanChuyenLoiNhuan.md) | UC173-178.2 — Buttons | **[CMR_CONFLICT]** Buttons "Luôn Enabled" (SRS) không đúng CMR_03. SRS hiện: "Luôn Enabled". CMR_03 quy định: Lưu nháp chỉ Enabled khi Lưu nháp; Nộp chỉ Enabled khi Lưu nháp hoặc Yêu cầu chỉnh sửa (sau Edit+Save) | "Luôn Enabled" (SRS UC173-178.2) | CMR_03: Lưu nháp → chỉ Enabled khi Lưu nháp; Nộp → chỉ Enabled khi Lưu nháp hoặc Yêu cầu chỉnh sửa (sau khi Edit+Save) | Need confirmation |
| 22 | [UC173-178_KeoThoiHanChuyenLoiNhuan.md](../../UC173-178/UC173-178_KeoThoiHanChuyenLoiNhuan.md) | UC173-178.1 — Filter Dự án, Trạng thái | **[NO_DEFECT]** CMR_16 đã có | "Tham chiếu: CMR_07, CMR_16" | N/A | OK |
| 23 | [UC173-178_KeoThoiHanChuyenLoiNhuan.md](../../UC173-178/UC173-178_KeoThoiHanChuyenLoiNhuan.md) | UC173-178.1 — Search bar (Field 4) | **[NO_DEFECT]** Placeholder "Tìm kiếm nhanh theo mã báo cáo" | "Tìm kiếm nhanh theo mã báo cáo" | N/A | OK |

---

## 3. Tổng hợp

| Loại Issue | Số lượng |
|---|---|
| CMR_WRONG_REF | 2 |
| NO_DEFECT (OK) | 6 |
| **Tổng cần xử lý** | **2** |
| **Tổng OK** | **6** |

---

## 4. Priority Actions

### P1 - Need to fix (Lỗi CMR refer SAI):
1. **UC173-178 L102 (Field 7 Date Picker):** Bỏ CMR_05 (Date Picker không phải Numeric)
2. **UC173-178 L115 (Field 16 Date Picker):** Bỏ CMR_05, giữ CMR_11

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