# Global Impact Matrix — UC249 / UC250 / UC251 / UC252 / UC253 / UC256
- **Ngày check:** 2026-05-22
- **Phạm vi:** Mobile — Nhóm Quản lý & Xác thực Tài khoản (6 UC)
- **Phiên bản UC:** UC249 v2.23 · UC250 v3.20 · UC251 v1.9 · UC252 v2.13 · UC253 v2.6 · UC256 v2.12
- **CMR tham chiếu:** CMR_Mobile.md (v1.10) — Rule H (no trailing period), CMR-07, CMR-09, CMR-11, CMR-14, CMR-16, CMR-18

---

## PASS 1 — Cross-UC Parity Conflicts (Field-by-Field)

### 1.1 Trường: Mã định danh

| ID | UC | Vị trí | Current | Target | Loại | Status |
|---|---|---|---|---|---|---|
| P1-01 | UC252 | §2.2 #2, L65, AC-17 | Rule Cá nhân VN: **"đúng 12 chữ số"** | Đồng bộ UC256: **"10 hoặc 12 chữ số"** (CMND cũ 10 số vẫn hợp lệ) | CROSS_UC_PARITY | `BA Confirm` |
| P1-02 | UC252 | §2.2 #2, L65, L176 | Error min: `"Mã định danh nhập chưa đủ 12 ký tự!"` Error max: `"không được vượt quá 12 ký tự!"` | `"Mã định danh phải bao gồm đúng 10 hoặc 12 chữ số!"` (sau khi BA confirm P1-01) | CROSS_UC_PARITY | `BA Confirm` |
| P1-03 | UC252 | §2.2 #2, L66 — Placeholder | `"Nhập Mã định danh"` (M hoa) | `"Nhập mã định danh"` (m thường — theo UC256 §2.2) | CROSS_UC_PARITY | `Pending` |
| P1-04 | UC253 | §2.1 #5, L49 — Max length | `"Max length: 50 ký tự"` | `"Max length: 12 ký tự"` (50 vô nghĩa khi MĐD chỉ tối đa 12 số) | CROSS_UC_PARITY | `Pending` |
| P1-05 | UC253 | §2.1 #5, L49 — Thiếu validate độ dài | Chỉ validate ký tự không hợp lệ; **không validate đúng 10/12 số** | Bổ sung: *"Độ dài khác 10/12 số → `"Mã định danh phải bao gồm đúng 10 hoặc 12 chữ số!"`"* | CROSS_UC_PARITY | `Pending` |
| P1-06 | UC250 | §2.2 Edit — Mã ĐD người ĐD, L134 — Thiếu min length | Chỉ có rule max 12; không có rule nhập ít hơn 12 số | Bổ sung: *"Nhập ít hơn 12 số → `"Mã định danh nhập chưa đủ 12 ký tự!"`"* | CROSS_UC_CONFLICT | `Pending` |

### 1.2 Trường: Mật khẩu

| ID | UC | Vị trí | Current | Target | Loại | Status |
|---|---|---|---|---|---|---|
| P2-01 | UC252 | §2.2 #1 MK, L81 — Error để trống | `"Vui lòng nhập Mật khẩu!"` (có `!`) | `"Vui lòng nhập Mật khẩu"` (bỏ `!` đồng nhất UC256 L86) | CROSS_UC_PARITY | `BA Confirm` |
| P2-02 | UC251 | §2.1 #2 MK Hiện tại, L44 — Error để trống | `"Vui lòng nhập Mật khẩu hiện tại!"` (có `!`) | `"Vui lòng nhập Mật khẩu hiện tại"` (đồng nhất UC256) | CROSS_UC_PARITY | `BA Confirm` |
| P2-03 | UC251 | §2.1 #4 XN MK, L46 — Error để trống | `"Vui lòng nhập Xác nhận mật khẩu"` (không `!`) | Đồng nhất UC252: `"Vui lòng nhập lại mật khẩu!"` hoặc chuẩn hóa 1 message duy nhất | CROSS_UC_PARITY | `BA Confirm` |
| P2-04 | UC253 | §2.2 #5 MK mới, L66 — Error để trống | `"Vui lòng nhập Mật khẩu mới"` (không `!`) | `"Vui lòng nhập Mật khẩu mới!"` (đồng nhất UC252) | CROSS_UC_PARITY | `BA Confirm` |
| P2-05 | UC253 | §2.2 #6 Nhập lại MK, L67 — Error để trống | `"Vui lòng nhập lại mật khẩu"` (không `!`) | `"Vui lòng nhập lại mật khẩu!"` (đồng nhất UC252) | CROSS_UC_PARITY | `BA Confirm` |
| P2-06 | UC253 | §2.2 #6, L67 — Error không khớp | `"Mật khẩu nhập lại không khớp. Vui lòng kiểm tra lại"` | `"Mật khẩu không trùng khớp"` (đồng nhất UC251 L46 + UC252 L82) | CROSS_UC_PARITY | `BA Confirm` |

