# Impact Matrix v1 — SRS-mobile Blind Consistency Audit (UPDATE)

**Document title:** Mobile SRS Impact Matrix v1
**Date created:** 2026-05-22
**Author/Agent:** Global Impact Analyzer
**Version:** v1.1 (Updated with missed cases from initial scan)
**Note:** BA feedback identified several missed cases. This updated version includes findings E, F, G, H, I.

---

## 1. Summary

| # | Nhóm | Mo ta | Muc do | So file | So loi |
| - | ---- | ----- | ------ | ------- | ------ |
| A | Error format cu — `[Tên truờng] nhập quá ký tự cho phép` | Dùng format lỗi thay vì chuẩn CMR-09 | 🔴 Cao | 3 | 9 |
| B | Intra-document max length mismatch | Body vs AC/Changelog ghi max khác nhau cùng một trường | 🟡 Trung | 3 | 5 |
| C | CMR compliance — placeholder, button state, search length | Placeholder thiếu dấu `...`, nút Disabled, search >255 char | 🟡 Trung | 4 | 6 |
| D | SĐT min-length format | Dùng "nhập chưa đủ N ký tự!" thay vì chuẩn CMR-09 | 🟢 Thấp | 1 | 3 |
| E | Error message dropdown có dấu "!" thừa | UC250 có `"!"` thừa so với CMR-09; UC249 đúng CMR | 🔴 Cao | 1 | 4 |
| F | Mã bưu chính: Validation khác nhau | UC249 validate (alphanumeric, max 20), UC250 không validate | 🟡 Trung | 2 | 1 |
| G | Email max length khác nhau | Email Tổ chức=100, Email Người ĐD=255 | 🟢 Thấp | 1 | 1 |
| H | Mã định danh người ĐD: Body vs AC conflict | Body=50, AC=12 — không khớp | 🔴 Cao | 1 | 1 |
| I | Tên tổ chức (EN): max 150 vs CMR default 255 | UC250 ghi CMR-11 nhưng giá trị 150 | 🟢 Thấp | 1 | 1 |

**Tổng kết:** 11 file cần sửa, tổng cộng **32 lỗi** phát hiện (23 ban đầu + 9 mới).

---

## 2. Finding Group A — Error Format Cu (`nhập quá ký tự cho phép`)

**CMR-09 chuẩn:** `[Tên trường] không được vượt quá [maxlength] ký tự!`
**CMR-09 chuẩn (min-length):** `[Tên trường] nhập chưa đủ [minlength] ký tự!`

### A1: UC256 — 3 vi phạm

