# UC Readiness Review
**Functional / Black-box Test Readiness Template**
**File được audit:** `UC70_tra-cuu-tthc_srs_20260512_v3.md`

---

## Feature Brief
Chức năng cho phép cá nhân, tổ chức (không yêu cầu đăng nhập) tìm kiếm, lọc và tra cứu thông tin chi tiết về các thủ tục hành chính. Hệ thống hiển thị danh sách thủ tục dưới dạng List Card và cung cấp màn hình chi tiết được phân rã thành 5 tab nội dung: Thông tin chung, Trình tự thực hiện, Thành phần hồ sơ, Cách thức thực hiện, và Căn cứ pháp lý.

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `85.5 / 100` | ⚡ **CONDITIONALLY READY** |

---

## 📊 Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
| --------- | ----------------------------------------- | --------- | ----- | ---------- |
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 12/15 | ⚡ |
| 6 | Object Attributes & Behavior Definition | 20 | 12/20 | ⚡ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 16/20 | ⚡ |
| 8 | Functional Integration Analysis | 10 | 10/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 9/10 | ⚡ |
| 10 | Non-functional Requirements | 5 | 5/5 | ✅ |
| **Total** | | **110** | | **94/110 → 85.5/100** |

---

## 📋 Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | Medium | *Nút "Lọc"* | Khi người dùng áp dụng bộ lọc (Lĩnh vực, Ngôn ngữ), icon bộ lọc trên giao diện có hiển thị **chấm xanh (Active filter indicator)** để báo hiệu trạng thái đang lọc theo chuẩn CMR-02 không? | Ảnh hưởng đến việc xác minh trạng thái hiển thị UI cho người dùng khi lọc dữ liệu. | Open |
| Q2 | Medium | *Nút **Tải mẫu đơn** (nếu có)* | Khi tap "Tải mẫu đơn" ở Tab Thành phần hồ sơ, ứng dụng sẽ tải trực tiếp file về thiết bị hay mở Preview trên trình duyệt theo quy định của CMR-08? Các định dạng file nào được phép tải? | Cần để chuẩn bị test data và kiểm tra quyền lưu trữ file trên từng hệ điều hành (Android/iOS). | Open |
| Q3 | Medium | *Tab Bar gồm 5 tab* | Người dùng có thể **vuốt ngang (Swipe left/right)** vùng nội dung để chuyển qua lại giữa 5 tab không, hay bắt buộc phải Tap trực tiếp vào tên tab trên header? | Ảnh hưởng đến việc thiết kế test case UI/UX (Swipe gestures support). | Open |
| Q4 | Medium | *Cuộn xuống để xem thêm (lazy load)* | Khi lazy load gặp lỗi mất mạng hoặc timeout, hệ thống có áp dụng cơ chế tự động **retry 3 lần** như quy định tại CMR-04 không, hay hiển thị lỗi ngay lập tức? | Cần thiết để tester giả lập lỗi mạng (network drop) và kiểm chứng cơ chế retry ngầm. | Open |
| Q5 | Low | *Nút **Hotline** (có icon điện thoại)* | Khi tap nút Hotline, hệ thống gọi thẳng luôn (dial) hay chỉ điều hướng sang trình gọi điện của máy (dialer) với số điện thoại được điền sẵn? | Xác định xem app có yêu cầu cấp quyền thực hiện cuộc gọi (Call Phone Permission) hay không. | Open |

---

## 🟢 What's Good
- Tài liệu tuân thủ cực kỳ tốt cấu trúc và các nguyên tắc hiển thị chung (CMR) như State Persistence (CMR-01), Partial API failure (CMR-07), Empty State (CMR-14), và Debounce Navigation (CMR-18).
- Giao diện 5 Tab chi tiết được rã luồng rõ ràng, cấu trúc dữ liệu hiển thị (các thẻ trạng thái Bản chính/Bản sao, Accordion list) được định nghĩa rất tường minh.
- Phân tích AC logic và chuẩn hóa đa ngôn ngữ theo chuẩn.

---

## 🧪 Testability Outlook

**What CAN be tested now:**
- Luồng tìm kiếm (Search) theo debounce 3 giây và auto-trim whitespace.
- Luồng lọc danh sách qua Bottom Sheet và Lazy loading 20 bản ghi.
- Hiển thị UI tĩnh của màn hình Chi tiết (các trường thông tin hiển thị, Accordion list).
- Cơ chế partial API failure và hiển thị lỗi mạng chung.

**What CANNOT be tested yet (blocked by gaps):**
- Hành vi mở rộng của Tab (vuốt ngang).
- Hành vi tương tác vật lý với file đính kèm (Quyền thiết bị, hành vi download vs view pdf).
- Edge case đứt mạng trong lúc đang Lazy Load trang thứ N.

**Suggested test focus areas (once gaps are resolved):**
- Happy path: Tìm kiếm, lọc kết hợp và xem chi tiết thủ tục.
- UI-specific checks: Giữ nguyên trạng thái (State Persistence) khi back từ màn hình chi tiết.
- Edge case tests: Xử lý chuỗi tìm kiếm siêu dài, mã HTML injection, lỗi Partial API ở Tab Cách thức thực hiện.
- Boundary & validation tests: Hiển thị trường nội dung dài bị cắt bớt (`...`).

---

## 📌 Summary & Recommendation
Tài liệu SRS UC70 đạt mức hoàn thiện rất tốt, bám sát các luồng ngoại lệ và quy tắc CMR. Điểm đánh giá đạt **85.5/100 (CONDITIONALLY READY)**. QA hoàn toàn có thể bắt tay vào thiết kế Test Case cho các luồng chính (Main Flows) và luồng hiển thị (UI). Song song với đó, vui lòng gửi 5 câu hỏi trong báo cáo Gap sang cho BA để làm rõ các hành vi tương tác phần cứng (Download file, vuốt Swipe tab, cấp quyền gọi Hotline) trước khi hoàn thiện bộ kịch bản kiểm thử.
