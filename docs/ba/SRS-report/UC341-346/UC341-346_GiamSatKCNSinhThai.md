# UC341-346: Báo cáo theo dõi, giám sát thực hiện khu công nghiệp sinh thái (khoản 1 Điều 43 Nghị định số 35/2022/NĐ-CP)

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | yen.trinh |
| **Phân hệ** | Báo cáo KKT/KCN |
| **Mẫu biểu** | Mẫu A.4 |
| **Loại báo cáo** | Định kỳ năm |
| **Phạm vi dữ liệu đầu vào** | Có phạm vi (Chọn dự án) |
| **Hình thức nộp** | Báo cáo đơn lẻ (Single report form) |
| **Cơ quan nhận** | Ban quản lý khu công nghiệp, kinh tế |
| **Đối tượng lập** | Nhà đầu tư / Tổ chức kinh tế thực hiện dự án |
| **Giao diện** | User site |
| **Ngày tạo** | 2026-04-23 |
| **Phiên bản** | 1.12 |
| **Quy tắc sinh mã báo cáo** | EZ_A4_[ID] |
| **Loại quy trình** | Quy trình 2 bước, CMCĐT_BCTK_01 |

---

## UC341-346.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo theo dõi, giám sát thực hiện khu công nghiệp sinh thái
- Chức năng cho phép Nhà đầu tư/Tổ chức kinh tế truy cập màn hình chính để theo dõi danh sách báo cáo, được nhóm theo từng Kỳ hạn báo cáo.

Ngoài phạm vi: Quy trình xét duyệt/phê duyệt báo cáo (thuộc Admin site). Quản lý cấu hình kỳ báo cáo. Nhập từ file báo cáo chi tiết (tham chiếu CF_02).

Phân quyền: Mỗi dự án chỉ có 1 Nhà đầu tư duy nhất thực hiện báo cáo. NĐT có toàn quyền: Xem, Tạo mới, Chỉnh sửa, Nộp, Xóa, In, Xuất báo cáo.

Điều kiện tiên quyết: Báo cáo này sẽ xuất hiện ở site user (Nhà đầu tư, doanh nghiệp/ tổ chức). Các doanh nghiệp sẽ nhìn thấy danh sách báo cáo.

Truy cập chức năng: Phân hệ Báo cáo → Báo cáo KKT/KCN → Báo cáo theo dõi, giám sát thực hiện KCN sinh thái

Hậu điều kiện: Hiển thị danh sách các kỳ báo cáo, cấu trúc màn hình danh sách báo cáo. Tham chiếu: CS_01.

Acceptance Criteria: Hiển thị toàn bộ các kỳ báo cáo đã được admin lập và các báo cáo mà nhà đầu tư đã nộp. Tham chiếu: CS_01.

Chức năng đáp ứng usecase số: 341, 342, 343, 344, 345, 346

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện: Periodic-single — Giao diện mẫu cho báo cáo có kỳ hạn và gửi lẻ từng báo cáo.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | | |
| 1 | Năm | YearPicker | Null | x | | Lọc danh sách theo năm báo cáo. Kết quả hiển thị ngay khi chọn. |
| 2 | Trạng thái | Multiple-selection Dropdown | Tất cả trạng thái | x | | Lọc theo trạng thái của báo cáo (Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa...). Chọn nhiều giá trị. Hiển thị kết quả ngay lập tức. Tham chiếu: CMR_03, CMR_07., CMR_16 |
| 3 | Dự án | Multiple-selection Dropdown | Tất cả dự án | x | | Lọc hiển thị báo cáo của các dự án thuộc NĐT. Chọn nhiều dự án. Hiển thị kết quả ngay lập tức. Tham chiếu: CMR_07., CMR_16 |
| 4 | Mã báo cáo, Tên dự án | Search bar | Null | x | | Search theo mã báo cáo hoặc Tên dự án. Kết quả hiển thị ngay khi nhập. Nếu không tìm thấy: hiển thị "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo / tên dự án". |
| 5 | Trạng thái kỳ | Multiple-selection Dropdown | Null | x | | Lọc theo trạng thái:Chưa tới hạn/ Trong thời hạn/ Qua kỳ báo cáo. Tham chiếu: CMR_04. Tham chiếu: CMR_16. |
| **Khung Danh sách Kỳ hạn** | | | | | | |
| 6 | Kỳ hạn báo cáo | Label | Null | | | Hiển thị tên kỳ hạn. Mặc định ở trạng thái collapse; click vào mũi tên sẽ expand ra danh sách các báo cáo của kỳ đó. Tham chiếu: CMR_08. |
| 7 | Trạng thái kỳ báo cáo | Label | Null | | | Hiển thị trạng thái kỳ theo thời gian: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| 8 | Lập báo cáo | Button | Null | | | Button chỉ hiển thị và enable khi kỳ báo cáo ở trạng thái "Trong thời hạn", và sẽ ẩn đi khi kỳ báo cáo ở trạng thái "Chưa tới hạn" và "Qua kỳ báo cáo". Tham chiếu : CMR_04 |
| 9 | Nhập từ file | Button | Null | | | Button chỉ hiển thị và enable khi kỳ báo cáo ở trạng thái "Trong thời hạn", và sẽ ẩn đi khi kỳ báo cáo ở trạng thái "Chưa tới hạn" và "Qua kỳ báo cáo". Khi click vào thì mở màn hình chọn/kéo thả file nhập từ file. Tham chiếu: CMR_04. |
| **Khung Danh sách Báo cáo** (trong mỗi kỳ) | | | | | | |
| 10 | Mã báo cáo | Label | Null | | | Hiển thị mã báo cáo do hệ thống sinh theo quy tắc. Tham chiếu: CMR_09. |
| 11 | Tên dự án | Label | Null | | | Hiển thị tên dự án. Tham chiếu: CMR_06. |
| 12 | Ngày cập nhật | Label | Null | | | Hiển thị ngày giờ thao tác gần nhất (Lưu nháp / Nộp). Định dạng: dd/MM/yyyy HH:mm. |
| 13 | Trạng thái | Label | Null | | | Trạng thái bản ghi. Tham chiếu: CMR_03. |
| 14 | Hành động | Button group | Null | | | Hiển thị các action: Nộp, Chỉnh sửa, Xem chi tiết, Xem vòng đời, In, Xuất báo cáo theo trạng thái bản ghi. Tham chiếu: UC341-346.3. |

