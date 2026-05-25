# UC Readiness Review
**Functional / Black-box Test Readiness Report**

**Tiêu đề:** Báo cáo kiểm định mức độ sẵn sàng của tài liệu UC2 — Tra cứu thông tin Khu công nghiệp / Khu kinh tế trên Mobile
**Ngày tạo:** 2026-05-10
**Người thực hiện:** Antigravity (Agent)
**Phiên bản:** v1

---

## Feature Brief

Tài liệu UC2 mô tả chức năng tra cứu thông tin Khu công nghiệp (KCN) và Khu kinh tế (KKT) trên ứng dụng di động. Người dùng đã đăng nhập có thể xem danh sách các loại khu (KCN, KCN sinh thái, KKT, v.v.), tìm kiếm gần đúng, lọc theo nhiều tiêu chí (tỉnh thành, diện tích, trạng thái) và xem chi tiết thông tin qua 12 tab dữ liệu (Hồ sơ, Khối lượng, Kinh tế, Xã hội, Môi trường, Dự án đầu tư, Lịch sử cập nhật, v.v.). Tài liệu tuân thủ quy tắc "Three-Tier Rule" (Hiển thị / Hành động / Validation) và tích hợp sâu các quy tắc chung (CMR) về xử lý lỗi, lazy load, pull-to-refresh, và đa ngôn ngữ.

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `98.2 / 100` | ✅ **READY** |

> **Nhận xét:** Tài liệu cực kỳ chi tiết, cấu trúc rõ ràng và tuân thủ các quy chuẩn của dự án Mobile. QA có thể bắt đầu thiết kế test case ngay lập tức. Một vài điểm mâu thuẫn nhỏ giữa Wireframe và Tài liệu cần được làm rõ để đảm bảo tính đồng nhất tuyệt đối.

---

## 📊 Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
| -- | ----------------------------------------- | ------- | ----- | ---------- |
| 1 | Feature Identity | 5 | 5/5 | ✅ Complete |
| 2 | Objective & Scope | 5 | 5/5 | ✅ Complete |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ Complete |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ Complete |
| 5 | UI Object Inventory & Mapping | 15 | 15/15 | ✅ Complete |
| 6 | Object Attributes & Behavior Definition | 20 | 18/20 | ⚡ Partial |
| 7 | Functional Logic & Workflow Decomposition | 20 | 20/20 | ✅ Complete |
| 8 | Functional Integration Analysis | 10 | 10/10 | ✅ Complete |
| 9 | Acceptance Criteria | 10 | 10/10 | ✅ Complete |
| 10 | Non-functional Requirements | 5 | 5/5 | ✅ Complete |
| **Total** | | **110** | **108/110** | **98.2/100** |

---

## 📋 Unified Gap & Question Report (Báo cáo Lỗ hổng & Câu hỏi)

| ID | Priority | Ref | Question | Why It Matters | Status |
| -- | -------- | --- | -------- | -------------- | ------ |
| Q1 | Medium | §2.2 - Nút Filter | Wireframe hiển thị trường lọc là "Lĩnh vực kinh doanh", nhưng UC mô tả là "Loại hình khu". Cần xác nhận tên trường đúng. | Đảm bảo UI khớp với Spec và thiết kế. | Open |
| Q2 | Medium | §2.2 - Diện tích từ/đến | UC quy định "Block các ký tự '.' và '-'" (chỉ cho nhập số nguyên), nhưng CMR-11 và thực tế diện tích (ha) thường có phần thập phân. | Ảnh hưởng đến validation và nhập liệu của người dùng. | Open |
| Q3 | Low | §2.2 - Giao diện | Hành vi của nút Back vật lý (Android) khi đang mở Bottom Sheet bộ lọc hoặc Drawer chi tiết? | UX nhất quán trên Android. | Open |
| Q4 | Low | §2.3.1 - Tab Hồ sơ | "Tên Tiếng Anh" có thay đổi theo cài đặt ngôn ngữ ứng dụng không, hay luôn hiển thị text gốc? | Clarify phạm vi CMR-17 (i18n). | Open |

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC2 | Tra cứu thông tin KCN/KKT trên Mobile | v3 | Finalized |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| han.luong | — | 2026-04-29 | 2026-05-10 |

---

## 1. Objective & Scope

### 1.1 Objective
Cung cấp công cụ tra cứu thông tin đa chiều về các Khu công nghiệp và Khu kinh tế cho người dùng cá nhân/tổ chức trên thiết bị di động, phục vụ nhu cầu khai thác dữ liệu pháp lý, kinh tế, xã hội và dự án đầu tư.

### 1.2 In Scope
- Xem danh sách các loại khu (Menu Grid).
- Tìm kiếm gần đúng theo tên khu (Debounce 3s).
- Bộ lọc tìm kiếm theo Tỉnh thành, Loại hình, Diện tích, Trạng thái.
- Xem chi tiết KCN/KKT với 12 tab thông tin.
- Xem Drawer chi tiết dự án đầu tư và Drawer chi tiết cập nhật.
- Tải/Xem file đính kèm (CMR-08).
- Bản đồ vị trí và chỉ đường (Tab Địa điểm).

### 1.3 Out of Scope
- Chỉnh sửa thông tin KCN/KKT (Mobile chỉ Read-only).
- Đăng ký/Tạo mới KCN/KKT.
- Các chức năng không yêu cầu đăng nhập (Public access).

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|-------|------|-------------------|
| Cá nhân / Tổ chức | Primary | Đã đăng nhập hệ thống. Có quyền xem và tra cứu toàn bộ thông tin KCN/KKT. |

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
- Người dùng đã đăng nhập thành công vào ứng dụng Mobile.
- Thiết bị có kết nối mạng (Internet).
- Có dữ liệu KCN/KKT trong hệ thống.

