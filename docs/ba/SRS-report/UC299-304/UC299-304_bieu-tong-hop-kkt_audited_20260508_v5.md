# Đánh Giá Mức Độ Sẵn Sàng (UC Readiness Review)
**Mẫu Đánh Giá Mức Độ Sẵn Sàng Kiểm Thử Chức Năng / Hộp Đen**

---

## Tóm tắt tính năng (Feature Brief)
Tính năng này cho phép Cán bộ chuyên môn Ban Quản lý khu xem danh sách và lập "Biểu tổng hợp tình hình xây dựng và phát triển các KKT (2111.H.QLKKT)" định kỳ theo Quý/Năm. Báo cáo này là báo cáo đơn lẻ, gồm màn hình hiển thị danh sách dạng collapsible theo kỳ hạn và màn hình lập báo cáo dưới dạng lưới (grid) gồm 20 cột, cho phép nhập thông tin của nhiều dự án/khu chức năng trong KKT. Người dùng có thể thực hiện các thao tác Lập, Nháp, Chỉnh sửa, Xem chi tiết, In, Kết xuất và Nộp báo cáo cho Cục Đầu tư nước ngoài.

---

## Kết quả Đánh Giá (Readiness Verdict)

| Điểm Tổng | Kết quả |
| ------------- | ------- |
| `95.4 / 100` | [✅ READY] |

---

## 0. Thông tin Tài liệu (Document Metadata)

| UC-ID | Tên tính năng | Phiên bản | Trạng thái |
|-------|-------------|---------|--------|
| UC299-304 | Báo cáo Biểu tổng hợp KKT | 1.4 | Finalized |

| Tác giả / BA | Người duyệt | Ngày tạo | Lần cập nhật cuối |
|-------------|-------------|--------------|--------------|
| Yen.trinh | Chưa rõ | 2026-04-22 | 2026-05-08 |

---

## 1. Mục tiêu & Phạm vi (Objective & Scope)

### 1.1 Mục tiêu
Tính năng hỗ trợ Cán bộ chuyên môn Ban Quản lý khu nộp Báo cáo định kỳ (Quý / Năm) Tình hình thu hút dự án đầu tư xây dựng và kinh doanh kết cấu hạ tầng trong khu kinh tế lũy kế đến cuối kỳ báo cáo.

### 1.2 Trong phạm vi (In Scope)
- UC299-304.1: Xem Danh Sách Báo Cáo
- UC299-304.2: Lập Báo Cáo (Dạng Bảng)
- UC299-304.3: Các Tác Vụ Bổ Trợ (Nộp, Chỉnh sửa, Xem chi tiết, Xem vòng đời, In, Kết xuất, Xóa)

### 1.3 Ngoài phạm vi (Out of Scope)
- Các dự án đầu tư xây dựng và kinh doanh kết cấu hạ tầng trong KCN, KCX.
- Phê duyệt báo cáo.

---

## 2. Tác nhân & Các bên liên quan (Actors & Stakeholders)

| Tác nhân | Loại | Vai trò & Quyền hạn |
|-------|------|-------------------|
| Cán bộ chuyên môn Ban Quản lý khu | Primary | Xem danh sách, lập mới báo cáo, sửa, xem, nộp báo cáo, in, export, xóa các báo cáo chưa nộp. (Phân quyền config trong Kỳ báo cáo) |
| Nhà đầu tư, tổ chức kinh tế | User | Xem danh sách báo cáo hiển thị ở site user. |
| Cục Đầu tư nước ngoài | Secondary | Đơn vị tiếp nhận báo cáo. |

---

## 3. Điều kiện tiên quyết & Hậu điều kiện (Preconditions & Postconditions)

### 3.1 Điều kiện tiên quyết
- Xem danh sách báo cáo: Admin hệ thống đã phải setup cấu hình Kỳ báo cáo (nếu chưa setup, danh sách sẽ hiển thị trống).
- Lập báo cáo: Hệ thống đã có sẵn Master Data về KKT, Dự án, NĐT để autofill. Đối tượng được phép lập báo cáo phải được config trong Kỳ báo cáo.
- Tài khoản thao tác phải có quyền tương ứng (role Cán bộ chuyên môn Ban quản lý hoặc role được config).

### 3.2 Hậu điều kiện
| Sau khi hoàn thành... | Trạng thái hệ thống |
|--------------------|------------------------------|
| Lập báo cáo (Lưu nháp) | Báo cáo được tạo ở trạng thái "Lưu nháp", hiển thị ở bảng báo cáo trong kỳ. |
| Nộp báo cáo | Báo cáo được chuyển trạng thái sang "Đã tiếp nhận" hoặc "Chờ duyệt", hiển thị ở danh sách. |

---

## 4. Kiểm kê đối tượng UI & Mapping (UI Object Inventory & Mapping)

