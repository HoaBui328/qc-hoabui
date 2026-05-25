# Impact Matrix v2 — SRS-mobile Rà soát V1 đối chiếu CMR v1.11 & Align v6.1

**Document title:** Mobile SRS Impact Matrix v2
**Date created:** 2026-05-22
**Author/Agent:** Global Impact Analyzer
**Version:** v2
**Baseline:** Impact_Matrix_v1.md (2026-05-22, 32 lỗi / 11 files)
**Reference:** CMR_Mobile.md v1.11 (2026-05-22) + Align_CMR_Mobile_20260520.md v6.1

---

## 1. Tóm tắt thay đổi V1 → V2 (Re-verified after pull 2026-05-22)

| Hạng mục | V1 | V2 (sau pull) | V2 (sau fix) | Ghi chú |
|----------|----|----|----|---------| 
| Tổng findings ban đầu | 32 | — | — | — |
| Đã resolve (đóng) | — | 23 | **32** | +3 phát hiện đã fix (J, K×2) + 6 vừa sửa (M3, L1-L5) |
| Findings MỚI (V2) | — | 6 | **6** | CMR-15 placeholder (5) + UC256 intra-doc (1) |
| **Còn Pending** | — | 9 | **0** | ✅ Toàn bộ đã fix |
| Open Questions | 5 | 0 | **0** | Tất cả đã resolve |
| Files đã sửa | 11 | 6 | **4** | UC256, UC53, UC56-57, UC69 |

---

## 2. Findings ĐÃ ĐÓNG (Resolved / Exception)

| Finding V1 | Lý do đóng | Reference |
|------------|-----------|-----------|
| **D** (SĐT min-length format) | Đã sửa hoàn toàn ở UC249 v2.21, UC250 đúng format | V1 đã confirm ✅ |
| **F** (Mã bưu chính validation khác nhau) | **Align Exception:** Postal code = freetext, không giới hạn length/format | Align v6.1 §M — Confirmed Exceptions |
| **G** (Email max 255 vs 100) | CMR-09 default textbox = 255 → Email Người ĐD max 255 hợp lệ. Email Tổ chức = 100 là custom rule riêng | CMR-09 v1.11 + Align v6.1 |
| **H** (Mã định danh Body=50, AC=12) | **ĐÃ FIX:** UC250 v3.11 đã sửa Body từ 50→12. Hiện tại Body dòng 134 = 12, AC-10 = 12 → khớp nhau | UC250 v3.20 dòng 134 + AC-10 dòng 183 |
| **I** (Tên tổ chức EN max 150 vs 255) | Custom rule hợp lệ — UC ghi rõ 150 cho trường cụ thể, không vi phạm CMR | CMR-09: "Các trường có quy định riêng sẽ được ghi rõ trong từng UC" |
| **A3** (UC251 body Mật khẩu) | **ĐÃ FIX sau pull:** UC251 v1.9 dòng 45 đã sửa → `"Mật khẩu không được vượt quá 50 ký tự!"` | Verified 2026-05-22 |
| **A4** (UC251 AC-08 Mật khẩu) | **ĐÃ FIX sau pull:** UC251 AC-08 dòng 81 đã sửa → `"Mật khẩu không được vượt quá 50 ký tự!"` | Verified 2026-05-22 |
| **A5** (UC252 body Tên tổ chức) | **ĐÃ FIX sau pull:** UC252 v2.13 dòng 64 đã sửa → `"Tên tổ chức không được vượt quá 50 ký tự!"` | Verified 2026-05-22 |
| **A6** (UC252 AC-24 Tên tổ chức) | **ĐÃ FIX sau pull:** UC252 AC-24 dòng 183 đã sửa → `"Tên tổ chức không được vượt quá 50 ký tự!"` | Verified 2026-05-22 |
| **B2** (UC252 Nơi cấp Body vs AC) | **ĐÃ FIX sau pull:** Body dòng 67 = 255, AC-22 dòng 181 = 255 → khớp nhau | UC252 v2.8 changelog: "Nơi cấp max 500→255" |
| **E1-E4** (UC250 dropdown "!") | **ĐÃ FIX sau pull:** UC250 dòng 118-121 đã sửa → `"Vui lòng chọn [tên]"` (không có `!`) | Verified 2026-05-22 |
| **C1** (UC250_audited_v2 format cũ) | File audited cũ — không phải SRS gốc. UC250 v3.20 đã fix hoàn toàn | Cần regenerate nhưng không phải lỗi SRS |
| **J** (UC40 button state) | **ĐÃ FIX:** UC40 v3.8 dòng 56 đã ghi "Luôn Enabled (CMR-09 I01)" | Verified 2026-05-22 |
| **K** (UC7-11 D07/D08) | **ĐÃ FIX:** UC7-11 v1.3 đã bổ sung D07/D08 cho Searchable Dropdown | Verified 2026-05-22 |
| **K** (UC27-31 D07/D08) | **ĐÃ FIX:** UC27-31 v1.4 changelog ghi rõ "Bổ sung D07/D08 CMR-03" | Verified 2026-05-22 |
| **M3** (UC256 AC-02-3) | **ĐÃ FIX:** Sửa logic + format → `"Nhập khác 10/12 số → Mã định danh phải bao gồm đúng 10 hoặc 12 chữ số!"` | Fixed 2026-05-22 |
| **L1** (UC53 Ngày tạo) | **ĐÃ FIX:** Placeholder → `"Từ ngày - Đến ngày"` | Fixed 2026-05-22 |
| **L2** (UC53 Ngày hẹn trả) | **ĐÃ FIX:** Placeholder → `"Từ ngày - Đến ngày"` | Fixed 2026-05-22 |
| **L3** (UC56-57 Ngày đăng) | **ĐÃ FIX:** Placeholder → `"Từ ngày - Đến ngày"` | Fixed 2026-05-22 |
| **L4** (UC56-57 Nút Nhập lại) | **ĐÃ FIX:** Reset text → `"Từ ngày - Đến ngày"` | Fixed 2026-05-22 |
| **L5** (UC69 Ngày ban hành) | **ĐÃ FIX:** Placeholder → `"Từ ngày - Đến ngày"` | Fixed 2026-05-22 |