---

### 3. Mô tả các xử lý của chức năng

- Yêu cầu hiển thị:
  - Hệ thống tự động nhóm danh sách theo Kỳ hạn báo cáo, mặc định collapse.
  - Sắp xếp báo cáo bên trong kỳ theo thứ tự từ mới → cũ.
  - Phân trang: Chọn hiển thị số kỳ báo cáo/trang. Tham chiếu: CMR_10.
- Lọc & Tìm kiếm:
  - Do là User Site, danh sách dự án ở bộ lọc chỉ hiển thị các dự án mà Nhà đầu tư đang login có thẩm quyền thực hiện.
- Ẩn/hiện Action theo kỳ:
  - [Lập báo cáo] và [Nhập từ file] bị ẩn với kỳ báo cáo chưa bắt đầu. Tham chiếu: CF_01.

---


## UC341-346.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Lập mới Báo cáo theo dõi, giám sát thực hiện khu công nghiệp sinh thái (Mẫu A.4)
- Chức năng cho phép Nhà đầu tư chọn dự án và điền biểu mẫu dài gồm 3 phần (Thông tin dự án, Tình hình thực hiện quy định, Đánh giá KCN sinh thái). Rất nhiều trường thông tin NĐT và Dự án sẽ được tự động fill từ Hệ thống QLDA nội bộ sau khi người dùng chọn Dự án.

Phân quyền: Mỗi dự án chỉ có 1 Nhà đầu tư duy nhất thực hiện báo cáo. NĐT có toàn quyền: Xem, Tạo mới, Chỉnh sửa, Nộp, Xóa, In, Xuất báo cáo.

Điều kiện tiên quyết: Chỉ những nhà đầu tư, tổ chức/ doanh nghiệp có dự án cần nộp báo cáo (được setup trong cấu hình kỳ báo cáo) thì mới có thể lập được báo cáo.

Truy cập chức năng: Màn danh sách báo cáo (UC341-346.1) → Nhấn nút [Lập báo cáo]

Hậu điều kiện: Tùy thuộc vào action người dùng chọn (Hủy / Xem / Lưu nháp / Nộp báo cáo) sẽ có cách xử lý khác nhau. Tham chiếu: CF_01.

Acceptance Criteria: Phụ thuộc vào hành vi của Nhà đầu tư:
- Người dùng chọn Lưu nháp: Tham chiếu CF_01 → Xử lý nút [Lưu nháp]
- Người dùng chọn Xem chi tiết: Tham chiếu CF_01 → Xử lý nút [Xem chi tiết]
- Người dùng chọn Nộp báo cáo: Tham chiếu CF_01 → Xử lý nút [Nộp báo cáo]
- Người dùng chọn Hủy: Tham chiếu CF_01 → Xử lý nút [Hủy]

Chức năng đáp ứng usecase số: 341, 342

---

### 2. Mô tả giao diện

**Giao diện lập báo cáo**

