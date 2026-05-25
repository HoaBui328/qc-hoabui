# UC035-040: Báo cáo trước khi thực hiện dự án đầu tư — UC Readiness Review

| Thuộc tính | Giá trị |
|---|---|
| **Tài liệu nguồn** | UC035-040_BaoCaoTruocKhiThucHienDuAnDT_v1.4.md (v2.3) |
| **Ngày audit** | 2026-05-15 |
| **Người audit** | Claude Agent |
| **Phiên bản audit** | v2 |

---

## Section 0 — Feature Identity

| Thuộc tính | Giá trị | Status |
|---|---|---|
| UC ID | UC035-040 | ✅ Complete |
| Tên chức năng | Báo cáo trước khi thực hiện dự án đầu tư (Mẫu A.III.3) | ✅ Complete |
| Phân hệ | Quản lý đầu tư nước ngoài / đầu tư trong nước (ĐTNN/ĐTTN) | ✅ Complete |
| Loại báo cáo | Khai báo bắt buộc 1 lần, không định kỳ | ✅ Complete |
| Hình thức nộp | Báo cáo đơn lẻ | ✅ Complete |
| Cơ quan nhận | Cơ quan đăng ký đầu tư | ✅ Complete |
| Đối tượng lập | Tổ chức kinh tế (TCKT) thực hiện dự án | ✅ Complete |
| Giao diện | User site | ✅ Complete |
| Quy tắc sinh mã | FDI_AIII3_[ID] | ✅ Complete |

---

## Section 1 — Objective & Scope

**Mục tiêu:** Cho phép TCKT thực hiện dự án khai báo bắt buộc 1 lần trước khi triển khai dự án đầu tư (đối với dự án không thuộc diện cấp Giấy chứng nhận đăng ký đầu tư). Sau khi nộp thành công, không được tạo báo cáo mới cho cùng dự án.

**Phạm vi:**
- ✅ Xem danh sách báo cáo (UC035-040.1)
- ✅ Lập báo cáo — Form nhập liệu Phần I + Phần II (UC035-040.2)
- ✅ Các tác vụ bổ trợ: Nộp, Chỉnh sửa, Xem chi tiết, Xem vòng đời, In, Export, Xóa, Import (UC035-040.3)

**Status:** ✅ Complete

---

## Section 2 — Actors & User Roles

| Actor | Mô tả | Quyền | Status |
|---|---|---|---|
| TCKT phụ trách dự án | Tổ chức kinh tế thực hiện dự án | Toàn quyền: Khởi tạo, Nộp, Chỉnh sửa, Xóa, Xem, In, Export, Xem vòng đời, Import (CMR_01) | ✅ Complete |
| NĐT thành viên trong dự án | Nhà đầu tư tham gia dự án | Chỉ Xem chi tiết, In, Export, Xem vòng đời. Tooltip: "Đã được lập bởi [Tên TCKT]" (CMR_01) | ✅ Complete |

**Status:** ✅ Complete

---

## Section 3 — Preconditions & Postconditions

### Preconditions

| # | Điều kiện | Nguồn | Status |
|---|---|---|---|
| 1 | Người dùng đã đăng nhập (TCKT hoặc NĐT thành viên) | UC doc | ✅ Complete |
| 2 | Truy cập: Phân hệ Báo cáo → Quản lý ĐTNN → Báo cáo trước khi thực hiện dự án ĐT | UC doc | ✅ Complete |
| 3 | TCKT phụ trách dự án (để tạo mới) — CMR_01 | CMR_01 | ✅ Complete |
| 4 | Dự án chưa có bản ghi nộp thành công (khai báo 1 lần) | UC doc | ✅ Complete |

### Postconditions

| # | Kết quả | Trạng thái hệ thống | Status |
|---|---|---|---|
| 1 | Lưu nháp thành công | Bản ghi ở trạng thái "Lưu nháp" | ✅ Complete |
| 2 | Nộp thành công | Bản ghi chuyển sang "Chờ duyệt"/"Đã tiếp nhận". Ẩn nút [Lập báo cáo] cho dự án này | ✅ Complete |
| 3 | Xóa thành công | Bản ghi bị xóa (chỉ khi Lưu nháp VÀ chưa từng nộp) | ✅ Complete |