*(Danh sách chi tiết 38 UI elements như ở bản v1. Bảng dữ liệu có tổng 20 cột, nút thao tác đã cập nhật tên thành Nộp báo cáo. Bỏ qua liệt kê lại toàn bộ bảng để tiết kiệm không gian).*

---

## 5. Thuộc tính & Định nghĩa Hành vi Đối tượng (Object Attributes & Behavior Definition)

| Đối tượng / Component | Trạng thái hệ thống | Ma trận Tương tác | Hành vi đối tượng (Data/State Change) |
|--------------------|---------------|--------------------|---------------------------------------------|
| Tên dự án/khu chức năng | Disabled mặc định, Enabled khi chọn KKT | Click chọn giá trị | Chọn xong gọi API tự điền Cột 5, 13, 14, 15, 16. |
| NĐT xây dựng... | Enabled | Chọn nhiều giá trị | Gọi API tự điền Cột 8 (Quốc tịch NĐT). |
| Dòng tổng | Disabled, tự tính toán | Không có | Tự động tính tổng của các cột 10 đến 20. |
| Nút "Thêm/Xóa dòng" | Theo CMR_15 | Click | Thêm/xóa dòng báo cáo, dòng tổng tự động cập nhật lại. |
| Nút "Lưu nháp" | Luôn Enabled | Click | Không validate định dạng hay bắt buộc; chỉ cần ít nhất 1 thông tin có dữ liệu là được lưu nháp. |
| Nút "Nộp báo cáo" | Luôn Enabled | Click | Kiểm tra bắt buộc tất cả các trường theo quy tắc; hiển thị lỗi inline đỏ nếu thiếu. Tham chiếu: CMR_18. |

---

## 6. Logic chức năng & Phân rã luồng công việc (Functional Logic & Workflow Decomposition)

### 6.1 Lập Báo Cáo & Nộp Báo Cáo