---

## 3. Findings GIỮ NGUYÊN (Vẫn còn lỗi)

### A — Error Format Cũ (`nhập quá ký tự cho phép`) [CMR_CONFLICT]

**CMR-09 v1.11 chuẩn:** `"[Tên trường] không được vượt quá [maxlength] ký tự!"`

| # | UC | Trường | Dòng | Hiện tại | Mục tiêu | Trạng thái |
|---|-----|--------|------|----------|----------|------------|
| A1 | UC256 | Mã định danh (§2.2 #2) | 66 | ✅ Đã sửa v2.12 | — | `Resolved` |
| A2 | UC256 | AC-02-3 | 198 | `"Mã định danh nhập quá ký tự cho phép"` | `"Mã định danh phải bao gồm đúng 10 hoặc 12 chữ số!"` | ✅ `Fixed` |
| A3 | UC251 | Mật khẩu mới (§2.1 #3) | 45 | ✅ Đã sửa v1.9 | — | `Resolved` |
| A4 | UC251 | AC-08 | 81 | ✅ Đã sửa v1.9 | — | `Resolved` |
| A5 | UC252 | Tên tổ chức (§2.2 #1) | 64 | ✅ Đã sửa v2.11 | — | `Resolved` |
| A6 | UC252 | AC-24 | 183 | ✅ Đã sửa v2.11 | — | `Resolved` |

**Kết luận:** Chỉ còn **A2 (UC256 AC-02-3)** chưa fix — đã merge vào finding M3 bên dưới.

---

### B — Intra-Document Max Length Mismatch [INTRA_DOC_CONFLICT]

| # | UC | Vị trí | Giá trị | Ghi chú | Trạng thái |
|---|-----|--------|---------|---------|------------|
| B1 | UC249 — Địa chỉ | Body vs AC | ✅ Đã sửa v2.20 | — | `Resolved` |
| B2 | UC252 — Nơi cấp | Body=255 vs AC=255 | ✅ Đã sửa v2.8 — cả hai khớp 255 | — | `Resolved` |

**Kết luận:** Toàn bộ group B đã resolve.

---

### ~~C — CMR Compliance [CMR_CONFLICT]~~ → RESOLVED

UC250 SRS gốc (v3.20) đã fix hoàn toàn. File `_audited_v2` là output QC agent cũ — cần regenerate nhưng không phải lỗi SRS.

---

### ~~E — Error message dropdown có dấu "!" [CMR_CONFLICT]~~ → RESOLVED

UC250 dòng 118-121 đã sửa: `"Vui lòng chọn [tên]"` (không có `!`). Verified sau pull.

---

### ~~J — UC40: Changelog-body Mismatch [INTRA_DOC_CONFLICT]~~ → RESOLVED

UC40 v3.8 dòng 56 đã ghi "**Luôn Enabled** (CMR-09 I01). Không có trạng thái Disabled." Verified 2026-05-22.

---

### ~~K — Missing D07/D08 Behavior (Searchable Dropdown) [CMR_CONFLICT]~~ → RESOLVED

| UC | Version | Trạng thái | Ghi chú |
|----|---------|------------|---------|
| UC7-11 | v1.3 | ✅ Đã có D07/D08 | Dòng 73: "Xóa hết keyword → placeholder", "Tap ra ngoài → Tất cả" |
| UC27-31 | v1.4 | ✅ Đã có D07/D08 | Changelog v1.3→v1.4: "Bổ sung D07/D08 CMR-03" |

---

## 4. Findings MỚI (V2)

### L — CMR-15 Placeholder Date Range: "Ngày bắt đầu - Ngày kết thúc" → "Từ ngày - Đến ngày" [CMR_CONFLICT]

**CMR-15 v1.11 chuẩn:** Placeholder: **"Từ ngày - Đến ngày"**

| # | UC | Trường | Dòng | Hiện tại | Mục tiêu | Trạng thái |
|---|-----|--------|------|----------|----------|------------|
| L1 | UC53 (Phản ánh kiến nghị) | Ngày tạo — Date Range Picker | 144 | Placeholder: `"Ngày bắt đầu - Ngày kết thúc"` | `"Từ ngày - Đến ngày"` | ✅ `Fixed` |
| L2 | UC53 (Phản ánh kiến nghị) | Ngày hẹn trả — Date Range Picker | 145 | Placeholder: `"Ngày bắt đầu - Ngày kết thúc"` | `"Từ ngày - Đến ngày"` | ✅ `Fixed` |
| L3 | UC56-57/66-68 (Tin tức) | Input Chọn ngày đăng — Date Range Picker | 81 | Placeholder: `"Ngày bắt đầu - Ngày kết thúc"` | `"Từ ngày - Đến ngày"` | ✅ `Fixed` |
| L4 | UC56-57/66-68 (Tin tức) | Nút "Nhập lại" — reset text | 82 | Reset về `"Ngày bắt đầu - Ngày kết thúc"` | Reset về `"Từ ngày - Đến ngày"` | ✅ `Fixed` |
| L5 | UC69 (Tra cứu VBPL) | Khoảng ngày ban hành — Date Range Picker | 76 | Placeholder: `"Ngày bắt đầu - Ngày kết thúc"` | `"Từ ngày - Đến ngày"` | ✅ `Fixed` |

**Các UC ĐÃ ĐÚNG (không cần sửa):**
- UC45-51 (dòng 88-89): ✅ Đã dùng "Từ ngày - Đến ngày"
- UC2 (dòng 454-455): ✅ Đã dùng "Từ ngày" / "Đến ngày"
- UC7-11 (dòng 453-454): ✅ Đã dùng "Từ ngày" / "Đến ngày"
- UC12-16 (dòng 383-384): ✅ Đã dùng "Từ ngày" / "Đến ngày"
- UC17-21 (dòng 393-394): ✅ Đã dùng "Từ ngày" / "Đến ngày"
- UC22-26 (dòng 415-416): ✅ Đã dùng "Từ ngày" / "Đến ngày"
- UC27-31 (dòng 413-414): ✅ Đã dùng "Từ ngày" / "Đến ngày"
- UC41 (dòng 60-63): ✅ Đã dùng "Từ ngày" / "Đến ngày"
- UC58 (dòng 72): ✅ Đã dùng "Từ ngày" / "Đến ngày"

---

### M — UC256: Body vs AC Conflict — Mã định danh validation [INTRA_DOC_CONFLICT]

**Mô tả:** UC256 v2.12 đã cập nhật body (dòng 66, 84) với validation mới theo CMR-09 v1.11, nhưng AC-02-3 (dòng 198) vẫn giữ format cũ và logic cũ (max 13 số thay vì đúng 10/12 số).

| # | UC | Vị trí | Hiện tại | Mục tiêu | Trạng thái |
|---|-----|--------|----------|----------|------------|
| M1 | UC256 | Body §2.2 #2 (dòng 66) | ✅ `"Mã định danh phải bao gồm đúng 10 hoặc 12 chữ số!"` | — | `Resolved` |
| M2 | UC256 | Body §3.1 (dòng 84) | ✅ `"Mã định danh phải bao gồm đúng 10 hoặc 12 chữ số!"` | — | `Resolved` |
| M3 | UC256 | **AC-02-3** (dòng 198) | `"Nhập quá 13 số → Mã định danh nhập quá ký tự cho phép"` | `"Nhập khác 10/12 số → Mã định danh phải bao gồm đúng 10 hoặc 12 chữ số!"` | ✅ `Fixed` |

**Issue:** AC-02-3 có 2 vấn đề:
1. **Logic sai:** Ghi "quá 13 số" nhưng CMR-09 v1.11 quy định đúng 10 hoặc 12 số (không phải max 13)
2. **Format sai:** Dùng `"nhập quá ký tự cho phép"` thay vì format CMR-09 chuẩn

---

## 5. Open Questions (Cập nhật)

| # | Câu hỏi | Trạng thái | Resolution |
|---|---------|------------|------------|
| ~~OQ-01~~ | ~~Dấu "!" ở error dropdown~~ | ✅ Resolved | CMR-03: KHÔNG có `!` |
| ~~OQ-02~~ | ~~Mã bưu chính UC250 validate?~~ | ✅ Resolved | Align Exception: freetext |
| ~~OQ-03~~ | ~~Email Người ĐD max 255 hay 100?~~ | ✅ Resolved | CMR-09 default 255 hợp lệ |
| ~~OQ-04~~ | ~~Mã định danh Body=50, AC=12?~~ | ✅ Resolved | UC250 v3.11 đã sửa Body→12. Cả hai khớp |
| ~~OQ-05~~ | ~~Tên tổ chức EN max 150 hay 255?~~ | ✅ Resolved | Custom rule hợp lệ |
| ~~OQ-06~~ | ~~UC252 Nơi cấp: Body=500 vs AC=255?~~ | ✅ Resolved | **ĐÃ FIX sau pull:** UC252 v2.8 sửa Body 500→255. Hiện tại Body dòng 67 = 255, AC-22 dòng 181 = 255 → khớp |

---

## 6. Self-Audit Evidence Table

| ID | Mục kiểm tra | Chi tiết | Kết quả | Ghi chú |
|----|-------------|----------|---------|---------|
| SA-01 | File coverage — CMR-15 scan | Đã scan 15 UC có date range filter. Phát hiện 3 UC vi phạm (UC53, UC56-57, UC69). 12 UC đã đúng | ✅ | Grep pattern: "Ngày bắt đầu\|Từ ngày" |
| SA-02 | CMR-09 Mã định danh/MST scan | Đã check UC249, UC250, UC252, UC256. UC250 body+AC khớp (12). UC256 body đúng nhưng AC-02-3 sai | ✅ | CMR v1.11 rule mới |
| SA-03 | Re-verify V1 findings | Đã đọc lại UC256 (dòng 66, 84, 198), UC250 (dòng 134, 183), UC251, UC252 | ✅ | Confirm A2-A6, E1-E4 vẫn còn |
| SA-04 | Intra-doc cross-check (Body↔AC) | UC256: Body dòng 66 ≠ AC-02-3 dòng 198 → CONFLICT mới (M3) | ✅ | Finding M mới |
| SA-05 | Align Exception verification | Đã đối chiếu Align v6.1 §M: Postal code=freetext, Search placeholder UC87=exception | ✅ | Đóng findings F, G, I |
| SA-06 | CMR v1.11 changelog verification | 2 thay đổi: CMR-15 placeholder + CMR-09 Mã định danh/MST | ✅ | Tạo findings L, M |
| SA-07 | Re-verify sau pull (2026-05-22) | Đọc lại UC250 (dòng 118-121), UC251 (dòng 45, 81), UC252 (dòng 64, 67, 181, 183). Confirm 10 findings đã fix | ✅ | A3-A6, B2, E1-E4, OQ-06 resolved |

---

## 7. Tổng hợp Impact Matrix — Bảng chính

| # | Tên File | Vị trí | Lỗi | Current Text | Target Text | Trạng thái |
|---|----------|--------|-----|-------------|-------------|------------|
| 1 | UC256_DangNhapMobile.md | AC-02-3 (dòng 198) | [INTRA_DOC_CONFLICT] + [CMR_CONFLICT] Body đã sửa nhưng AC chưa sync | `"Nhập quá 13 số → Mã định danh nhập quá ký tự cho phép"` | `"Nhập khác 10/12 số → Mã định danh phải bao gồm đúng 10 hoặc 12 chữ số!"` | ✅ `Fixed` |
| 2 | UC40 | Body §2.1 (dòng 56) | [INTRA_DOC_CONFLICT] Changelog ghi đã sửa nhưng body chưa reflect | `"Disabled (grayed out) khi validation fail"` | `"Luôn Enabled"` (CMR-09 I01) | ✅ `Fixed` (đã fix trước pull) |
| 3 | UC7-11 | Searchable Dropdown | [CMR_CONFLICT] Thiếu D07/D08 | Không mô tả hành vi xóa keyword/tap ngoài | Bổ sung D07/D08 theo CMR-03 | ✅ `Fixed` (v1.3) |
| 4 | UC27-31 | Searchable Dropdown | [CMR_CONFLICT] Thiếu D07/D08 | Không mô tả hành vi xóa keyword/tap ngoài | Bổ sung D07/D08 theo CMR-03 | ✅ `Fixed` (v1.4) |
| 5 | UC53_PhanAnhKienNghi.md | Ngày tạo (dòng 144) | [CMR_CONFLICT] Placeholder date range cũ | `"Ngày bắt đầu - Ngày kết thúc"` | `"Từ ngày - Đến ngày"` | ✅ `Fixed` |
| 6 | UC53_PhanAnhKienNghi.md | Ngày hẹn trả (dòng 145) | [CMR_CONFLICT] Placeholder date range cũ | `"Ngày bắt đầu - Ngày kết thúc"` | `"Từ ngày - Đến ngày"` | ✅ `Fixed` |
| 7 | UC56-57_66-68_TinTuc.md | Input Chọn ngày đăng (dòng 81) | [CMR_CONFLICT] Placeholder date range cũ | `"Ngày bắt đầu - Ngày kết thúc"` | `"Từ ngày - Đến ngày"` | ✅ `Fixed` |
| 8 | UC56-57_66-68_TinTuc.md | Nút Nhập lại (dòng 82) | [CMR_CONFLICT] Reset text dùng placeholder cũ | Reset về `"Ngày bắt đầu - Ngày kết thúc"` | Reset về `"Từ ngày - Đến ngày"` | ✅ `Fixed` |
| 9 | UC69_TraCuuVBPL.md | Khoảng ngày ban hành (dòng 76) | [CMR_CONFLICT] Placeholder date range cũ | `"Ngày bắt đầu - Ngày kết thúc"` | `"Từ ngày - Đến ngày"` | ✅ `Fixed` |

**Tổng: 0 lỗi Pending.** Toàn bộ 9 findings đã được fix (3 đã fix trước pull, 6 vừa sửa 2026-05-22).

---

## 8. Appendix: Source Files

| File | Version | Trạng thái V2 |
|------|---------|---------------|
| UC249_QuanLyThongTinTaiKhoanCaNhan.md | v2.23 | ✅ Không còn lỗi |
| UC250_QuanLyTaiKhoanDoanhNghiep.md | v3.20 | ✅ Không còn lỗi (E1-E4 đã fix sau pull) |
| UC250_audited_v2.md | audited | ⚠️ Cần regenerate (không phải lỗi SRS gốc) |
| UC251_DoiMatKhau.md | v1.9 | ✅ Không còn lỗi (A3-A4 đã fix sau pull) |
| UC252_DangKyTaiKhoan.md | v2.13 | ✅ Không còn lỗi (A5-A6, B2 đã fix sau pull) |
| UC253_GuiThongTinQuenMatKhau.md | latest | ✅ Không lỗi |
| UC256_DangNhapMobile.md | v2.12 | ✅ Đã fix M3 (AC-02-3) |
| UC40_TraCuuDatKCN.md | v3.8 | ✅ Đã fix trước pull (J — button state) |
| UC7-11 | v1.3 | ✅ Đã fix trước pull (K — D07/D08) |
| UC27-31 | v1.4 | ✅ Đã fix trước pull (K — D07/D08) |
| UC53_63-65_PhanAnhKienNghi.md | latest | ✅ Đã fix L1-L2 (placeholder) |
| UC56-57_66-68_TinTuc.md | v1.7 | ✅ Đã fix L3-L4 (placeholder + reset) |
| UC69_TraCuuVanBanPhapLuat.md | latest | ✅ Đã fix L5 (placeholder) |
| UC87 v2.2 | v2.2 | ✅ Đã fix hoàn toàn |
| UC60-61_Chatbot.md | v1.4 | ✅ Không lỗi |
| UC70 v5 | v5 | ✅ Không lỗi |
| CMR_Mobile.md | v1.11 | Reference standard |