**Status:** ✅ Complete

---

## Section 4 — UI Object Inventory & Mapping

### 4.1. Màn hình Danh sách (UC035-040.1)

| # | Tên trường / Component | Kiểu | Required | Default | Ghi chú | Source |
|---|---|---|---|---|---|---|
| 1 | Thanh tìm kiếm | Search bar | — | Null | Tìm theo Mã báo cáo, Tên dự án. | UC #1 |
| 2 | Năm | Yearpicker + Searchable | — | Null | Lọc theo năm báo cáo | UC #2 |
| 3 | Trạng thái báo cáo | Multiple Dropdown | — | Null | Lưu nháp / Chờ duyệt / Đã tiếp nhận / YCCS | UC #4 |
| 4 | Tên dự án | Label | — | — | Tên đầy đủ dự án | UC #6 |
| 5 | Mã báo cáo | Label | — | — | Sinh theo CMR_09 | UC #7 |
| 6 | Năm báo cáo | Label | — | — | Năm nộp | UC #8 |
| 7 | Ngày gửi / Ngày cập nhật | Label | — | — | dd/MM/yyyy HH:mm | UC #9 |
| 8 | Trạng thái | Label | — | — | CMR_03. Tooltip cho NĐT thành viên | UC #10 |
| 9 | Cột Thao tác | Button group | — | — | Theo trạng thái + phân quyền | UC #11 |
| 10 | Nút Lập báo cáo | Button | — | — | Chỉ TCKT, ẩn khi đã nộp thành công | UC035-040.3 |
| 11 | Nút Import | Button | — | — | Chỉ TCKT phụ trách dự án | UC035-040.3 #8 |
| 12 | Thanh phân trang | Pagination | — | 10/trang | CMR_10 | CMR_10 |

### 4.2. Form Lập báo cáo — Đơn vị tiếp nhận

| # | Tên trường | Kiểu | Required | Default | Ghi chú | Source |
|---|---|---|---|---|---|---|
| 0 | Đơn vị tiếp nhận | Dropdown | ✓ | Null | Cơ quan đăng ký đầu tư | UC #0 |

### 4.3. Form Lập — Phần I: Thông tin về Nhà đầu tư (Dynamic Block)

| # | Tên trường | Kiểu | Required | Default | Ghi chú | Source |
|---|---|---|---|---|---|---|
| 1 | Loại nhà đầu tư | Radio | ✓ | Null | Cá nhân / Doanh nghiệp-Tổ chức | UC #1 |
| * | **[Block NĐT Cá nhân]** | | | | Hiển thị khi #1 = Cá nhân | |
| 2 | Họ tên | API Label | ✓ | Auto-fill | Disabled | UC #2 |
| 3 | Giới tính | API Label | ✓ | Auto-fill | Disabled | UC #3 |
| 4 | Ngày sinh | API Label | ✓ | Auto-fill | Disabled | UC #4 |
| 5 | Quốc tịch | API Label | ✓ | Auto-fill | Disabled | UC #5 |
| 6 | Mã số định danh cá nhân | API Label | ✓ | Auto-fill | Disabled | UC #6 |
| 7 | Địa chỉ liên hệ | API Label | ✓ | Auto-fill | Disabled | UC #7 |
| 8 | Điện thoại | API Label | ✓ | Auto-fill | Disabled | UC #8 |
| 9 | Email | API Label | ✓ | Auto-fill | Disabled | UC #9 |
| * | **[Block NĐT Doanh nghiệp]** | | | | Hiển thị khi #1 = Doanh nghiệp | |
| 10 | Tên doanh nghiệp/tổ chức | API Label | ✓ | Auto-fill | Disabled | UC #10 |
| 11 | Loại hình tổ chức kinh tế | API Label | ✓ | Auto-fill | Disabled | UC #11 |
| 12 | Địa chỉ trụ sở | API Label | ✓ | Auto-fill | Disabled | UC #12 |
| 13 | Mã số thuế | API Label | ✓ | Auto-fill | Disabled | UC #13 |
| 14 | Điện thoại | API Label | ✓ | Auto-fill | Disabled | UC #14 |
| 15 | Email | API Label | ✓ | Auto-fill | Disabled | UC #15 |
| 16 | Website | API Label | — | Auto-fill | Disabled | UC #16 |
| 17 | Vốn điều lệ | Number | ✓ | Null | VNĐ, USD (auto-calc), Tỷ giá, Ngày TG | UC #17 |
| 18 | Họ tên (Đại diện PL) | Textbox | ✓ | Null | Bắt buộc nhập | UC #18 |
| 19 | Giới tính (ĐD) | Dropdown/Radio | ✓ | Null | Nam/Nữ/Khác | UC #19 |
| 20 | Ngày sinh (ĐD) | Datepicker | ✓ | Null | — | UC #20 |
| 21 | Quốc tịch (ĐD) | Dropdown | ✓ | Null | — | UC #21 |
| 22 | Chức danh | Textbox | ✓ | Null | — | UC #22 |
| 23 | Mã số định danh cá nhân | Textbox | ✓ | Null | — | UC #23 |
| 24 | Địa chỉ liên hệ (ĐD) | Textbox | ✓ | Null | — | UC #24 |
| 25 | Điện thoại (ĐD) | Textbox | ✓ | Null | Validation SĐT | UC #25 |
| 26 | Email (ĐD) | Textbox | ✓ | Null | Validation email | UC #26 |

