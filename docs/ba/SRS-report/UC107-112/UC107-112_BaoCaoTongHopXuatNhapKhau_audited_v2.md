# UC Readiness Review
**Functional / Black-box Test Readiness Template**

**Tài liệu:** UC107-112_BaoCaoTongHopXuatNhapKhau.md (phiên bản 1.1)
**Ngày tạo:** 2026-05-06
**Phiên bản report:** v2 (Re-audit)

---

## Feature Brief

Chức năng Báo cáo tổng hợp tình hình xuất, nhập khẩu (Mẫu A.IV.8a) dành cho Cục Hải quan. Tính năng thực hiện tổng hợp dữ liệu từ hai báo cáo nguồn cấp Trung ương (Mẫu 8b - Xuất khẩu và Mẫu 8c - Nhập khẩu). Tài liệu đã được bổ sung đầy đủ các thành phần điều kiện, giao diện nút thao tác, chi tiết Popup chọn nguồn và các tiêu chí nghiệm thu chặt chẽ.

---

## 0. Feature Identity (Tiêu đề, ID, Ngữ cảnh)
- **Điểm:** 5/5
- **Đánh giá:** ✅ Clear
- **Chi tiết:** Đầy đủ thông tin định danh và quy tắc sinh mã.

## 1. Objective & Scope (Mục tiêu & Phạm vi)
- **Điểm:** 5/5
- **Đánh giá:** ✅ Clear
- **Chi tiết:** Đã bổ sung mục tiêu hỗ trợ nộp trực tuyến và xác định rõ Out of Scope (nộp trễ hạn).

## 2. Actors & User Roles (Phân quyền & Vai trò)
- **Điểm:** 10/10
- **Đánh giá:** ✅ Clear
- **Chi tiết:** Phân quyền rõ cho Cục Hải quan và Lãnh đạo duyệt.

## 3. Preconditions & Postconditions (Tiền/Hậu điều kiện)
- **Điểm:** 10/10
- **Đánh giá:** ✅ Clear
- **Chi tiết:** Đã bổ sung điều kiện về kỳ báo cáo và các hậu kỳ về Notification/Audit log.

## 4. UI Object Inventory & Mapping (Danh sách phần tử UI)
- **Điểm:** 15/15
- **Đánh giá:** ✅ Clear
- **Chi tiết:** Đã bổ sung đầy đủ các nút [Lưu nháp], [Nộp], [Hủy] và chi tiết các trường thông tin trong Popup chọn nguồn.

## 5. Object Attributes & Behavior Definition (Thuộc tính & Hành vi)
- **Điểm:** 20/20
- **Đánh giá:** ✅ Clear
- **Chi tiết:** Quy định rõ hành vi của Popup (required chọn 1 báo cáo mỗi bên) và tính chất cho phép sửa tay sau tổng hợp.

## 6. Functional Logic & Workflow Decomposition (Luồng nghiệp vụ)
- **Điểm:** 20/20
- **Đánh giá:** ✅ Clear
- **Chi tiết:** Logic tổng hợp từ các báo cáo cấp Trung ương đã được xác nhận. Luồng validate khi nộp báo cáo rõ ràng.

## 7. Functional Integration Analysis (Liên kết chức năng)
- **Điểm:** 10/10
- **Đánh giá:** ✅ Clear
- **Chi tiết:** Liên kết dữ liệu SUM từ 8b/8c theo tỉnh/TP.

## 8. Acceptance Criteria (Tiêu chí nghiệm thu)
- **Điểm:** 10/10
- **Đánh giá:** ✅ Clear
- **Chi tiết:** Đã bổ sung 6 AC bao quát toàn bộ các case quan trọng của chức năng.

## 9. Non-functional Requirements (Yêu cầu phi chức năng)
- **Điểm:** 5/5
- **Đánh giá:** ✅ Clear
- **Chi tiết:** Có yêu cầu cụ thể về Performance (< 5s) và Security/Audit.

---

## Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 15/15 | ✅ |
| 6 | Object Attributes & Behavior Definition | 20 | 20/20 | ✅ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 20/20 | ✅ |
| 8 | Functional Integration Analysis | 10 | 10/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 10/10 | ✅ |
| 10 | Non-functional Requirements | 5 | 5/5 | ✅ |
| **Total** | | **110** | **110/110** | **100/100** |

👉 **Verdict:** ✅ **READY** (Tài liệu đã hoàn thiện và đủ điều kiện thiết kế test).

---

## Unified Gap & Question Report

_(Tất cả các câu hỏi đã được giải quyết.)_

---

### 🟢 What's Good
- Quy tắc chọn nguồn tại Popup được quy định chặt chẽ (Required 1 report per list), giúp tránh sai sót dữ liệu.
- Cấu trúc tài liệu sau cập nhật rất đầy đủ và chuyên nghiệp.

### 🧪 Testability Outlook
**What CAN be tested now:**
- Kiểm thử luồng tổng hợp dữ liệu từ 2 nguồn 8b và 8c.
- Kiểm thử các ràng buộc tại Popup chọn nguồn.
- Kiểm thử khả năng chỉnh sửa dữ liệu sau khi tổng hợp.
- Kiểm thử các nút thao tác và luồng phê duyệt.

### 📌 Summary & Recommendation
Tài liệu SRS UC107-112 (v1.1) đã đạt điểm tối đa sau khi tiếp thu phản hồi của BA. **Khuyến nghị: Chuyển sang giai đoạn thiết kế kịch bản kiểm thử.**

---
## Changelog
- Bổ sung Objective, Scope, Pre/Post-conditions.
- Bổ sung Buttons (Lưu nháp, Nộp, Hủy) vào UI Inventory.
- Bổ sung chi tiết UI và Behavior cho Popup chọn nguồn.
- Bổ sung 6 Acceptance Criteria và NFR.