### 3.2 Postconditions
| After completing... | System state / Postcondition |
|--------------------|------------------------------|
| Xem chi tiết | Hệ thống ghi nhận lượt truy cập (nếu có tracking). |
| Quay lại từ Chi tiết | Trạng thái tìm kiếm/lọc và vị trí cuộn trang được giữ nguyên (State persistence). |

---

## 4. UI Object Inventory & Mapping

| Category | Component Name | Description & Constraints |
|----------|----------------|---------------------------|
| **Data Display Structure** | Card List | Danh sách cuộn dọc, 20 bản ghi/lần (Lazy load). Sắp xếp mặc định A-Z theo tên. Empty state: "Không có dữ liệu." |
| **Control System** | Search Bar | Max 500 ký tự. Debounce 3s. Placeholder gợi ý theo loại khu. |
| **Navigation & Actions** | Tab Navigation | 12 tab, hỗ trợ scroll ngang, sticky header. |
| **Other Components** | Bottom Sheet Filter | Mở từ dưới lên. Chứa các dropdown searchable và input số. |

---

## 5. Object Attributes & Behavior Definition

| Object / Component | System States | Interaction Matrix | Object Behavior (Data/State Change Context) |
|--------------------|---------------|--------------------|---------------------------------------------|
| Nút Áp dụng (Filter) | Disabled nếu "Diện tích đến" < "Diện tích từ". | Tap: Đóng sheet, reload danh sách. | Chuyển sang Enabled khi validation hợp lệ. |
| Card KCN/KKT | Enabled. | Tap: Mở màn chi tiết. | Debounce double-tap để tránh mở 2 lần. |
| Badge Trạng thái | Read-only. | N/A | Màu sắc thay đổi theo trạng thái (Xanh/Vàng/Đỏ/Xám) theo CMR-05. |
| File đính kèm | Enabled. | Tap: Mở viewer hoặc Download. | Hiển thị thông báo "Định dạng không hỗ trợ" nếu không xem được trực tiếp. |

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Function Name: Tra cứu danh sách & Tìm kiếm

**A. Workflows**
| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | Người dùng | Nhập từ khóa search | Hệ thống đợi 3s (debounce) rồi gọi API. | Xóa từ khóa: Hiển thị lại toàn bộ danh sách. | Lỗi mạng: Hiển thị "Không thể kết nối" + nút Thử lại. |
| 2 | Người dùng | Cuộn xuống cuối | Hệ thống tự động tải thêm 20 bản ghi tiếp theo. | Hết dữ liệu: Ẩn loading indicator. | API Timeout (>10s): Thông báo "Yêu cầu hết thời gian chờ". |

**B. Business Rules & Validations**
| Field / Object | Required | Format / Constraint | Min / Max | Error Message *(exact text)* |
|----------------|----------|---------------------|-----------|-------------------------------|
| Ô tìm kiếm | No | Chứa từ khóa | 0 / 500 | N/A |
| Diện tích đến | No | Số nguyên dương | >= Diện tích từ | "Diện tích (Đến) phải lớn hơn Diện tích (Từ)" |

---

## 7. Functional Integration Analysis

| Trigger Function / Action | Impact Analysis (Cross-function influence) | Data Consistency Verification |
|---------------------------|--------------------------------------------|-------------------------------|
| Đổi ngôn ngữ (CMR-17) | Toàn bộ text cứng (label, tab, toast) thay đổi ngay lập tức. | Kiểm tra các tab chi tiết vẫn hiển thị đúng tiêu đề ngôn ngữ mới. |
| Quay lại từ Chi tiết | Ảnh hưởng đến trải nghiệm người dùng. | Kiểm tra keyword search và filter cũ vẫn được giữ nguyên trên màn danh sách. |

---

## 8. Acceptance Criteria

| AC # | Scenario | Given | When | Then |
|------|----------|-------|------|------|
| AC-01 | Tìm kiếm chính xác | Người dùng ở màn danh sách. | Nhập tên KCN cụ thể. | Sau 3s, danh sách chỉ hiển thị các KCN có tên chứa từ khóa đó. |
| AC-02 | Lazy load hoạt động | Danh sách có > 20 bản ghi. | Cuộn xuống cuối trang. | Loading indicator xuất hiện và 20 bản ghi tiếp theo được nạp vào. |
| AC-03 | Validation diện tích | Đang mở bộ lọc. | Nhập "Diện tích đến" < "Diện tích từ". | Nút Áp dụng bị disable, thông báo lỗi đỏ hiển thị dưới trường nhập. |

---

## 9. Non-functional Requirements

| Category | Requirement | Source / Reference |
|----------|-------------|-------------------|
| Hiệu năng | API phản hồi tối đa 10 giây. | CMR-16 |
| UX | Debounce navigation cho các hành động quan trọng. | CMR-18 |
| Đa ngôn ngữ | Hỗ trợ 5 ngôn ngữ cho text cứng. | CMR-17 |

---

## 10. Open Questions & Dependencies

### 10.1 Open Questions
*(Xem bảng Unified Gap & Question Report ở đầu tài liệu)*

### 10.2 Dependencies
- **Auth Service**: Để kiểm tra trạng thái đăng nhập.
- **Catalog API**: Để lấy danh mục Tỉnh thành, Loại hình.
- **KCN/KKT API**: Để lấy dữ liệu danh sách và chi tiết.

---

## 11. Change Log

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| v1 | 2026-05-10 | Antigravity | Khởi tạo báo cáo audit cho UC2 v3. |

---
*UC Readiness Template v3.0 — For QA Test Design*