### 4.4. Form Lập — Phần II: Báo cáo thực hiện dự án

| # | Tên trường | Kiểu | Required | Default | Ghi chú | Source |
|---|---|---|---|---|---|---|
| 001 | Tên dự án đầu tư | Textbox | ✓ | Null | — | UC #001 |
| 002 | Mục tiêu dự án | Textarea | ✓ | Null | — | UC #002 |
| 003a | Diện tích đất... | Number | — | Null | Dynamic Giai đoạn | UC #003a |
| 003b | Diện tích đất phù hợp QH | Number | — | Null | Dynamic Giai đoạn | UC #003b |
| 003c | Công suất thiết kế | Textbox | — | Null | Dynamic Giai đoạn | UC #003c |
| 003d | Sản phẩm, dịch vụ | Textarea | — | Null | Dynamic Giai đoạn | UC #003d |
| 003e | Quy mô kiến trúc XD dự kiến | Textarea | — | Null | Dynamic Giai đoạn | UC #003e |
| 003f | Checkbox mục tiêu nhà ở | Checkbox | — | Unchecked | Trigger Conditional | UC #003f |
| 003g | Diện tích đất xây dựng | Number | — | Null | Khi 003f = Checked | UC #003g |
| ... | (Các trường 003h-003n) | | | | Khi 003f = Checked | UC #003h-n |
| 004 | Địa điểm thực hiện dự án | Textarea | ✓ | Null | — | UC #004 |
| 005 | Diện tích mặt đất, mặt nước | Number | — | Null | (nếu có) | UC #005 |
| 006 | Tổng vốn đầu tư | Number | ✓ | Null | VNĐ, USD, Tỷ giá, Ngày TG | UC #006 |
| 007 | Thời hạn hoạt động | Textbox/Date | ✓ | Null | Số năm, Ngày bắt đầu | UC #007 |
| 008a | Vốn góp của nhà đầu tư | Number | ✓ | Null | VNĐ, USD, Tỷ giá, Ngày TG | UC #008a |
| 008a2 | Vốn huy động | Number | ✓ | Null | VNĐ, USD | UC #008a2 |
| 008b | Tiến độ xây dựng cơ bản | Textarea | — | Null | (nếu có) | UC #008b |
| 008c | Phân kỳ đầu tư | Textarea | — | Null | Auto-sinh theo số lượng Giai đoạn (003) | UC #008c |
| 009a | Doanh thu | Number | ✓ | Null | — | UC #009a |
| 009b | Giá trị xuất nhập khẩu | Number | ✓ | Null | — | UC #009b |
| 009c | Lợi nhuận | Number | ✓ | Null | — | UC #009c |
| 010a | Tổng số lao động | Number | ✓ | Null | — | UC #010a |
| 010b | Mức thu nhập bình quân | Number | ✓ | Null | — | UC #010b |
| 011 | Khó khăn và kiến nghị | Textarea | — | Null | (nếu có) | UC #011 |

