# GLOBAL IMPACT MATRIX — Mobile SRS Compliance Audit

**Tiêu đề:** Ma trận Ảnh hưởng Toàn cục — Kiểm tra Tính nhất quán SRS Mobile
**Ngày tạo:** 2026-05-21
**Tác giả:** Antigravity Agent
**Phiên bản:** v2
**Nguồn chuẩn:** CMR_Mobile.md (v1.9), Align_CMR_Mobile_20260520.md
**Phạm vi:** 35/47 UC đã quét (Pass 1 Batch 1–5 + Global Grep Scan)
**Thay đổi so v1:** Bổ sung Cụm 4-5 (UC7-31, UC45-51, UC52, UC54-62, UC69-95, UC229-243) + phát hiện mới Searchable Dropdown thiếu CMR-03

---

## A — Button Submit/Action → Luôn Enabled (CMR-09)

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

| # | UC | Trường | Hiện tại | Cần sửa → | Mức |
|:--|:---|:---|:---|:---|:---:|
| 1-8 | UC249-256 | Các error messages | Có dấu `.` cuối | Bỏ `.` + thêm `!` | 🟡 |

---

## D — Searchable Dropdown thiếu CMR-03 (D07/D08)

**Phát hiện mới (v2):** 4 UC nhóm (UC12-31) clone từ UC2 template nhưng **thiếu** D07/D08 rules cho Searchable Dropdown.

**UC đã có D07/D08 đầy đủ:**
- ✅ UC2, UC7-11, UC40, UC41, UC42-44, UC45-51, UC53, UC54

**UC THIẾU D07/D08:**

| # | UC | Trường | Số fields |
|:--|:---|:---|:---:|
| 1 | UC12-16 | Tỉnh/Thành, Người ĐC, Người duyệt | 3 |
| 2 | UC17-21 | Tỉnh/Thành, Người ĐC, Người duyệt | 3 |
| 3 | UC22-26 | Tỉnh/Thành, Chọn khu, Người ĐC, Người duyệt | 4 |
| 4 | UC27-31 | Tỉnh/Thành, Người ĐC, Người duyệt | 3 |
| | **TỔNG** | | **13** |

---

## E — Nút "Áp dụng" Filter → Disabled (UC2)

| # | UC | Tab | Hiện tại | Cần sửa → | Mức |
|:--|:---|:---|:---|:---|:---:|
| 1 | UC2 | Tab Kinh tế | Disabled khi validation error | Luôn Enabled (CMR-09) | 🔴 |
| 2 | UC2 | Tab Xã hội | Disabled khi validation error | Luôn Enabled (CMR-09) | 🔴 |
| 3 | UC2 | Tab Môi trường | Disabled khi validation error | Luôn Enabled (CMR-09) | 🔴 |

---

## TÓM TẮT HÀNH ĐỘNG ƯU TIÊN

| # | Nhóm | Số fields | Mức |
|:--|:---|:---:|:---:|
| A | Button Submit → Luôn Enabled | 8 | 🔴 |
| B | Max Length Textbox/Textarea | 8 | 🔴 |
| C | Error format | 8 | 🟡 |
| **D** | **Searchable Dropdown thiếu CMR-03** | **13** | 🟡 |
| E | UC2 Filter Disabled | 3 | 🔴 |
| | **TỔNG** | **~40** | |

---

## NEXT STEPS

1. ✅ **Pass 1 — Full Scan:** 35/47 UC đã quét.
2. Tiếp tục quét UC còn lại (UC58, UC69, UC70, UC88-95).
3. **Pass 2 — Cross-UC Validation.**
4. **Pass 3 — Post-Pull Recheck.**
5. **Pass 4 — Executor:** Sửa hàng loạt SRS files.

---

*Tạo Impact Matrix v2 — 21/05/2026 22:38.*
*35/47 UC đã quét | ~40 findings tổng cộng*