### 1.3 Trường: Email

| ID | UC | Vị trí | Current | Target | Loại | Status |
|---|---|---|---|---|---|---|
| P3-01 | UC250 | §2.2 Edit — Email người ĐD, L138 — Error để trống | `"Vui lòng nhập Email"` | `"Vui lòng nhập địa chỉ email"` (đồng nhất UC250 L125 + UC249) | INTRA_DOC + CROSS_UC | `Pending` |

### 1.4 Trường: Datepicker (CMR-09/H02)

| ID | UC | Vị trí | Current | Target | Loại | Status |
|---|---|---|---|---|---|---|
| P4-01 | UC250 | §2.2 Edit — Ngày sinh NĐD, L133 | `"Vui lòng nhập ngày sinh"` | `"Vui lòng chọn ngày sinh"` (CMR-09/H02: datepicker → "chọn") | CMR_CONFLICT | `Pending` |
| P4-02 | UC250 | §2.2 Edit — Ngày cấp NĐD, L135 | `"Vui lòng nhập ngày cấp"` | `"Vui lòng chọn ngày cấp"` (CMR-09/H02) | CMR_CONFLICT | `Pending` |

### 1.5 Toast Account Lockout

| ID | UC | Vị trí | Current | Target | Loại | Status |
|---|---|---|---|---|---|---|
| P5-01 | UC256 | §3.1 Lockout, L100 | `"Tài khoản đã bị tạm khóa do nhập sai nhiều lần. Vui lòng thử lại sau 15 phút"` | — (giữ nguyên — đây là bản đầy đủ hơn) | — | ✅ Reference |
| P5-02 | UC251 | §3.1 Lockout, L59 | `"Tài khoản của bạn đã bị khóa tạm thời. Vui lòng thử lại sau 15 phút."` | Cần BA xác nhận: UC251 và UC256 có cùng flow nhưng message khác. Đề xuất đồng nhất về UC256 | CROSS_UC_PARITY | `BA Confirm` |

---

## PASS 2 — Intra-Document Conflicts (Body ↔ AC)

| ID | UC | Vị trí | Current (Body) | Current (AC) | Target | Status |
|---|---|---|---|---|---|---|
| I1-01 | UC252 | §3.1 vs AC-03 — Message lỗi trùng | §3.1: `"Email đã tồn tại"` / `"Số điện thoại đã tồn tại"` etc. | AC-03: `"Dữ liệu [tên trường] đã tồn tại"` (format template) | Sửa AC-03 thành các message cụ thể của §3.1 | `Pending` |
| I1-02 | UC256 | §3.1 vs AC-02-14 — Toast lockout | §3.1: `"...do nhập sai nhiều lần. Vui lòng thử lại sau 15 phút"` | AC-02-14: `"...đã bị tạm khóa. Vui lòng thử lại sau 15 phút."` (ngắn hơn + có dấu `.`) | Đồng nhất với §3.1, bỏ dấu `.` cuối | `BA Confirm` |
| I1-03 | UC256 | Header vs Changelog — Version | Header: `v2.12` | Changelog: kết thúc tại v2.11 (thiếu entry v2.12) | Bổ sung dòng changelog v2.11→v2.12 | `Pending` |
| I1-04 | UC256 | Bảng AC-02 — Số thứ tự | AC nhảy AC-02-2 → AC-02-4, **không có AC-02-3** | — | Bổ sung AC-02-3 hoặc renumber | `BA Confirm` |
| I1-05 | UC249 | §2.2 L95 vs AC-02-3 — Email empty error | §2.2: `"Vui lòng nhập địa chỉ email"` | AC-02-3: `"Vui lòng nhập Email"` | Cập nhật AC-02-3 → `"Vui lòng nhập địa chỉ email"` | `Pending` |
| I1-06 | UC249 | §2.2 L111 vs AC-02-5 vs §3.3 — Mã bưu chính error | §2.2: `"Mã bưu chính không hợp lệ"` | AC-02-5: `"Mã không bao gồm khoảng trắng và ký tự có dấu"` | Đồng nhất AC-02-5 → `"Mã bưu chính không hợp lệ"` | `Pending` |

---

## PASS 3 — CMR Rule H Violations (Trailing Period)

