# GLOBAL IMPACT MATRIX — Mobile SRS Compliance Audit

**Tiêu đề:** Ma trận Ảnh hưởng Toàn cục — Kiểm tra Tính nhất quán SRS Mobile
**Ngày tạo:** 2026-05-21
**Tác giả:** Antigravity Agent
**Phiên bản:** v1
**Nguồn chuẩn:** CMR_Mobile.md (v1.9), Align_CMR_Mobile_20260520.md
**Phạm vi:** 18/47 UC đã quét (Cụm 1: UC249-253, Cụm 2: UC256/UC53/UC87/UC254-260, Cụm 3: UC1/UC2/UC40/UC41/UC42-44)

---

## A — Button Submit/Action → Luôn Enabled (CMR-09)

**Chuẩn CMR:** Tất cả nút Submit/Action (Lưu, Đăng ký, Gửi, Đăng nhập, v.v.) phải **Luôn Enabled** (CMR-09). Không có trạng thái Disabled.

| # | UC | Nút | Hiện tại | Cần sửa → | Mức |
|:--|:---|:---|:---|:---|:---:|
| 1 | UC249 | "Lưu thay đổi" | Disabled khi chưa thay đổi | Luôn Enabled | 🔴 |
| 2 | UC250 | "Lưu thay đổi" | Disabled khi chưa thay đổi | Luôn Enabled | 🔴 |
| 3 | UC251 | "Xác nhận" | Disabled khi chưa nhập | Luôn Enabled | 🔴 |
| 4 | UC252 | "Đăng ký" | Disabled khi chưa nhập đủ | Luôn Enabled | 🔴 |
| 5 | UC253 | "Gửi email" / "Xác nhận" | Disabled khi chưa nhập | Luôn Enabled | 🔴 |
| 6 | UC256 | "Đăng nhập" | Disabled khi chưa nhập | Luôn Enabled | 🔴 |
| 7 | UC53 | "Gửi phản ánh" | Disabled khi chưa nhập đủ | Luôn Enabled | 🔴 |
| 8 | UC87 | "Xem dự án phù hợp" | Disabled khi chưa chọn | Luôn Enabled | 🔴 |

---

## B — Max Length Textbox/Textarea (CMR-01/CMR-09/CMR-11)

**Chuẩn CMR:** Textbox max 255 ký tự. Textarea max 3000 ký tự. Numeric max 255 ký tự.

| # | UC | Trường | Hiện tại | Cần sửa → | Mức |
|:--|:---|:---|:---:|:---:|:---:|
| 1 | UC249 | Địa chỉ | 500 | 255 | 🔴 |
| 2 | UC250 | Địa chỉ | 500 | 255 | 🔴 |
| 3 | UC250 | Nơi cấp | 500 | 255 | 🔴 |
| 4 | UC252 | Nơi cấp | 500 | 255 | 🔴 |
| 5 | UC53 | Họ và tên | 200 | 255 | 🔴 |
| 6 | UC53 | Địa chỉ (cá nhân + tổ chức) | 500 | 255 | 🔴 |
| 7 | UC53 | Nội dung phản ánh | 10000 | 3000 | 🔴 |
| 8 | UC87 | Quy mô vốn | 500 | 255 | 🔴 |

---

## C — Error Message Format

**Chuẩn CMR:** Error message không có dấu `.` cuối. Sử dụng dấu `!` khi cần nhấn mạnh.

| # | UC | Trường | Hiện tại | Cần sửa → | Mức |
|:--|:---|:---|:---|:---|:---:|
| 1 | UC252 | "Mã định danh chỉ gồm các số 0-9." | Có dấu `.` | Bỏ `.` | 🟡 |
| 2 | UC256 | "Mã định danh chỉ gồm các số 0-9." | Có dấu `.` | Bỏ `.` | 🟡 |
| 3-8 | UC249-256 | Các error messages khác | Có dấu `.` cuối | Bỏ `.` + thêm `!` | 🟡 |

---

## D — Searchable Dropdown D07/D08 (CMR-03)

**Chuẩn CMR-03:** Dropdown Searchable phải:
- D07: Xóa hết keyword → hiển thị lại placeholder
- D08: Tap ra ngoài khi keyword trống → chọn lại "Tất cả" (filter) hoặc rỗng + validation (form)

| UC đã quét (có D07/D08) | UC chưa kiểm tra |
|:---|:---|
| UC2, UC7-11, UC40, UC41, UC42-44, UC53, UC54 | UC12-31 chưa quét |

---

## TÓM TẮT HÀNH ĐỘNG ƯU TIÊN

| Ưu tiên | Nhóm | Số fields | Ghi chú |
|:---:|:---|:---:|:---|
| 🔴 Cao | Button Submit → Luôn Enabled | 8 | UC249-256, UC53, UC87 |
| 🔴 Cao | Max Length Textbox 500→255 | 6 | UC249, UC250, UC252, UC53 |
| 🔴 Cao | Max Length Textarea 10000→3000 | 1 | UC53 |
| 🔴 Cao | Max Length Numeric 500→255 | 1 | UC87 |
| 🟡 TB | Error format | 8 | UC249-256, UC53, UC251 |
| ⏳ | D07/D08 chưa quét | ? | UC12-31 cần quét tiếp |

---

## NEXT STEPS

1. **Pass 1 tiếp tục:** Quét Cụm 4-5 (UC7-31, UC45-95, UC229-243).
2. **Pass 2:** Cross-UC validation.
3. **Pass 3:** Post-Pull Recheck.
4. **Pass 4:** Executor — sửa trực tiếp SRS files.

---

*Tạo Impact Matrix v1 — 21/05/2026 22:32.*
*18/47 UC đã quét | ~24 findings ưu tiên cao*
