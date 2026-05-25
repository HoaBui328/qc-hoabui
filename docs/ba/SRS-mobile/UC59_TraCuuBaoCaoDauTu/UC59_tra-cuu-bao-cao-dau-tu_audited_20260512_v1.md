# UC Readiness Review
**Functional / Black-box Test Readiness Template**
**File được audit:** `UC59_tra-cuu-bao-cao-dau-tu_srs_20260512_v1.md`

---

## Feature Brief
Chức năng cho phép người dùng public tra cứu thông tin Báo cáo đầu tư. Giao diện bao gồm danh sách báo cáo, bộ lọc tìm kiếm theo nhiều tiêu chí, và màn hình chi tiết hiển thị số liệu nổi bật, tóm tắt nội dung cùng mục lục báo cáo. Chức năng cũng tích hợp màn hình "Thông tin cơ quan" (hiển thị profile cơ quan và liên kết đến các thủ tục, tài liệu liên quan thông qua Tab Bar).

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `90.0 / 100` | ⚡ **CONDITIONALLY READY** |

---

## 📊 Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
| --------- | ----------------------------------------- | --------- | ----- | ---------- |
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 14/15 | ⚡ |
| 6 | Object Attributes & Behavior Definition | 20 | 16/20 | ⚡ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 17/20 | ⚡ |
| 8 | Functional Integration Analysis | 10 | 9/10 | ⚡ |
| 9 | Acceptance Criteria | 10 | 9/10 | ⚡ |
| 10 | Non-functional Requirements | 5 | 5/5 | ✅ |
| **Total** | | **110** | | **100/110 → 90.9/100 (Adjusted to 90.0 cho các Gaps)** |

---

## 📋 Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | High | *Màn hình Chi tiết báo cáo* | Trên màn hình Chi tiết báo cáo có hiển thị "48 trang" và "Mục lục chính", nhưng **không thấy có nút "Tải tài liệu" (Download) hay "Xem toàn văn" (View PDF)**. Đây là thiếu sót thiết kế (Design missing) hay do logic nghiệp vụ chỉ cho xem tóm tắt và mục lục? | Đây là chức năng tra cứu cốt lõi của người dùng. Thiếu tính năng xem nội dung gốc sẽ ảnh hưởng lớn đến trải nghiệm. | Open |
| Q2 | Medium | *Chi tiết báo cáo -> Mục lục* | Tap vào các dòng trong mục "Mục lục chính" (VD: "Tr. 4") thì chỉ xem text tĩnh hay hệ thống có tự động mở màn hình đọc PDF nhảy tới đúng trang số 4? | QA cần verify behavior tương tác của các dòng list này. | Open |
| Q3 | Medium | *Thông tin cơ quan -> Tab Tài liệu* | Dropdown sắp xếp "Mới nhất >" ở góc phải màn hình Tab Tài liệu phát hành khi tap vào sẽ gồm những lựa chọn nào? (VD: Cũ nhất, Tên A-Z, Lượt xem nhiều nhất?). | Thiếu option để QA viết test case kiểm tra sắp xếp (Sorting). | Open |
| Q4 | Low | *Thông tin cơ quan -> Gọi OS Intent* | Khi thực hiện thao tác Gọi điện, Website, Bản đồ... nếu thiết bị báo lỗi không thể mở App (VD: Máy tính bảng không hỗ trợ SIM, hoặc chưa cài Google Maps), App sẽ hiển thị Toast báo lỗi cụ thể như thế nào? | Đảm bảo xử lý triệt để Exception Handling của luồng Mobile App. | Open |

---

## 🟢 What's Good
- Cấu trúc SRS trình bày xuất sắc, rõ ràng các block thông tin, layout hiển thị 3 cột số liệu động có `%` tăng trưởng.
- Quy chiếu toàn vẹn đến các luật CMR (Debounce, Lazy load riêng biệt giữa các Tab, Partial API Failure).
- Khung sườn đa màn hình phức tạp (Chi tiết kết nối đến màn Thông tin cơ quan độc lập) được xử lý liên kết mạch lạc.

---

## 🧪 Testability Outlook

**What CAN be tested now:**
- Luồng xem danh sách, cuộn lazy load, thực hiện pull to refresh.
- Hoạt động của Bottom Sheet bộ lọc (nhất là trường hợp Dropdown chọn "Năm phát hành").
- Format màu sắc/hiển thị của % tăng trưởng (Xanh lá có dấu `+` và đỏ có dấu `-`).
- Điều hướng swipe tab ở Màn hình cơ quan ban hành.

**What CANNOT be tested yet (blocked by gaps):**
- Chức năng đọc nội dung thật của báo cáo (Đang thiếu trong wireframe và yêu cầu).
- Tính năng Sort (Sắp xếp) trong danh sách tài liệu thuộc Cơ quan.

**Suggested test focus areas (once gaps are resolved):**
- Boundary Test: Tỷ lệ phần trăm có số quá lớn, định dạng tiền tệ khi string siêu dài (Ví dụ: 15.000.000.000.000 tỷ VNĐ).
- Hardware API Test: Các nút Gọi, Maps trên iOS vs Android có xử lý lỗi đồng nhất khi mở App ngoài hay không.

---

## 📌 Summary & Recommendation
SRS UC59 v1.0 đạt **90.0/100 (CONDITIONALLY READY)**. Tài liệu đã rất sát với thực tế phát triển, tuy nhiên Gaps liên quan đến nút **Đọc/Tải Báo Cáo** (Q1) là cực kỳ quan trọng đối với bản chất của tính năng "Tra cứu báo cáo". Vui lòng gửi các câu hỏi này cho BA/Design confirm để bổ sung ngay vào phiên bản v2.0.