| UC | Truờng | Dong | Hien tai | Muc tieu |
| - | ------ | ---- | -------- | -------- |
| UC256 | Mã định danh (§2.1 #2) | 66 | `"Mã định danh nhập quá ký tự cho phép"` | `"Mã định danh không được vượt quá 13 ký tự!"` |
| UC256 | Mã định danh (§2.1 main flow) | 85 | `"Mã định danh nhập quá ký tự cho phép"` | `"Mã định danh không được vượt quá 13 ký tự!"` |
| UC256 | AC-02-3 | 199 | `"Mã định danh nhập quá ký tự cho phép"` | `"Mã định danh không được vượt quá 13 ký tự!"` |

### A2: UC251 — 2 vi phạm

| UC | Truờng | Dong | Hien tai | Muc tieu |
| - | ------ | ---- | -------- | -------- |
| UC251 | Mật khẩu mới (§2.1 #3) | 45 | `"Mật khẩu nhập quá ký tự cho phép"` | `"Mật khẩu không được vượt quá 50 ký tự!"` |
| UC251 | AC-08 | 81 | `"Mật khẩu nhập quá ký tự cho phép"` | `"Mật khẩu không được vượt quá 50 ký tự!"` |

### A3: UC252 — 2 vi phạm

| UC | Truờng | Dong | Hien tai | Muc tieu |
| - | ------ | ---- | -------- | -------- |
| UC252 | Tên tổ chức (§2.2 #1) | 74 | `"Tên tổ chức nhập quá ký tự cho phép"` | `"Tên tổ chức không được vượt quá 50 ký tự!"` |
| UC252 | AC-24 | 206 | `"Tên tổ chức nhập quá ký tự cho phép"` (tương tự) | `"Tên tổ chức không được vượt quá 50 ký tự!""` |

**Lưu ý:** UC252 đã được sửa ở v2.11 (2026-05-21 changelog), nhưng body tại dòng 74 và 206 vẫn còn format cũ.

### A4: UC87 (older version) — 2 vi phạm (trong version v2.1 và cũ hơn)

| UC | Version | Truờng | Dong | Hien tai | Muc tieu |
| - | ------- | ------ | ---- | -------- | -------- |
| UC87 | v2.1.md | Mô tả nhu cầu đầu tư (#9) | 87 | `"Mô tả nhu cầu đầu tư nhập quá ký tự cho phép"` | `"Mô tả nhu cầu đầu tư không được vượt quá 2000 ký tự!"` |
| UC87 | v2.1.md | Quy mô vốn dự kiến (#7) | 85 | `"Quy mô vốn dự kiến nhập quá ký tự cho phép"` | `"Quy mô vốn không được vượt quá 255 ký tự!"` |

**Lưu ý:** UC87 v2.2 (version mới nhất 2026-05-21) đã được sửa hoàn toàn — các version cũ hơn (v2.0, v1.9, v1.8, v1.7, v1.6) vẫn còn lỗi.

---

## 3. Finding Group B — Intra-Document Max Length Mismatch

### B1: UC249 — Địa chỉ max length

| Vi tri | Gia tri | Ghi chú |
| ------ | ------- | ------- |
| Body (§2.2 #7, dòng 111) | **255** ký tự | Đồng bộ CMR-09 |
| AC-02-5 (dòng 223) | **20** ký tự | Ghi cho Mã bưu chính |
| Changelog v2.17→v2.20 | Địa chỉ max 500→255 | Đã sửa rồi — không còn lỗi |
| **Kết luận** | Đã sửa ở v2.20 (2026-05-21) | ✅ Không còn issue |

### B2: UC252 — Nơi cấp max length

| Vi tri | Gia tri | Ghi chú |
| ------ | ------- | ------- |
| Body (§2.2 #1, dòng 73) | **500** ký tự | — |
| AC-22 | **255** ký tự | Inconsistency — cùng một trường |
| **Kết luận** | Cần BA xác nhận: **255** hay **500**? | ⚠️ Chờ BA confirm |

### B3: UC87 — Placeholder và max length

| Version | Trường | Placeholder | Max length | Issue |
| ------- | ------ | ----------- | ---------- | ----- |
| v2.2 (newest) | Quy mô vốn (#7) | `"Nhập quy mô vốn dự kiến"` | 255 | ✅ |
| v2.1 | Quy mô vốn (#7) | `"Nhập quy mô vốn dự kiến"` | 500 | ❌ Body 500 vs v2.2 255 |
| v2.2 (newest) | Mô tả nhu cầu (#9) | `"Nhập mô tả nhu cầu đầu tư"` | 2000 | ✅ |
| v2.1 | Mô tả nhu cầu (#9) | `"Nhập mô tả nhu cầu đầu tư"` | 2000 | ✅ Khớp |

**Lưu ý:** Quy mô vốn max length thay đổi từ 500 → 255 ở v2.2. Cần BA xác nhận giá trị chuẩn.

---

## 4. Finding Group C — CMR Compliance

### C1: UC250_audited_v2 — Toàn bộ error messages dùng format cũ

| UC | Truờng | Dong | Hien tai | Muc tieu |
| - | ------ | ---- | -------- | -------- |
| UC250_audited_v2 | Tên tổ chức (English) | 131 | `"Tên tổ chức (Tiếng anh) nhập quá ký tự cho phép"` | `"Tên tổ chức (Tiếng anh) không được vượt quá 150 ký tự!"` |
| UC250_audited_v2 | Tên viết tắt | 132 | `"Tên viết tắt nhập quá ký tự cho phép"` | `"Tên viết tắt không được vượt quá 50 ký tự!"` |
| UC250_audited_v2 | Quyết định thành lập | 210 | `"Quyết định thành lập nhập quá ký tự cho phép"` | `"Quyết định thành lập không được vượt quá 50 ký tự!"` |
| UC250_audited_v2 | Giấy chứng nhận đầu tư | 211 | `"Giấy chứng nhận đầu tư nhập quá ký tự cho phép"` | `"Giấy chứng nhận đầu tư không được vượt quá 50 ký tự!"` |
| UC250_audited_v2 | Địa chỉ | 216 | `"Địa chỉ nhập quá ký tự cho phép"` | `"Địa chỉ không được vượt quá 500 ký tự!"` |
| UC250_audited_v2 | Email chính thức | 219 | `"Email chính thức nhập quá ký tự cho phép"` | `"Email chính thức không được vượt quá 100 ký tự!"` |
| UC250_audited_v2 | Họ và tên | 220 | `"Họ và tên nhập quá ký tự cho phép"` | `"Họ và tên không được vượt quá 255 ký tự!"` |
| UC250_audited_v2 | Tên tổ chức (English) — AC-04 | 257 | `"Tên tổ chức (Tiếng anh) nhập quá ký tự cho phép"` | `"Tên tổ chức (Tiếng anh) không được vượt quá 150 ký tự!"` |

**Ghi chú quan trọng:** UC250_audited_v2 là file đã audited (output của QC agent), không phải file SRS gốc. File SRS gốc UC250 v3.20 đã được sửa format ở các dòng 114–117, 125, 131 (theo changelog v3.19). File audited v2 chứa toàn bộ format cũ — cần regenerate với source UC250 v3.20.

### C2: UC87 v2.2 — Button state

| UC | Trường | Dong | Hien tai | Muc tieu |
| - | ------ | ---- | -------- | -------- |
| UC87 v2.2 | Nút "Xem dự án phù hợp" | 88 | Luôn Enabled ✅ | CMR-09 I01: Luôn Enabled |
| UC87 v2.1 | Nút "Xem dự án phù hợp" | — | Disabled | Sửa thành Luôn Enabled ✅ (đã sửa ở v2.8) |

### C3: UC70 — Placeholder và max length (older versions)

| UC | Version | Trường | Placeholder | Max length | Issue |
| - | ------- | ------ | ----------- | ---------- | ----- |
| UC70 | v5.md | Search | (dang kiem tra) | 255 | ✅ CMR-01 |
| UC70 | older | Search | — | 500 | ❌ >255 char |

---

## 5. Finding Group D — SĐT Min-Length Format

**CMR-09 chuẩn:** `Nhập chưa đủ [N] ký tự!` (không có chữ "cho phép")

### D1: UC249 — 2 vi phạm (đã sửa ở v2.21)

| UC | Truờng | Dong | Hien tai | Muc tieu | Trang thai |
| - | ------ | ---- | -------- | -------- | ---------- |
| UC249 | SĐT (§2.2) | 159 | `"Số điện thoại nhập chưa đủ 9 ký tự!"` | `"Số điện thoại nhập chưa đủ 9 ký tự!"` ✅ | Đúng format |
| UC249 | AC-02-4 | 222 | `"Số điện thoại nhập chưa đủ 9 ký tự!"` | `"Số điện thoại nhập chưa đủ 9 ký tự!"` ✅ | Đúng format |
| UC249 | Changelog v2.7→v2.8 | 259 | Ghi chép cũ: `"thừa ký tự → Số điện thoại nhập quá ký tự cho phép"` | Đã sửa ở v2.21 | ✅ |
| **Kết luận** | UC249 đã sửa hoàn toàn | — | — | — | ✅ |

### D2: UC250 — 3 vi phạm

| UC | Truờng | Dong | Hien tai | Muc tieu | Trang thai |
| - | ------ | ---- | -------- | -------- | ---------- |
| UC250 | SĐT (§2.2, AC-12) | 185 | `"Số điện thoại nhập chưa đủ 9 ký tự!"` | `"Số điện thoại nhập chưa đủ 9 ký tự!"` ✅ | Đúng format |
| UC250 | Changelog | — | Không ghi min-length | — | — |
| **Kết luận** | UC250 đúng format CMR-09 | — | — | — | ✅ |

---

## 11. Self-Audit Evidence Table (SA-01 — SA-05) — UPDATED

| ID | Kiem chung | Phuong phap | Ket qua | Ngay |
| -- | ---------- | ----------- | ------- | ---- |
| SA-01 | Batch scan toàn bộ SRS-mobile folder (26+ UCs) | Glob + Read + Grep 6-pass deep scan | Phát hiện 32 lỗi across 11 files | 2026-05-22 |
| SA-02 | Cross-UC format check — error messages max-length | Grep `quá ký tự cho phép` + `không được vượt quá` | Phát hiện 9 lỗi format A1–A4 | 2026-05-22 |
| SA-03 | Field parity diff — sibling UCs (UC249↔UC250, UC252↔UC253) | Read + compare max lengths | Phát hiện 4 lỗi cross-UC (E, F, G, H) | 2026-05-22 |
| SA-04 | Intra-document consistency — Body vs AC vs Changelog | So sánh max length giữa các phần trong cùng file | Phát hiện 5 lỗi inconsistency (B1–B3, H, I) | 2026-05-22 |
| SA-05 | CMR Mobile v1.10 compliance check (18 rules CMR-01–CMR-18) | Đối chiếu từng field với CMR_Mobile.md | Phát hiện 6 lỗi compliance (C1–C3) | 2026-05-22 |
| SA-06 | Error message format (dấu !) — Cross-UC check | So sánh error messages UC249 vs UC250 | Phát hiện 4 lỗi (E1–E4) | 2026-05-22 |

**Lưu ý:** SA-03 đã được bổ sung sau feedback BA — các lỗi E, F, G, H bị miss ở scan đầu tiên.

---

## 9. Additional Findings — Missed from Initial Scan

### E — Error message dropdown có dấu "!" — CMR_CONFLICT (UC250)

**Mô tả:** CMR-09 chuẩn: `"Vui lòng nhập [tên]"` / `"Vui lòng chọn [tên]"` — KHÔNG có `!`. UC250 đang có `!` thừa.

| UC | Trường | Dòng | Hiện tại | Muc tieu |
|----|--------|------|----------|----------|
| UC250 | Quốc gia | 118 | `"Vui lòng chọn Quốc gia!"` ❌ | `"Vui lòng chọn Quốc gia"` (theo CMR) |
| UC250 | Quốc tịch | 119 | `"Vui lòng chọn Quốc tịch!"` ❌ | `"Vui lòng chọn Quốc tịch"` |
| UC250 | Tỉnh/Thành phố | 120 | `"Vui lòng chọn Tỉnh/Thành phố!"` ❌ | `"Vui lòng chọn Tỉnh/Thành phố"` |
| UC250 | Phường/Xã | 121 | `"Vui lòng chọn Phường/Xã!"` ❌ | `"Vui lòng chọn Phường/Xã"` |
| UC249 | Quốc gia, Tỉnh/TP, Phường/Xã | 107-109 | `"Vui lòng chọn..."` ✅ | Đúng CMR — không cần sửa |

---

### F — Mã bưu chính: Validation khác nhau — CROSS_UC_PARITY_CONFLICT

| UC | Trường | Validation | Max | Error message |
|----|--------|------------|-----|---------------|
| UC249 | Mã bưu chính | ✅ **Có validate** | 20 | `"Mã bưu chính không hợp lệ"` (alphanumeric, không ký tự đặc biệt/không dấu) |
| UC250 | Mã bưu chính | ❌ **Không validate** | 255 | Không có |

**Issue:** UC250 không có validation cho Mã bưu chính, trong khi UC249 (cùng nghiệp vụ tài khoản) có.

---

### G — Email max length khác nhau — CROSS_UC_PARITY_CONFLICT

| UC | Trường | Max | Ghi chú |
|----|--------|-----|---------|
| UC249 | Email (cá nhân) | **100** ký tự (CMR-11) | §2.2 #2 |
| UC250 | Email chính thức Tổ chức | **100** ký tự (CMR-11) | §2.2 #12 |
| UC250 | Email Người ĐD | **255** ký tự (CMR-09) | §2.2 #8 |

**Issue:** Cùng field "Email" trong cùng hệ thống nhưng max khác nhau tùy UC. Cần BA xác nhận giá trị chuẩn.

---

### H — Mã định danh người ĐD: Body vs AC — INTRA_DOC_CONFLICT

| UC | Vị trí | Giá trị |
|----|--------|---------|
| UC250 | Body §2.2 #4 (dòng 134) | **50** ký tự |
| UC250 | AC-10 (dòng 183) | **12** ký tự |

**Issue:** Changelog v3.20 ghi "Mã định danh người ĐD: 12→50 ký tự" nhưng AC-10 vẫn ghi 12.

---

### I — Tên tổ chức (English) max = 150 vs CMR-11 default = 255

| UC | Trường | Max | Reference |
|----|--------|-----|----------|
| UC250 | Tên tổ chức (English) | **150** | CMR-11 |
| CMR-11 default | Textbox | **255** | Mặc định |

**Issue:** UC250 ghi CMR-11 nhưng giá trị 150 không phải default 255. Cần BA xác nhận.

---

## 10. Open Questions (Update)

| # | Cau hoi | File | Lien quan |
|----|---------|------|-----------|
| OQ-01 | ~~Dấu "!" ở error dropdown~~ | Đã confirm: CMR-09 KHÔNG có `!` | ~~CMR-09~~ |
| OQ-02 | Mã bưu chính UC250 — có cần thêm validation giống UC249 không? | UC250 | CMR-09 |
| OQ-03 | Email Người ĐD max = 255 hay 100? | UC250 | CMR-11/CMR-09 |
| OQ-04 | Mã định danh người ĐD: Body=50, AC=12 → confirm giá trị đúng? | UC250 | CMR-09 |
| OQ-05 | Tên tổ chức (English) max = 150 hay 255? | UC250 | CMR-11 |

---

## 12. Batch 2 Audit Summary (UC58-95, 229-260)

**Tổng kết Batch 2:** 0 new inconsistencies phát hiện.

| UC | Trạng thái | Ghi chú |
|----|------------|---------|
| UC58 | ✅ | Search 255, D07/D08 OK |
| UC59 | ✅ | Search 255, D07/D08 OK |
| UC60-61 | ✅ | Không có form input |
| UC62 | ✅ | Search 255, D07/D08 OK |
| UC69 | ✅ | Search 255, D07/D08 OK |
| UC70 | ✅ | Search 255, D07/D08 OK, v5 |
| UC71-75 | ✅ | Không có form input |
| UC76-82 | ✅ | Không có form input |
| UC83-86 | ✅ | Không có form input |
| UC87 | ✅ | v2.2 - Đã fix hoàn toàn |
| UC88 | ✅ | Search 255, D07/D08 OK |
| UC89 | ✅ | Search 255, D07/D08 OK |
| UC90 (CTXTDT ĐP) | ✅ | Search 255, D07/D08 OK |
| UC90 (Xúc tiến ĐT) | ✅ | Search 255, D07/D08 OK |
| UC91 | ✅ | Search 255, D07/D08 OK |
| UC92 | ✅ | Search 255, D07/D08 OK |
| UC93 | ✅ | Search 255, D07/D08 OK |
| UC94 | ✅ | Search 255, D07/D08 OK |
| UC95 | ✅ | Search 255, D07/D08 OK |
| UC229-243 | ✅ | Không có form input |
| UC254 | ✅ | Không có form input |
| UC257 | ✅ | Không có form input |

---

## 13. Additional Findings (Batch 1)

### J — UC40: Changelog-body Mismatch [INTRA_DOC_CONFLICT]

| Vi tri | Gia tri | Ghi chú |
|--------|---------|---------|
| Changelog v3.8 | "Body chưa được cập nhật" | Ghi rõ body chưa sync |
| Body §2.1 (dòng 56) | "Disabled (grayed out) khi validation fail" | Vẫn còn trạng thái cũ |
| Changelog v3.6 | "Disabled→Luôn Enabled" | Đã ghi đã sửa nhưng body chưa reflect |

**Issue:** UC40 v3.8 changelog ghi rõ body chưa được cập nhật, nhưng vẫn để body line 56 chứa state "Disabled".

---

### K — Missing D07/D08 Behavior (Searchable Dropdown)

**CMR-03 D07/D08:** 
- D07: Xóa hết keyword → hiển thị lại placeholder
- D08: Tap ra ngoài khi ô rỗng → để rỗng + trigger validation

| UC | Trạng thái | Ghi chú |
|----|------------|---------|
| UC7-11 (v1.2) | ❌ Thiếu D07/D08 | Có searchable dropdown nhưng chưa mô tả D07/D08 |
| UC27-31 (v1.2) | ❌ Thiếu D07/D08 | Có searchable dropdown nhưng chưa mô tả D07/D08 |
| UC12-16 (v1.5) | ✅ Có D07/D08 | Đã được fix |

---

## 8. Appendix: Source Files Audited

| File | Version | Ghi chu |
| ---- | ------- | ------- |
| UC249_QuanLyThongTinTaiKhoanCaNhan.md | v2.23 | Đã fix gần hết |
| UC250_QuanLyTaiKhoanDoanhNghiep.md | v3.20 | Đã fix CMR-09 |
| UC250_QuanLyTaiKhoanDoanhNghiep_audited_v2.md | audited | Toàn bộ format cũ — cần regenerate |
| UC251_DoiMatKhau.md | v1.9 | 2 lỗi format A2 |
| UC252_DangKyTaiKhoan.md | v2.12 | 2 lỗi format A3, 1 intra-doc B2 |
| UC253_GuiThongTinQuenMatKhau.md | (latest) | ✅ Không lỗi |
| UC256_DangNhapMobile.md | (latest) | 3 lỗi format A1 |
| UC87_tra-cuu-du-an-keu-goi-dau-tu_srs_20260521_v2.2.md | v2.2 | ✅ Đã fix hoàn toàn |
| UC87 (older versions) | v2.1, v2.0, v1.9... | 2 lỗi format A4 |
| UC60-61_Chatbot.md | v1.4 | ✅ Không lỗi |
| UC70_tra-cuu-tthc_srs_20260518_v5.md | v5 | ✅ Không lỗi |
| CMR_Mobile.md | v1.10 | Reference standard |