Giao diện: Form nhập liệu được chia làm 3 Phần chính.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **PHẦN I: CHỌN DỰ ÁN & THÔNG TIN CHUNG** | | | | | | |
| 1 | Chọn dự án | Dropdown | `-- Chọn dự án --` | x | x | Gọi API hệ thống QLDA nội bộ trả về danh sách dự án của user đang đăng nhập. Ngay khi chọn, hệ thống gọi API điền toàn bộ trường từ mục 1.1 đến 2.4.4. Tham chiếu: CMR_07. |
| **1. Thông tin về nhà đầu tư thực hiện dự án đầu tư xây dựng và kinh doanh kết cấu hạ tầng khu công nghiệp** | | | | | | Tất cả các trường dưới đây sẽ tự động fill sau khi chọn Dự án, trạng thái Disabled, không được phép sửa. Dữ liệu lấy từ API Quản lý dự án nội bộ. Trường hợp dự án có nhiều NĐT, hiển thị chuỗi danh sách NĐT phân tách bởi dấu phẩy. Tham chiếu: CMR_12. |
| 1.1 | Tên nhà đầu tư thực hiện dự án | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.2 | Mã số doanh nghiệp | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.2.1 | Tên cơ quan cấp | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.2.2 | Ngày cấp lần đầu | Date | Trống | | x | Auto-fill. Disabled. Định dạng: DD/MM/YYYY |
| 1.2.3 | Ngày điều chỉnh gần nhất | Date | Trống | | x | Auto-fill. Disabled. (Nếu không có thì để trống). Định dạng: DD/MM/YYYY |
| 1.3 | Mã số thuế | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.3.1 | Địa chỉ trụ sở | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.3.2 | Điện thoại | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.3.3 | Fax | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.3.4 | Email | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.3.5 | Website | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.3.6 | Loại hình doanh nghiệp | Text | Trống | | x | Auto-fill (Cổ phần, TNHH...). Disabled. Tham chiếu: CMR_06. |
| 1.3.7 | Địa chỉ trụ sở chính | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| **1.4 Thông tin về người đại diện theo pháp luật của nhà đầu tư/tổ chức kinh tế thực hiện dự án:** | | | | | | Chỉ hiển thị section này nếu Loại hình NĐT là Doanh nghiệp/Tổ chức. Toàn bộ tự động fill từ API, trạng thái Disabled. Tham chiếu: CMR_12. |
| 1.4.1 | Họ tên | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.4.2 | Giới tính | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.4.3 | Chức danh | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.4.4 | Ngày sinh | Date | Trống | | x | Auto-fill. Disabled. Định dạng: DD/MM/YYYY |
| 1.4.5 | Quốc tịch | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.4.6 | Số tài liệu pháp lý | Text | Trống | | x | Auto-fill (CMND/CCCD/Hộ chiếu). Disabled. Tham chiếu: CMR_06. |
| 1.4.7 | Ngày cấp tài liệu | Date | Trống | | x | Auto-fill. Disabled. Định dạng: DD/MM/YYYY |
| 1.4.8 | Nơi cấp | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.4.9 | Điện thoại di động | Number | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.4.10 | Email | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| **2. Thông tin về dự án đầu tư xây dựng và kinh doanh kết cấu hạ tầng khu công nghiệp** | | | | | | Toàn bộ tự động fill từ API, trạng thái Disabled. Tham chiếu: CMR_12. |
| 2.1 | Tên dự án | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 2.2 | Địa điểm thực hiện dự án | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 2.4.1 | Số Chủ trương đầu tư/Giấy phép đầu tư/Giấy chứng nhận đầu tư | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 2.4.2 | Tên cơ quan cấp | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 2.4.3 | Ngày cấp lần đầu | Date | Trống | | x | Auto-fill. Disabled. Định dạng: DD/MM/YYYY |
| 2.4.4 | Ngày điều chỉnh gần nhất | Date | Trống | | x | Auto-fill. Disabled. (Để trống nếu không có). Định dạng: DD/MM/YYYY |
| **2.5. Diện tích đất** | | | | | | |
| 2.5.1 | Tổng diện tích đất KCN (ha) | Number | Null | x | x | Nhập tay. Validate: Số dương. Tham chiếu: CMR_05. |
| 2.5.2 | Diện tích đất dành cho cây xanh (ha) | Number | Null | x | x | Nhập tay. Validate: Số dương. Tham chiếu: CMR_05. |
| 2.5.3 | % diện tích cây xanh | Number | `0%` | | x | Auto-calculated: `(Cột 2.5.2 / Cột 2.5.1) * 100%`. Không cho sửa. Tham chiếu: CMR_05. |
| 2.5.4 | Diện tích đất dành cho giao thông (ha) | Number | Null | x | x | Nhập tay. Validate: Số dương. Tham chiếu: CMR_05. |
| 2.5.5 | % diện tích giao thông | Number | `0%` | | x | Auto-calculated: `(Cột 2.5.4 / Cột 2.5.1) * 100%`. Không cho sửa. Tham chiếu: CMR_05. |
| 2.5.6 | Diện tích đất dành cho khu kỹ thuật (ha) | Number | Null | x | x | Nhập tay. Validate: Số dương. Tham chiếu: CMR_05. |
| 2.5.7 | % diện tích khu kỹ thuật | Number | `0%` | | x | Auto-calculated: `(Cột 2.5.6 / Cột 2.5.1) * 100%`. Không cho sửa. Tham chiếu: CMR_05. |
| 2.5.8 | Diện tích đất dành cho hạ tầng xã hội (ha) | Number | Null | x | x | Nhập tay. Validate: Số dương. Tham chiếu: CMR_05. |
| 2.5.9 | % diện tích hạ tầng xã hội | Number | `0%` | | x | Auto-calculated: `(Cột 2.5.8 / Cột 2.5.1) * 100%`. Không cho sửa. Tham chiếu: CMR_05. |
| **2.6. Các giải pháp về công trình xã hội** | | | | | | |
| 2.6.1 | Nhà ở cho người lao động | Textarea | Null | x | x | Nhập tay. Mô tả chi tiết. Tham chiếu: CMR_06. Placeholder: "Nhập Nhà ở cho người lao động". |
| 2.6.2 | Công trình dịch vụ, tiện ích công cộng | Textarea | Null | x | x | Nhập tay. Mô tả chi tiết. Placeholder: "Nhập Công trình dịch vụ, tiện ích công cộng". Tham chiếu: CMR_06. |
| **PHẦN II: Tóm tắt tình hình thực hiện quy định của pháp luật về đầu tư, doanh nghiệp, xây dựng, đất đai, bảo vệ môi trường, lao động** | | | | | | |
| II.1 | Tóm tắt tình hình thực hiện quy định của pháp luật về đầu tư, doanh nghiệp, xây dựng, đất đai, bảo vệ môi trường, lao động | Textarea | Null | x | | Nhập tay tóm tắt tình hình thực hiện các quy định pháp luật. Tham chiếu: CMR_06. Placeholder: "Nhập Tóm tắt tình hình thực hiện quy định của pháp luật về đầu tư, doanh nghiệp, xây dựng, đất đai, bảo vệ môi trường, lao động". |
| **PHẦN III: TÌNH HÌNH THỰC HIỆN KCN SINH THÁI** | | | | | | |
| **1. Tình hình thực hiện và duy trì hoạt động sử dụng hiệu quả tài nguyên và sản xuất sạch hơn** | | | | | | Tình hình thực hiện và duy trì hoạt động sử dụng hiệu quả tài nguyên và sản xuất sạch hơn |
| 1.1.1 | Tổng số doanh nghiệp trong KCN đã áp dụng RECP đến năm [N-2] | Number | Null | x | x | Nhập tay. Validate: Số nguyên dương. Tham chiếu: CMR_05. |
| 1.1.2 | Tổng số giải pháp đến năm [N-2] | Number | Null | x | x | Nhập tay. Validate: Số nguyên dương. Tham chiếu: CMR_05. |
| 1.1.3 | Tổng số DN đã áp dụng RECP trong năm [N-1] | Number | Null | x | x | Nhập tay. Validate: Số nguyên dương. Tham chiếu: CMR_05. |
| 1.1.4 | Tổng số giải pháp trong năm [N-1] | Number | Null | x | x | Nhập tay. Validate: Số nguyên dương. Tham chiếu: CMR_05. |
| 1.1.5 | Dự kiến số doanh nghiệp trong KCN có kế hoạch áp dụng RECP trong 3 năm tới [N+3] | Number | Null | x | x | Nhập tay. Validate: Số nguyên dương. Tham chiếu: CMR_05. |
| **1.2. Giải pháp tiết kiệm năng lượng** | | | | | | |
| 1.2.1 | Hệ thống quản lý năng lượng áp dụng | Text | Null | x | x | Nhập tên hệ thống. Tham chiếu: CMR_06. |
| 1.2.2 | Mức tiết kiệm năng lượng cho năm [N-1] | Label | Mức tiết kiệm năng lượng cho năm [N-1] | | x | Read-only. Hiển thị header section cho nhóm trường tiết kiệm năng lượng năm [N-1]. Không tương tác. Tham chiếu: CMR_06. |
| 1.2.3 | Điện năng tiết kiệm (kWh) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 1.2.4 | Mức tiết kiệm năng lượng từ tiết kiệm điện (%) | Number | Null | x | x | Nhập tay. Validate: Từ 0 đến 100. Ngoài khoảng → Error: "Giá trị hợp lệ trong khoảng từ 0 - 100%". Tham chiếu: CMR_05. |
| 1.2.5 | Giảm phát thải CO2 từ tiết kiệm điện (T/n) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 1.2.6 | Tiết kiệm chi phí từ tiết kiệm điện (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 1.2.7 | Lợi ích khác | Textarea | Null | x | | Nhập tay. Không bắt buộc. Placeholder: "Nhập Lợi ích khác". Tham chiếu: CMR_06. |
| 1.2.8 | Nhiên liệu khác năm [N-1] (đơn vị đo) | Text | Null | x | x | Nhập tay nhiên liệu khác có thể tiết kiệm. Tham chiếu: CMR_06. |
| **1.3. Hiệu quả thu được** | | | | | | |
| 1.3.1 | Giảm phát thải CO2 năm [N-1] (T/n) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 1.3.2 | Tiết kiệm nước năm [N-1] (m3/n) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 1.3.3 | Tiết kiệm chi phí nước (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 1.3.4 | Giảm nước thải năm [N-1] (m3/n) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 1.3.5 | Tiết kiệm chi phí nước thải (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 1.3.7 | Giảm chất thải phải xử lý thông qua: | Label | Giảm chất thải phải xử lý thông qua | | x | |
| 1.3.8 | Tái sử dụng (T/n) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 1.3.9 | Tiết kiệm chi phí tái sử dụng (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 1.3.10 | Tái chế (T/n) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 1.3.11 | Tiết kiệm chi phí tái chế (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 1.3.12 | Tiết kiệm vật liệu năm [N-1] (t/n) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 1.3.13 | Tiết kiệm chi phí vật liệu (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 1.3.14 | Tiết kiệm hóa chất năm [N-1] (t/n) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 1.3.15 | Tiết kiệm chi phí hóa chất (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 1.3.16 | Tổng chi phí tiết kiệm năm [N-1] (triệu đồng) | Number | `0` | | x | Auto-calculated = Tổng dồn tất cả các trường tiết kiệm chi phí: 1.3.16 = 1.2.6 + 1.3.3 + 1.3.5 + 1.3.9 + 1.3.11 + 1.3.13 + 1.3.15 => Tham chiếu: CMR_05 |
| **2. Tình hình thực hiện cộng sinh công nghiệp, hiệu quả thu được và các doanh nghiệp mới tham gia vào liên kết cộng sinh** | | | | | | |
| 2.1.1 | Số lượng cộng sinh đến hết năm [N-1] (mạng lưới) | Number | Null | x | | Nhập tay. Số nguyên dương. Tham chiếu: CMR_05. |
| 2.1.2 | Trao đổi yếu tố đầu vào, đầu ra phục vụ sản xuất (nguyên vật liệu, nước, năng lượng, chất thải, sản phẩm phụ, phế liệu...) | Checkbox | Bỏ chọn | x | | Người dùng tick chọn. |
| 2.1.3 | Sử dụng chung hạ tầng phục vụ sản xuất trong khu công nghiệp (không bao gồm hạ tầng kỹ thuật và xã hội dùng chung do doanh nghiệp đầu tư phát triển hạ tầng khu công nghiệp cung cấp) | Checkbox | Bỏ chọn | x | | Người dùng tick chọn. |
| 2.1.4 | Sử dụng dịch vụ hoạt động sản xuất kinh doanh trong khu công nghiệp do Cty phát triển hạ tầng hoặc bên thứ 3 cung cấp (dịch vụ đào tạo nhân viên, dịch vụ bảo dưỡng, dịch vụ cung cấp hơi, dịch vụ kho hàng, dịch vụ kho đông lạnh...) | Checkbox | Bỏ chọn | x | | Người dùng tick chọn. |
| 2.1.5 | Liên kết cộng tác giữa các doanh nghiệp trong các khu công nghiệp khác trong việc thu gom, xử lý, tái sử dụng và tái chế nguyên vật liệu, chất thải, phế liệu, thu hồi năng lượng và nhiệt dư, tái sử dụng và tuần hoàn nước | Checkbox | Bỏ chọn | x | | Người dùng tick chọn. |
| 2.1.6 | Khác | Checkbox | Bỏ chọn | x | | Người dùng tick chọn. Khi chọn, hiển thị trường 2.1.7. |
| 2.1.7 | Mô tả liên kết cộng sinh khác | Textarea | Null | x | | Hiện khi checkbox `Khác` ở 2.1.6 được chọn. Nhập mô tả. Placeholder: "Nhập Mô tả liên kết cộng sinh khác". Tham chiếu: CMR_06. |
| 2.1.8 | Số lượng cộng sinh dự kiến đến năm [N+3] | Number | Null | x | | Nhập tay. Số nguyên dương. Tham chiếu: CMR_05. |
| 2.1.9 | Mô tả mạng lưới dự kiến | Textarea | Null | x | | Nhập tay. Placeholder: "Nhập Mô tả mạng lưới dự kiến". Tham chiếu: CMR_06. |
| 2.1.10 | Hình thức thỏa thuận cộng sinh công nghiệp | Textarea | Null | x | | Nhập tay mô tả. Placeholder: "Nhập Hình thức thỏa thuận cộng sinh công nghiệp". Tham chiếu: CMR_06. |
| 2.1.11 | Upload tài liệu chứng minh | File | Null | x | | - Hiển thị place holder: "Click để upload hoặc kéo thả file Hợp đồng dân sự hoặc thỏa thuận vào đây. Định dạng hợp lệ: PDF, Word, Excel (Có thể upload tối đa 10 file, tổng dung lượng các file không vượt quá 10MB )"<br>- Rule upload và validate khi upload Tham chiếu CMR_17 |
| 2.1.13 | Các doanh nghiệp trong cùng khu công nghiệp | Dropdown | Null | x | | Cho phép chọn nhiều. Tham chiếu: CMR_07. |
| 2.1.14 | Các doanh nghiệp trong các khu công nghiệp khác nhau | Textarea | Null | x | | Cho phép nhập. Tham chiếu: CMR_06. |
| 2.1.15 | Doanh nghiệp trong khu công nghiệp và khu vực dân cư ngoài khu công nghiệp | Textarea | Null | x | | Cho phép nhập. Tham chiếu: CMR_06. |
| 2.1.16 | Hỗ trợ của nhà đầu tư hạ tầng khu công nghiệp để thực hiện cộng sinh công nghiệp | Textarea | Null | x | | Nhập tay mô tả. Placeholder: "Nhập Hỗ trợ của nhà đầu tư hạ tầng khu công nghiệp để thực hiện cộng sinh công nghiệp". Tham chiếu: CMR_06. |
| **3. Kết quả thực hiện cộng sinh công nghiệp của khu công nghiệp** | | | | | | |
| 3.1 | Tiết kiệm năng lượng cho năm [N-1] | label | Tiết kiệm năng lượng cho năm [N-1] | | x | Read-only. Hiển thị header section cho nhóm 7 dòng liền kề bên dưới: 3.2 - 3.8 |
| 3.2 | Điện năng tiết kiệm (kWh) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 3.3 | Mức tiết kiệm năng lượng (%) | Number | Null | x | x | Nhập tay. Validate: Từ 0 đến 100. Ngoài khoảng → Error: "Giá trị hợp lệ trong khoảng từ 0 - 100%". Tham chiếu: CMR_05. |
| 3.4 | Giảm phát thải CO2 từ tiết kiệm điện (T/n) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 3.5 | Tiết kiệm chi phí điện (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 3.6 | Lợi ích khác từ tiết kiệm điện | Textarea | Null | x | x | Nhập tay. Placeholder: "Nhập Lợi ích khác từ tiết kiệm điện". Tham chiếu: CMR_06. |
| 3.7 | Nhiên liệu khác năm [N-1] (Đơn vị đo) | String | Null | x | x | Nhập tay. Tham chiếu: CMR_06. |
| 3.8 | Giảm phát thải CO2 năm [N-1] (T/n) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 3.9 | Tiết kiệm nước năm [N-1] (m3/n) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 3.10 | Tiết kiệm chi phí nước (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 3.11 | Giảm nước thải năm [Năm -1] (m3/n) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 3.12 | Tiết kiệm chi phí nước thải (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 3.12a | Giảm chất thải phải xử lý thông qua | label | Giảm chất thải phải xử lý thông qua: | | x | Read-only. Hiển thị header section cho nhóm 4 dòng liền kề bên dưới |
| 3.13 | Tái sử dụng chất thải (T/n) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 3.14 | Tiết kiệm chi phí tái sử dụng (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 3.15 | Tái chế chất thải (T/n) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 3.16 | Tiết kiệm chi phí tái chế (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 3.17 | Tiết kiệm vật liệu trong năm [N-1] (t/n) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 3.18 | Tiết kiệm chi phí vật liệu (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 3.19 | Sử dụng vật liệu từ doanh nghiệp khác năm [N-1] (t/n) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 3.20 | Tiết kiệm chi phí từ sử dụng vật liệu doanh nghiệp khác (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 3.21 | Cung cấp vật liệu cho doanh nghiệp khác năm [N-1] (t/n) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 3.22 | Thu được chi phí từ cung cấp vật liệu (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 3.23 | Tiết kiệm hóa chất năm [N-1] (t/n) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 3.24 | Tiết kiệm chi phí hóa chất (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 3.25 | Tổng chi phí tiết kiệm năm [N-1] (triệu đồng) | Number | `0` | | x | Auto-calculated = Tổng dồn tất cả các trường tiết kiệm chi phí: 3.25 = 3.5 + 3.10 + 3.12 + 3.14 + 3.16 + 3.18 + 3.20 + 3.24 => Tham chiếu: CMR_05 |
| 3.26 | Chia sẻ dịch vụ/dịch vụ dùng chung trong năm [N -1] | Text | Null | x | x | Nhập tay. Tham chiếu: CMR_06. |
| 3.27 | Tiết kiệm chi phí từ chia sẻ dịch vụ (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| 3.28 | Các kết quả khác | Textarea | Null | x | x | Nhập tay. Placeholder: "Nhập Các kết quả khác". Tham chiếu: CMR_06. |
| **CÁC BUTTON** | | | | | | |
| B1 | Hủy | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]"). |
| B2 | Xem trước | Button | | | | Mở popup PDF Preview báo cáo (không rời màn Lập). Tham chiếu: CF_07.1. |
| B3 | Lưu nháp | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]"). |
| B4 | Nộp báo cáo | Button | | | | Tham chiếu: CF_01. |

---

### 3. Mô tả các xử lý của chức năng

Xử lý chung: Tham chiếu: CF_01 (Lập báo cáo), CMR_18, CMR_17, CF_04 (Xuất báo cáo), CF_05 (In).

Xử lý đặc thù biểu mẫu A.4:

- Khởi tạo màn hình: Tất cả các trường thông tin tự động (Phần I) sẽ bị Disabled và bỏ trống. Chỉ khi Nhà đầu tư chọn Dự án tại trường (1), hệ thống mới cho phép thao tác các phần còn lại. Tham chiếu: CF_01.
- Xử lý Auto-fill (Phần 1 & 2): Khi chọn Dự án, hệ thống gọi API Quản lý dự án nội bộ và điền dữ liệu tương ứng vào các trường 1.1 đến 2.4.4. Với dự án có nhiều NĐT, thông tin mục 1.1->1.3.7 sẽ gộp dưới dạng chuỗi liệt kê NĐT cách nhau bằng dấu phẩy.
- Xử lý API trả null/rỗng: Nếu API không trả về dữ liệu cho trường auto-fill, trường chuyển sang Enabled — NĐT nhập liệu thủ công. Tham chiếu: CMR_12.
- Tính toán tự động (Auto-calc): Các trường phần trăm % (2.5.3, 2.5.5, 2.5.7, 2.5.9) tự động cập nhật ngay khi nhập Tổng diện tích KCN hoặc diện tích các cấu phần nhỏ. Các trường Tổng chi phí tiết kiệm (1.3.16, 3.25) tự động cộng dồn ngay khi User thay đổi giá trị của bất kỳ khoản mục tiết kiệm chi phí nào.

---


## UC341-346.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ – Xem chi tiết, Xem vòng đời, In, Xuất báo cáo, Nộp, Chỉnh sửa
- Chức năng cho phép Nhà đầu tư thực hiện tác vụ theo trạng thái báo cáo (Lưu nháp / Yêu cầu chỉnh sửa).

Phân quyền: Mỗi dự án chỉ có 1 Nhà đầu tư duy nhất thực hiện báo cáo. NĐT có toàn quyền: Xem, Tạo mới, Chỉnh sửa, Nộp, Xóa, In, Xuất báo cáo. Hành động hiển thị theo trạng thái bản ghi. Tham chiếu: CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC341-346.1) → Cột Hành động → Chọn tác vụ tương ứng

Hậu điều kiện: Tùy thuộc action: Xem chi tiết → hiển thị full-page read-only (CF_07); Xóa → bản ghi bị xóa khỏi danh sách (CF_08); Nộp → chuyển trạng thái theo CMR_03; Chỉnh sửa → mở form chỉnh sửa (CF_03).

Chức năng đáp ứng usecase số: 343, 344, 345, 346

---

### 2. Mô tả giao diện

**Màn hình Xem chi tiết (Full-Page View Screen)**

Tham chiếu: CF_07.

- Giao diện: Form đọc (toàn bộ trường Disabled), layout giống hệt màn hình Lập báo cáo.
- Nút [Chỉnh sửa]: Chỉ hiển thị khi bản ghi ở trạng thái Lưu nháp hoặc Yêu cầu chỉnh sửa. Tham chiếu: CF_07, CMR_03.
- Nút [Hủy]: Quay về màn hình Danh sách. Không cần popup xác nhận.

**Popup Xem vòng đời (Audit Trail)**

Tham chiếu: CF_06.

**Các Button theo Action Mapping:**

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Chỉ khi Lưu nháp | Người tạo | Tham chiếu: CF_09. Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |
| 2 | Chỉnh sửa | Button | Chỉ khi Lưu nháp hoặc Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Tất cả người dùng | Khi click mở màn hình Xem chi tiết báo cáo. Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Tất cả người dùng | Khi click mở popup Vòng đời. Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_04. |
| 7 | Xóa | Button | Lưu nháp **VÀ** chưa từng nộp | Người tạo | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết: Tham chiếu: CF_07.
- Xem vòng đời: Tham chiếu: CF_06.
- In báo cáo: Tham chiếu: CF_05.
- Xuất báo cáo: Kết xuất ra file Docx. Tham chiếu: CF_04.
- Chỉnh sửa: Tham chiếu: CF_03.

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| --- | --- | --- | --- | --- | --- |
| 2026-05-07 | 1.0 → 1.1 | Bổ sung Tham chiếu | (Nhiều dòng thiếu CMR) | Bổ sung Tham chiếu: CMR_05/06/07 dựa theo Kiểu trường | Cập nhật theo yêu cầu |
| 2026-05-07 | 1.0 → 1.1 | Trường Tổng diện tích đất | Tham chiếu: CMR_08 | Tham chiếu: CMR_05 | Cập nhật theo yêu cầu |
| 2026-05-07 | 1.0 → 1.1 | Upload tài liệu chứng minh | Hỗ trợ PDF/Image... | Cập nhật rule số lượng, dung lượng file và alert thông báo lỗi | Cập nhật theo yêu cầu |
| 2026-05-07 | 1.0 → 1.1 | Quy tắc mã báo cáo | KCN_A4_[ID] | EZ_A4_[ID] | Cập nhật theo yêu cầu |
| 2026-05-07 | 1.0 → 1.1 | Dòng 1.3.15 và 3.25 | Label, Auto-calculated | Number, Auto-calculated + công thức tính và CMR_05 | Cập nhật theo yêu cầu |
| 2026-05-07 | 1.1 → 1.2 | Thuộc tính file | (Không có) | Thêm Phạm vi báo cáo: Có phạm vi (Chọn dự án) | Cập nhật theo yêu cầu |
| 2026-05-07 | 1.1 → 1.2 | Điều kiện tiên quyết | (Không có) | Thêm điều kiện ở UC341-346.1 và UC341-346.2 | Cập nhật theo yêu cầu |
| 2026-05-07 | 1.1 → 1.2 | Nút Nộp báo cáo | B2: Nộp báo cáo | B2: Nộp | Chuẩn hóa theo CMR_03 |
| 2026-05-07 | 1.1 → 1.2 | Nút Nhập từ file | Luôn enable... | Chỉ hiển thị trong thời hạn. Tham chiếu: CMR_04 | Cập nhật theo yêu cầu |
| 2026-05-07 | 1.1 → 1.2 | Tên dự án | Hiển thị tên dự án | Bổ sung tham chiếu CMR_06 | Cập nhật theo yêu cầu |
| 2026-05-07 | 1.1 → 1.2 | Trường kiểu Date | (Không có) | Bổ sung Định dạng: DD/MM/YYYY ở Ghi chú | Cập nhật theo yêu cầu |
| 2026-05-07 | 1.1 → 1.2 | % Diện tích | Label | Number, Tham chiếu CMR_05 | Cập nhật theo yêu cầu |
| 2026-05-07 | 1.2 → 1.3 | Mục 1.1 Phần III | (Có trường 1.1.1 Năm báo cáo) | Bỏ trường 1.1.1, đánh lại STT từ 1.1.1 đến 1.1.5 | Cập nhật theo yêu cầu |
| 2026-05-07 | 1.2 → 1.3 | Nhóm trường Giảm chất thải | Tái sử dụng/Tái chế gộp chung trong tên | Thêm Header phụ và rút gọn tên label, tịnh tiến STT và công thức tính 1.3.16 | Cập nhật theo yêu cầu |
| 2026-05-07 | 1.2 → 1.3 | Nút thao tác | B2: Nộp | B2: Nộp báo cáo | Cập nhật theo tham chiếu CF_01 |
| 2026-05-08 | 1.3 → 1.4 | Tên nút Submit | Nộp báo cáo (5 lần) | Nộp báo cáo | Thống nhất tên nút toàn hệ thống |
| 2026-05-18 | 1.9 → 1.10 | Bảng thuộc tính | (Không có) | Bổ sung Loại quy trình: Quy trình 2 bước, CMCĐT_BCTK_01 | Phân loại luồng quy trình theo yêu cầu |

| 2026-05-07 | 1.3 → 1.4 | CÁC BUTTON | (Chỉ có B1, B2, B3) | Thêm dòng B4: Xem chi tiết | Cập nhật theo tham chiếu CF_01 |
| 2026-05-07 | 1.4 → 1.5 | Postconditions UC341-346.1 | (Không có) | Bổ sung: Hiển thị danh sách kỳ báo cáo. Tham chiếu: CS_01 | Kết quả audit |
| 2026-05-07 | 1.4 → 1.5 | Postconditions UC341-346.2 | (Không có) | Bổ sung: Tùy thuộc action người dùng chọn. Tham chiếu: CF_01 | Kết quả audit |
| 2026-05-07 | 1.4 → 1.5 | Dòng 1.2.2 Phần III | (Không có — nhảy 1.2.1 → 1.2.3) | Thêm dòng 1.2.2: Mức tiết kiệm năng lượng cho năm [N-1] (Label) | Kết quả audit Q12 |
| 2026-05-07 | 1.4 → 1.5 | Validate % (1.2.4, 3.3) | Validate: Từ 0 đến 100 | Bổ sung Error: "Giá trị hợp lệ trong khoảng từ 0 - 100%" | Kết quả audit Q9 |
| 2026-05-07 | 1.4 → 1.5 | Checkbox 2.1.2-2.1.6 | Gộp 1 dòng, danh sách ví dụ | Tách thành 5 dòng riêng với nội dung đầy đủ | Kết quả audit Q3 |
| 2026-05-07 | 1.4 → 1.5 | Dropdown 2.1.13-2.1.15 | Gộp 1 dòng Dropdown Multiple-select | Tách thành 3 dòng: 2.1.13 (Dropdown), 2.1.14 (Textarea), 2.1.15 (Textarea) | Kết quả audit Q4 |
| 2026-05-07 | 1.4 → 1.5 | Upload 2.1.11 behavior xóa | Được phép xoá file khi đã upload | Bổ sung: Khi xóa, hệ thống bỏ block file khỏi frame upload. Không hiển thị label đếm số file. | Kết quả audit Q8 |
| 2026-05-07 | 1.5 → 1.6 | Out-of-scope | (Không có) | Bổ sung: Quy trình xét duyệt (Admin site), Cấu hình kỳ, Nhập từ file chi tiết (CF_02) | Nâng điểm audit |
| 2026-05-07 | 1.5 → 1.6 | Phân quyền (3 sub-UC) | Tham chiếu: CMR_02 | Mỗi dự án chỉ có 1 NĐT duy nhất. Toàn quyền thao tác | BA confirm loại dự án |
| 2026-05-07 | 1.5 → 1.6 | Postconditions UC341-346.3 | (Không có) | Bổ sung: Xem chi tiết → CF_07; Xóa → CF_08; Nộp → CMR_03; Chỉnh sửa → CF_03 | Nâng điểm audit |
| 2026-05-07 | 1.5 → 1.6 | Behavior 1.2.2 | Không chỉnh sửa | Read-only. Hiển thị header section nhóm trường tiết kiệm năng lượng | Nâng điểm audit |
| 2026-05-07 | 1.5 → 1.6 | Exception API null | (Không có) | Nếu API trả null → trường Enabled, NĐT nhập tay. Tham chiếu: CMR_12 | Nâng điểm audit |
| 2026-05-07 | 1.5 → 1.6 | AC tường minh (.1, .2) | (Không có) | Bổ sung AC cho UC341-346.1 (CS_01) và UC341-346.2 (CF_01 theo từng action) | Nâng điểm audit |
| 2026-05-07 | 1.6 → 1.7 | Thuộc tính chung | Phạm vi báo cáo | Phạm vi dữ liệu đầu vào | Thay đổi tên thuộc tính theo yêu cầu |
| 2026-05-07 | 1.6 → 1.7 | Khung lọc & tìm kiếm | Kỳ báo cáo (Dropdown) | Năm (YearPicker) | Cập nhật điều kiện lọc theo yêu cầu |
| 2026-05-08 | 1.7 → 1.8 | Tính năng Xem vòng đời | N/A | Xác nhận sử dụng Tham chiếu CF_06 không cần mô tả chi tiết | Cập nhật theo Implementation Plan |
| 2026-05-11 | +1 | Tên cột | `Ngày cập nhật / Nộp` | `Ngày cập nhật` | Đồng bộ tên cột theo CS_02 (INS-03) |
| 2026-05-11 | +1 | Điều kiện hiển thị nút | `Luôn hiển thị` | `Tất cả trạng thái` | Chuẩn hóa điều kiện (INS-07) |
| 2026-05-11 | +1 | Dòng phân cách Markdown | Sai số cột | 6 cột đúng | Sửa lỗi Markdown (INS-05) |
| 2026-05-17 | 1.8 → 1.9 | Upload tài liệu chứng minh | Nội dung rule cấu hình upload riêng lẻ (tối đa 5 file) | Thay bằng Placeholder và Tham chiếu CMR_17 (tối đa 10 file) | Cập nhật theo yêu cầu hệ thống |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao / ten du an | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (2 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them , CMR_18 vao tham chieu CF_01 tren man hinh lap bao cao | Tuan thu CMR_18 Tab Navigation (STD-07) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_17 (Upload File Dinh kem) | Chua co CMR_17 | Them CMR_17 vao tham chieu man hinh Lap bao cao | UC co chuc nang upload file dinh kem (CMR_17) |
| 2026-05-17 | CMR v2.0 | STD-01 Them CMR_16 vao filter dropdown rows (1 dong) | Chua co CMR_16 | Them tham chieu CMR_16 | Filter phai co Tat ca default |
| 2026-05-17 | CMR v2.0 | STD-04a Placeholder text/numeric (10 truong) | Nhap du lieu | Nhap [ten truong cu the] | CMR_06 STD-04a |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-21 | 1.10 → 1.11 | Thêm nhãn và chuẩn hóa tên trường | (Nhiều trường thông tin cũ) | Thêm các nhãn 3.1, 3.12a và chuẩn hóa tên các cột theo yêu cầu đã duyệt | Cập nhật và chuẩn hóa theo yêu cầu người dùng |
| 2026-05-23 | 1.11 → 1.12 | Dòng 1 (Chọn dự án), cột Ghi chú | Tham chiếu: CF_01, CMR_04. Tham chiếu: CMR_07. | Tham chiếu: CMR_07. | Bỏ tham chiếu CF_01, CMR_04 theo yêu cầu |
| 2026-05-23 | 1.11 → 1.12 | Dòng 1.1 → 2.4.4 (28 dòng), cột Ghi chú | (Không có ghi chú placeholder) | Thêm "Không hiển thị placeholder." vào đầu cột Ghi chú | Cập nhật theo yêu cầu |
| 2026-05-23 | 1.11 → 1.12 | Dòng 1.4.9 (Điện thoại di động), Kiểu trường | Text | Number | Cập nhật theo yêu cầu |