**Status:** ✅ Complete

---

## Section 5 — Object Attributes & Behavior Definition (Summary)

Tài liệu UC035-040 mô tả đầy đủ trạng thái và hành vi:
- **API Label fields (Phần I):** Đã được làm rõ trong v2.3 là **Disabled** hoàn toàn cho tất cả các trường NĐT Cá nhân (#2-9) và NĐT Doanh nghiệp (#10-16).
- **Dynamic Blocks NĐT:** Trigger theo Radio Type NĐT. Tối thiểu 1 dòng.
- **Conditional Block (#003f-003n):** Ẩn/hiện theo Checkbox. Bỏ check → xóa dữ liệu.
- **Auto-calc fields:** Vốn điều lệ USD (read-only, tính từ VNĐ/Tỷ giá). Chuyển đổi số sang chữ chỉ hỗ trợ Tiếng Việt, hiển thị lúc Xem/In.
- **Render rule (#008c):** Cascade delete rõ ràng — xóa giai đoạn → xóa Textarea 008c tương ứng, có cảnh báo nếu đã có dữ liệu.

**Status:** ✅ Complete

---

## Section 6 — Functional Logic & Workflow Decomposition

Đã thống nhất phân quyền: TCKT phụ trách dự án có quyền thực hiện tính năng Import. QA tự derive Acceptance Criteria từ các luồng quy định. Báo cáo Ad-hoc nên đã xóa các khái niệm liên quan đến "Kỳ báo cáo" và filter trạng thái kỳ. Các lỗi logic cũ (vd phân quyền Admin) đã được xử lý.

**Status:** ✅ Complete

---

## Section 7 — Functional Integration Analysis

Mối liên kết giữa Block Giai đoạn và Block 008c đã được bổ sung hành vi Xóa (Cascade delete), đảm bảo dữ liệu toàn vẹn khi thao tác người dùng. Không còn mâu thuẫn giữa việc Enabled/Disabled trường API.

**Status:** ✅ Complete

---

## Section 8 — Acceptance Criteria

QA đã xác nhận tự derive AC dựa trên đặc tả. Đặc tả đã đủ chi tiết (từ regex, auto-calc, đến behavior) để viết AC.

**Status:** ✅ Complete

---

## Section 9 — Non-functional Requirements

Đáp ứng các NFR về Format, Sort, Auto-calc, Text conversion (Tiếng Việt). Chưa có NFR tường minh về Accessibility, tuy nhiên không ảnh hưởng đến quá trình thiết kế testcase tính năng.

**Status:** ✅ Complete

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
| 10 | Non-functional Requirements | 5 | 4/5 | ✅ |
| **Total** | | **110** | **109/110** | **99.1/100** |

**Verdict: ✅ READY**

Tài liệu đã đạt trạng thái sẵn sàng để QA thiết kế Test Case (TC) và Test Scenario. Các rủi ro logic, UI data-mapping và quy tắc ràng buộc đã được làm rõ và thống nhất.

---

## Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|---|---|---|---|---|---|
*(Tất cả câu hỏi đã được trả lời và đưa vào danh sách Backlog)*

---

## Changelog v2 (Re-Audit)

- Áp dụng các thay đổi từ tài liệu gốc v2.3: Restructure hoàn toàn phần Danh sách, Phần I (NĐT) và Phần II (Mục tiêu).
- Xác nhận các thông tin API-sourced của Nhà đầu tư (Cá nhân & Tổ chức) luôn ở trạng thái Disabled.
- Xóa khái niệm "Trạng thái kỳ" do đây là báo cáo Ad-hoc một lần.
- Cập nhật quy tắc Cascade delete đối với block 008c khi xóa giai đoạn.
- Cập nhật phân quyền Import cho TCKT.
- Chốt quy tắc chuyển đổi chữ số chỉ áp dụng tiếng Việt.