**A. Workflows**
| Bước | Tác nhân | Hành động | Phản hồi hệ thống (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | CB BQL Khu | Nhấn "Lập báo cáo" | Mở form nhập liệu với 1 dòng trống. | N/A | N/A |
| 2 | CB BQL Khu | Nhập thông tin, nhấn "Nộp báo cáo" | Validate OK, chuyển trạng thái "Đã tiếp nhận" / "Chờ duyệt", toast báo thành công. | Click "Lưu nháp": báo cáo chuyển trạng thái Lưu nháp. | Thiếu thông tin bắt buộc: hiển thị lỗi inline đỏ "Trường bắt buộc". |

**B. Business Rules & Validations**
| Trường / Đối tượng | Bắt buộc | Định dạng / Ràng buộc | Min / Max | Thông báo lỗi (exact text) |
|----------------|----------|---------------------|-----------|-------------------------------|
| Các trường số (VD: Doanh thu, Cột 10-20) | Có | Numeric, >= 0, không cho phép dấu âm ở đầu. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | - | "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy" (CMR_05) |
| Các trường Text | Có | Max 255 ký tự | 1 / 255 | "Vui lòng nhập [tên trường]" (nếu để trống) |
| KKT | Có | Enum / Master data | - | "Vui lòng chọn [tên trường]" |

**C. UI/UX Feedback**
* **Loading States:** Mặc định của trình duyệt / hệ thống khi call API.
* **Toast Messages:** 
  - Thành công: "Đã lưu báo cáo thành công" / "Đã nộp báo cáo thành công" (CF_01).
  - Thất bại: "Không thể kết nối đến hệ thống. Vui lòng thử lại sau" (CF_01).

---

## 7. Phân tích Tích hợp Chức năng (Functional Integration Analysis)

| Hàm kích hoạt / Hành động | Đánh giá Tác động | Xác minh tính nhất quán dữ liệu |
|---------------------------|--------------------------------------------|-------------------------------|
| Chọn KKT | Enable dropdown Dự án, load data dự án | Kiểm tra dropdown Dự án hiển thị danh sách khớp với KKT đã chọn. |
| Chọn Dự án | Tự động điền dữ liệu API (Cột 5, 13-16) | Kiểm tra các cột 5, 13-16 bị disable và có dữ liệu chính xác từ IRC. |
| Chọn NĐT | Tự động điền dữ liệu API (Cột 8) | Kiểm tra cột 8 tự động load quốc tịch đúng với các NĐT đã chọn. |

---

## 8. Tiêu chí Chấp nhận (Acceptance Criteria)

| AC # | Kịch bản | Given (Điều kiện tiên quyết) | When (Hành động) | Then (Kết quả mong đợi) |
|------|----------|------------------------|----------------------|--------------------------|
| AC-01 | Lưu nháp thành công | Ở màn hình thêm mới, có nhập ít nhất 1 dữ liệu bất kỳ trên 1 dòng | Nhấn "Lưu nháp" | Toast "Đã lưu báo cáo thành công" hiển thị, báo cáo lưu trạng thái Nháp. Không cần validate trường bắt buộc. |
| AC-02 | Validate bắt buộc nộp | Bỏ trống các trường bắt buộc ở dòng 1 | Nhấn "Nộp báo cáo" | Hệ thống hiện lỗi "Trường bắt buộc" ở các ô trống, không submit. |
| AC-03 | Auto fill data IRC | Đã chọn KKT và mở list Dự án | Chọn 1 dự án | Cột Địa điểm, Vốn ĐTNN/ĐTTN đăng ký/thực hiện (13-16) tự động được điền và bị disable. |
| AC-04 | Dòng Tổng | Người dùng nhập số liệu vào Cột 10 đến 20 | Quan sát dòng Tổng cuối bảng | Hệ thống tính tổng tự động real-time, trường tự disable. |
| AC-05 | Xem danh sách khi rỗng | Admin hệ thống CHƯA setup bất kỳ Kỳ báo cáo nào | User truy cập màn hình Danh sách | Danh sách hiển thị trống, không có dữ liệu báo cáo nào. |

---

## 9. Yêu cầu Phi chức năng (Non-functional Requirements)

| Danh mục | Yêu cầu | Nguồn / Tham chiếu |
|----------|-------------|-------------------|
| NFR | *⚠️ Chưa được định nghĩa trong tài liệu gốc* | - |

---

## 10. Báo Cáo Lỗ Hổng & Tổng Hợp Câu Hỏi (Unified Gap & Question Report)

_Không có câu hỏi mở nào. Mọi câu hỏi từ phiên bản trước đã được BA giải đáp và tài liệu đã được cập nhật._

| ID | Ưu tiên | Ref | Câu hỏi | Why It Matters | Trạng thái |
|----|----------|-----|----------|----------------|--------|
| - | - | - | - | - | Resolved |

---

## Audit Summary

| #               | Knowledge Area                           | Max Pts       | Score | Status                    |
| --------------- | ---------------------------------------- | ------------- | ----- | ------------------------- |
| 1               | Feature Identity                         | 5             | 5/5   | ✅ |
| 2               | Objective & Scope                        | 5             | 5/5   | ✅ |
| 3               | Actors & User Roles                      | 10            | 10/10 | ✅ |
| 4               | Preconditions & Postconditions           | 10            | 10/10 | ✅ |
| 5               | UI Object Inventory & Mapping            | 15            | 15/15 | ✅ |
| 6               | Object Attributes & Behavior Definition  | 20            | 20/20 | ✅ |
| 7               | Functional Logic & Workflow Decomposition| 20            | 20/20 | ✅ |
| 8               | Functional Integration Analysis          | 10            | 10/10 | ✅ |
| 9               | Acceptance Criteria                      | 10            | 10/10 | ✅ |
| 10              | Non-functional Requirements              | 5             | 0/5   | ⚠️ |
| **Total**       |                                          | **110**       |       | **105/110 → 95.4/100** |

### 🟢 What's Good
Tài liệu gốc (v1.4) đã được cập nhật trọn vẹn và tích hợp đầy đủ các tiêu chuẩn hệ thống (bao gồm `CMR_15` cho quy tắc Add/Remove Row).

### 🧪 Testability Outlook

**What CAN be tested now:**
- Toàn bộ luồng tạo, lưu nháp, chỉnh sửa và nộp báo cáo.
- Các quy tắc auto-fill từ API Master Data.
- Hành vi lưới (thêm/xóa dòng) theo CMR_15.

### 📌 Summary & Recommendation
Tài liệu **ĐÃ SẴN SÀNG (READY)**. Đội QA có thể tự tin sử dụng phiên bản 1.4 này để thiết kế Kịch bản kiểm thử (Test Scenarios) và Test Cases.

---

## 11. Changelog
- **2026-05-22 (Audit v5 — Align CMR):** Áp dụng CMR alignment: (1) Numeric precision cập nhật thành "Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự)"; (2) Bổ sung tham chiếu CMR_18 (Tab Navigation) cho nút Nộp báo cáo; (3) Textbox max sửa 500→255; (4) Buttons ghi "Luôn Enabled"; (5) Loại bỏ trailing `.` khỏi toast messages.
- **2026-05-08 (Audit v4):** Thực hiện Re-Audit dựa trên bản cập nhật **v1.4** của tài liệu `UC299-304_BieuTongHopKKT.md`. Xác nhận việc chuẩn hóa quy tắc thêm/xóa hàng (tham chiếu `CMR_15`) và thống nhất tên nút [Nộp báo cáo] trên toàn bộ hệ thống đã được tích hợp đúng cách. Tài liệu giữ nguyên trạng thái READY.
- **2026-05-06 (Audit v3):** Đánh giá lại toàn bộ dựa trên bản cập nhật **v1.1** của tài liệu. Ghi nhận trạng thái hoàn thành tất cả các Gap trong Question Backlog.