| ID | UC | Vị trí | Current (có dấu `.`) | Target (bỏ dấu `.`) | Status |
|---|---|---|---|---|---|
| H1-01 | UC252 | §3.2 — Link xác thực hết hạn, L139 | `"Link xác thực đã hết hạn, vui lòng thử lại."` | `"Link xác thực đã hết hạn, vui lòng thử lại"` | `Pending` |
| H1-02 | UC252 | §3.2 — Token không hợp lệ, L140 | `"Nội dung không tồn tại hoặc đã bị xóa."` | `"Nội dung không tồn tại hoặc đã bị xóa"` | `Pending` |
| H1-03 | UC252 | §3.2 — Email gửi thất bại, L141 | `"Không thể gửi email xác thực. Vui lòng thử lại."` | `"Không thể gửi email xác thực. Vui lòng thử lại"` | `Pending` |
| H1-04 | UC256 | AC-02-14, L208 | `"Tài khoản đã bị tạm khóa. Vui lòng thử lại sau 15 phút."` | `"Tài khoản đã bị tạm khóa. Vui lòng thử lại sau 15 phút"` | `Pending` |
| H1-05 | UC251 | §3.1 + AC-03, L59 + L76 | `"Tài khoản của bạn đã bị khóa tạm thời. Vui lòng thử lại sau 15 phút."` (2 chỗ) | Bỏ dấu `.` cuối | `Pending` |
| H1-06 | UC253 | §2.1 — Nút Gửi email, L50 | `"Đường dẫn đặt lại mật khẩu đã được gửi đến email của bạn."` | `"Đường dẫn đặt lại mật khẩu đã được gửi đến email của bạn"` | `Pending` |
| H1-07 | UC253 | §3.1 Deep link hết hạn, L80 | `"Link đặt lại mật khẩu đã hết hạn. Vui lòng thử lại."` | `"Link đặt lại mật khẩu đã hết hạn. Vui lòng thử lại"` | `Pending` |
| H1-08 | UC253 | §3.3 Case table, L95 | `"Mã định danh không tồn tại trên hệ thống."` | `"Mã định danh không tồn tại trên hệ thống"` | `Pending` |
| H1-09 | UC249 | §3.1 Error Flow, L136 | `"Phiên đăng nhập hết hạn."` | `"Phiên đăng nhập hết hạn"` | `Pending` |
| H1-10 | UC249 | §3.3 Error Flow, L170 | `"Phiên đăng nhập hết hạn."` | `"Phiên đăng nhập hết hạn"` | `Pending` |

---

## TỔNG KẾT

| Loại lỗi | Số lượng | Cần BA Confirm | Có thể fix ngay |
|---|---|---|---|
| Cross-UC Parity Conflict | 16 | 9 | 7 |
| Intra-Document Conflict | 6 | 2 | 4 |
| CMR Rule H (trailing period) | 10 | 0 | 10 |
| **TỔNG** | **32** | **11** | **21** |

### Các câu hỏi cần BA confirm ngay:

| # | Câu hỏi | UC liên quan |
|---|---|---|
| Q1 | Mã định danh Cá nhân VN: chỉ nhận 12 số (CCCD) hay cả 10 số (CMND cũ)? | UC252, UC256 |
| Q2 | Toast lockout UC251 và UC256 có cần đồng nhất không? Nếu có, chọn bản nào? | UC251, UC256 |
| Q3 | AC-02-3 trong UC256 bị missing — có phải là AC bị skip hay cần bổ sung? | UC256 |
| Q4 | Dấu `!` cuối error "Vui lòng nhập Mật khẩu": có `!` hay không? Chọn 1 chuẩn duy nhất cho tất cả UC | UC251, UC252, UC253, UC256 |
| Q5 | Message "Mật khẩu không trùng khớp" hay "Mật khẩu nhập lại không khớp. Vui lòng kiểm tra lại" — chọn 1? | UC251, UC252, UC253 |

---

## SELF-AUDIT EVIDENCE TABLE

| # | Mục kiểm tra | Chi tiết | Kết quả |
|---|---|---|---|
| SA-01 | File coverage | 6/6 UC files chính đọc đầy đủ (bỏ qua audited/backlog) | ✅ |
| SA-02 | Sibling UC parity | UC249↔UC250, UC252↔UC256, UC251↔UC252↔UC253, UC251↔UC256 | ✅ |
| SA-03 | Intra-doc (Body↔AC) | UC252 (1), UC256 (3), UC249 (2) — tổng 6 conflicts | ✅ |
| SA-04 | Error message exact-match | Diff từng message: Mã ĐD, Mật khẩu, Email, Lockout, Không khớp | ✅ |
| SA-05 | CMR Rule H sweep | Scan dấu `.` cuối tất cả toast/inline trong 6 UC — phát hiện 10 violations | ✅ |
| SA-06 | Datepicker verb check | CMR-09/H02: datepicker phải dùng "chọn". Phát hiện 2 chỗ UC250 dùng "nhập" | ✅ |
