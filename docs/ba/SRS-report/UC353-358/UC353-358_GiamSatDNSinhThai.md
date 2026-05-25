# UC353-358: Báo cáo theo dõi, giám sát thực hiện doanh nghiệp sinh thái (khoản 2 Điều 43 Nghị định số 35/2022/NĐ-CP)

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | yen.trinh |
| **Phân hệ** | Báo cáo KKT/KCN |
| **Mẫu biểu** | Mẫu B.4 |
| **Loại báo cáo** | Định kỳ năm |
| **Phạm vi dữ liệu đầu vào** | Có (chọn dự án) |
| **Hình thức nộp** | Báo cáo đơn lẻ (Single report form) |
| **Cơ quan nhận** | Ban quản lý khu công nghiệp, kinh tế |
| **Đối tượng lập** | Nhà đầu tư / Tổ chức kinh tế thực hiện dự án |
| **Giao diện** | User site |
| **Ngày tạo** | 2026-04-23 |
| **Phiên bản** | 1.7 |
| **Quy tắc sinh mã báo cáo** | EZ_B4_[ID] |
| **Loại quy trình** | Quy trình 2 bước, CMCĐT_BCTK_01 |

---

## UC353-358.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo theo dõi, giám sát thực hiện doanh nghiệp sinh thái
- Chức năng cho phép Nhà đầu tư/Tổ chức kinh tế truy cập màn hình chính để theo dõi danh sách báo cáo, được nhóm theo từng Kỳ hạn báo cáo.

Phân quyền: Nhà đầu tư/Tổ chức kinh tế thực hiện dự án. Tham chiếu: CMR_02.

Điều kiện tiên quyết: Báo cáo này sẽ xuất hiện ở site user (Nhà đầu tư, doanh nghiệp/ tổ chức). Các doanh nghiệp sẽ nhìn thấy danh sách báo cáo.

Hậu điều kiện: Hiển thị danh sách các kỳ báo cáo, cấu trúc màn hình danh sách báo cáo. Tham chiếu: CS_01.

Truy cập chức năng: Phân hệ Báo cáo → Báo cáo KKT/KCN → Báo cáo theo dõi, giám sát thực hiện doanh nghiệp sinh thái

Chức năng đáp ứng usecase số: 353, 354, 355, 356, 357, 358

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện: Periodic-single — Giao diện mẫu cho báo cáo có kỳ hạn và gửi lẻ từng báo cáo.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | |  |
| 1 | Năm | YearPicker | Null | x | | Lọc danh sách theo năm báo cáo. Kết quả hiển thị ngay khi chọn. |
| 2 | Trạng thái | Multiple-selection Dropdown | Tất cả trạng thái | x | | Lọc theo trạng thái báo cáo. Chọn nhiều giá trị. Tham chiếu: CMR_03, CMR_07., CMR_16 |
| 3 | Dự án | Multiple-selection Dropdown | Tất cả dự án | x | | Chỉ hiển thị dự án thuộc NĐT đang login. Chọn nhiều dự án. Tham chiếu: CMR_07., CMR_16 |
| 4 | Mã dự án, Tên dự án | Search bar | Null | x | | Search theo mã hoặc tên dự án. Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã dự án / tên dự án". |
| 5 | Trạng thái kỳ | Multiple-selection Dropdown | Null | x | | Lọc theo trạng thái:Chưa tới hạn/ Trong thời hạn/ Qua kỳ báo cáo. Tham chiếu: CMR_04. Tham chiếu: CMR_16. |
| **Khung Danh sách Kỳ hạn** | | | | | |  |
| 6 | Kỳ hạn báo cáo | Label | Null | | | Mặc định collapse; click mũi tên để expand danh sách. Tham chiếu: CMR_08. |
| 7 | Trạng thái kỳ báo cáo | Label | Null | | | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| 8 | Lập báo cáo | Button | Null | | | Luôn enable. Chỉ hiển thị khi kỳ ở trạng thái Trong thời hạn. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CF_01, CMR_04. |
| 9 | Nhập từ file | Button | Null | | | Luôn enable. Mở màn hình chọn/kéo thả file. Chỉ hiển thị khi kỳ ở trạng thái Trong thời hạn. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| **Khung Danh sách Báo cáo** | | | | | |  |
| 10 | Mã báo cáo | Label | Null | | | Mã hệ thống sinh. Tham chiếu: CMR_09. |
| 11 | Tên dự án | Label | Null | | | Tên dự án gắn với báo cáo. |
| 12 | Ngày cập nhật | Label | Null | | | Định dạng: dd/MM/yyyy HH:mm. |
| 13 | Trạng thái | Label | Null | | | Tham chiếu: CMR_03. |
| 14 | Hành động | Button group | Null | | | Nộp, Chỉnh sửa, Xem chi tiết, Xem vòng đời, In, Xuất báo cáo theo trạng thái. Tham chiếu: UC353-358.3. |

---

### 3. Mô tả các xử lý của chức năng

- Hệ thống tự động nhóm danh sách theo Kỳ hạn báo cáo, mặc định collapse.
- Sắp xếp báo cáo bên trong kỳ theo thứ tự từ mới → cũ.
- Danh sách dự án trong bộ lọc chỉ hiển thị dự án của NĐT đang login. Tham chiếu: CMR_02.
- [Lập báo cáo] và [Nhập từ file] bị ẩn với kỳ báo cáo chưa bắt đầu. Tham chiếu: CF_01.
- Phân trang. Tham chiếu: CMR_10.

---


## UC353-358.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Lập mới Báo cáo theo dõi, giám sát thực hiện doanh nghiệp sinh thái (Mẫu B.4)
- Chức năng cho phép Nhà đầu tư chọn dự án và điền biểu mẫu gồm 4 Phần. Sau khi chọn Dự án, toàn bộ thông tin NĐT và Dự án (Phần I) sẽ được tự động fill từ Hệ thống QLDA nội bộ. Hệ thống rẽ nhánh UI theo Loại nhà đầu tư (Cá nhân hoặc DN/Tổ chức).

Phân quyền: Nhà đầu tư/Tổ chức kinh tế thực hiện dự án. Tham chiếu: CMR_02.

Điều kiện tiên quyết: Chỉ những nhà đầu tư, tổ chức/ doanh nghiệp có dự án cần nộp báo cáo (được setup trong cấu hình kỳ báo cáo) thì mới có thể lập được báo cáo.

Hậu điều kiện: Tùy thuộc vào action người dùng chọn (Hủy / Xem / Lưu nháp / Nộp báo cáo) sẽ có cách xử lý khác nhau. Tham chiếu: CF_01.

Truy cập chức năng: Màn danh sách báo cáo (UC353-358.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 353, 354

---

### 2. Mô tả giao diện

**Giao diện lập báo cáo**

Giao diện: Form nhập liệu chia làm 4 Phần chính.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **CHỌN DỰ ÁN** | | | | | |  |
| 0 | Chọn dự án | Dropdown | `-- Chọn dự án --` | x | x | Gọi API QLDA nội bộ, trả về danh sách dự án của user đang login. Khi chọn, tự động fill toàn bộ Phần I. Các phần còn lại chỉ được thao tác sau khi đã chọn dự án. Bổ sung quy tắc: Khi người dùng đang nhập liệu các Phần II, III, IV cho một dự án, nếu họ thay đổi lựa chọn ở Dropdown Dự án, hệ thống phải hiển thị Popup Confirm: "Bạn có muốn đổi dự án? Dữ liệu đã nhập cho dự án hiện tại sẽ bị xóa." Đồng ý -> Xóa data cũ và đổi dự án. Hủy -> Giữ nguyên. Tham chiếu: CF_07. |
| **PHẦN I – THÔNG TIN VỀ NHÀ ĐẦU TƯ VÀ DỰ ÁN ĐẦU TƯ** | | | | | | Toàn bộ Phần I: Auto-fill sau khi chọn Dự án. Disabled. Nguồn: API Quản lý dự án nội bộ. Tham chiếu: CMR_12. |
| **Mục 1 – Loại Nhà đầu tư** | | | | | | Hệ thống auto-fill Loại nhà đầu tư (Cá nhân / DN-Tổ chức) từ API. Giá trị này điều khiển hiển thị Mục 1.1 hoặc Mục 1.2 + 1.2a. Với dự án có nhiều NĐT, ưu tiên fill thông tin NĐT đang đăng nhập. |
| **Mục 1.1 – NĐT là Cá nhân** (chỉ hiển thị khi Loại NĐT = Cá nhân) | | | | | |  |
| 1.1.1 | Loại nhà đầu tư | Text | Trống | | x | Auto-fill. Disabled. Giá trị: "Cá nhân". Tham chiếu: CMR_06. |
| 1.1.2 | Họ tên | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.1.3 | Giới tính | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.1.4 | Ngày sinh | Date | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_05. |
| 1.1.5 | Quốc tịch | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.1.6 | Số giấy tờ pháp lý | Text | Trống | | x | Auto-fill. Disabled. (CMND/CCCD/). Tham chiếu: CMR_06. |
| 1.1.7 | Ngày cấp giấy tờ pháp lý | Date | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_05. |
| 1.1.8 | Nơi cấp giấy tờ pháp lý | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.1.9 | Địa chỉ thường trú | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.1.10 | Chỗ ở hiện tại | Text | Trống | | | Auto-fill. Disabled. Không bắt buộc. Tham chiếu: CMR_06. |
| 1.1.11 | Mã số thuế (tại Việt Nam) | Text | Trống | | | Auto-fill. Disabled. Hiển thị ghi chú "(nếu có)". Tham chiếu: CMR_06. |
| 1.1.12 | Điện thoại | Text | Trống | | | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.1.13 | Fax | Text | Trống | | | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.1.14 | Email | Text | Trống | | | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| **Mục 1.2 – NĐT là DN/Tổ chức** (chỉ hiển thị khi Loại NĐT = DN/Tổ chức) | | | | | |  |
| 1.2.1 | Loại nhà đầu tư | Text | Trống | | x | Auto-fill. Disabled. Giá trị: "Doanh nghiệp/Tổ chức". Tham chiếu: CMR_06. |
| 1.2.2 | Tên doanh nghiệp/tổ chức | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.2.3 | Số giấy tờ pháp lý | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.2.4 | Ngày cấp giấy tờ pháp lý | Date | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_05. |
| 1.2.5 | Cơ quan cấp giấy tờ pháp lý | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.2.6 | Địa chỉ trụ sở | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.2.7 | Mã số thuế (tại Việt Nam) | Text | Trống | | | Auto-fill. Disabled. Hiển thị ghi chú "(nếu có)". Tham chiếu: CMR_06. |
| 1.2.8 | Điện thoại | Text | Trống | | | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.2.9 | Fax | Text | Trống | | | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.2.10 | Email | Text | Trống | | | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.2.11 | Website | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| **Mục 1.2a – Người đại diện theo pháp luật** (chỉ hiển thị khi Loại NĐT = DN/Tổ chức) | | | | | |  |
| 1.2a.1 | Quốc tịch người đại diện | Label | Trống | | x | Auto-fill. Disabled. |
| 1.2a.2 | Họ tên người đại diện | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.2a.3 | Ngày sinh | Date | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_05. |
| 1.2a.4 | Số định danh cá nhân/CCCD/Số hộ chiếu | Text | Trống | | x | Auto-fill. Disabled. Hiển thị chung label, không phân biệt là CCCD hay Passport. Tham chiếu: CMR_06. |
| 1.2a.5 | Chỗ ở hiện tại | Text | Trống | | | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.2a.6 | Điện thoại | Text | Trống | | | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.2a.7 | Fax | Text | Trống | | | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 1.2a.8 | Email | Text | Trống | | | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| **Mục 2 – Tổ chức kinh tế thực hiện dự án** | | | | | |  |
| 2.1 | Tên tổ chức kinh tế | Text | Trống | | | Auto-fill. Disabled. Hiển thị ghi chú "(nếu có)". Tham chiếu: CMR_06. |
| 2.2 | Mã số doanh nghiệp/số Giấy phép đầu tư/Giấy chứng nhận đăng ký đầu tư/Quyết định thành lập | Text | Trống | | | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 2.3 | Tên cơ quan cấp | Text | Trống | | | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 2.4 | Ngày cấp lần đầu | Date | Trống | | | Auto-fill. Disabled. Tham chiếu: CMR_05. |
| 2.5 | Ngày điều chỉnh gần nhất | Date | Trống | | | Auto-fill. Disabled. Hiển thị ghi chú "(nếu có)". Tham chiếu: CMR_05. |
| **Mục 3 – Thông tin về dự án đầu tư** | | | | | |  |
| 3.1 | Tên dự án đầu tư | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 3.2 | Địa điểm thực hiện dự án | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 3.3 | Số Giấy chứng nhận đầu tư/ Giấy chứng nhận đăng ký đầu tư (hoặc văn bản pháp lý tương đương) | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 3.4 | Cơ quan cấp | Text | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_06. |
| 3.5 | Ngày cấp lần đầu | Date | Trống | | x | Auto-fill. Disabled. Tham chiếu: CMR_05. |
| 3.6 | Ngày điều chỉnh gần nhất | Date | Trống | | | Auto-fill. Disabled. Hiển thị ghi chú "(nếu có)". Tham chiếu: CMR_05. |
| **PHẦN II – NĂNG LỰC SẢN XUẤT** | | | | | | Bảng động (Dynamic Table). Người dùng có thể Thêm/Xóa dòng. Không auto-fill. Tên tiêu đề bảng: "Bảng năng lực sản xuất năm [Năm kỳ báo cáo - 1]". |
| P2.1 | Tên sản phẩm | Textarea | Null | x | x | Nhập tay. Tự động xuống dòng khi nội dung dài; chiều cao ô tự co giãn theo nội dung. Placeholder: "Nhập Tên sản phẩm". Tham chiếu: CMR_06. |
| P2.2 | Đơn vị đo | Dropdown | Null | x | x | Single-select. Các giá trị: tấn/năm, m/năm, m²/năm, m³/giờ. Tham chiếu: CMR_07. |
| P2.3 | Theo thiết kế | Textarea | Null | x | x | Nhập tay. Tự động xuống dòng. Placeholder: "Nhập Theo thiết kế". Tham chiếu: CMR_06. |
| P2.4 | Mức sản xuất hiện tại | Text | Null | x | x | Nhập tay. Tự động xuống dòng. Tham chiếu: CMR_06. |
| P2.5 | Tiêu thụ năng lượng theo sản phẩm | Number + Single choice dropdown | Điện | x | x | Nhập giá trị số kèm chọn loại năng lượng: điện/dầu/gas. Mặc định chọn loại năng lượng là Điện. Tham chiếu: CMR_05. Tham chiếu: CMR_07. |
| P2.6 | Doanh thu theo sản phẩm (triệu đồng) | Number | Null | x | x | Nhập tay. Validate: Giá trị ≥ 0. Tham chiếu: CMR_08. |
| **Phần III. TÌNH HÌNH THỰC HIỆN VÀ DUY TRÌ HOẠT ĐỘNG SỬ DỤNG HIỆU QUẢ TÀI NGUYÊN VÀ SẢN XUẤT SẠCH HƠN** | | | | | | Sử dụng hiệu quả tài nguyên và sản xuất sạch hơn. |
| P3.1 | Mô hình tiết kiệm năng lượng đã áp dụng | Textarea | Null | x | x | Nhập tay. Mô tả tự do. Tham chiếu: CMR_06. Placeholder: "Nhập Mô hình tiết kiệm năng lượng đã áp dụng". |
| P3.2 | Tiết kiệm điện năng (kWh) | Number | Null | x | x | Nhập tay. Số dương. Nhóm tiêu đề: "Mức tiết kiệm năng lượng cho năm [Năm kỳ báo cáo - 1]". Tham chiếu: CMR_05. |
| P3.3 | Giảm phát thải CO2 từ tiết kiệm điện (tấn/năm) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P3.4 | Tiết kiệm chi phí điện (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P3.5 | Lợi ích khác từ tiết kiệm điện | Textarea | Null | x | x | Nhập tay. Mô tả tự do. Placeholder: "Nhập Lợi ích khác từ tiết kiệm điện". Tham chiếu: CMR_06. Tham chiếu: CMR_07. |
| P3.6 | Nhiên liệu năm [N-1] | Number + Dropdown đơn vị | Null | x | x | Nhập giá trị số và chọn đơn vị (lít, m³, tấn...). Tham chiếu: CMR_05. |
| P3.7 | Giảm phát thải CO2 từ tiết kiệm nhiên liệu (tấn/năm) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P3.8 | Tiết kiệm chi phí nhiên liệu (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P3.9 | Lợi ích khác từ tiết kiệm nhiên liệu | Textarea | Null | x | x | Nhập tay. Mô tả tự do. Placeholder: "Nhập Lợi ích khác từ tiết kiệm nhiên liệu". Tham chiếu: CMR_06. |
| P3.10 | Giảm phát thải CO2 trong năm [N -1] tương đương (tấn/năm) | Number | Null | x | x | Nhập tay hoặc hệ thống gợi ý auto-sum: P3.3 + P3.7 (hiển thị tooltip). Hệ thống chỉ là gợi ý, nếu người dùng nhập số khác hệ thống vẫn lưu và không warning gì cả. Tham chiếu: CMR_08. |
| P3.11 | Tiết kiệm nước (m³/năm) trong năm [N-1] | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P3.12 | Tiết kiệm chi phí nước (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P3.13 | Giảm nước thải (m³/năm) trong năm [N-1] | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P3.14 | Tiết kiệm chi phí từ giảm nước thải (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P3.15 | Tái sử dụng (tấn/năm) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P3.16 | Tiết kiệm chi phí từ tái sử dụng (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P3.16a | Giảm chất thải phải xử lý (tấn/năm): thông qua: | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P3.17 | Tái chế (tấn/năm) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P3.18 | Tiết kiệm chi phí từ tái chế (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P3.19 | Tiết kiệm vật liệu sơ cấp (tấn/năm) trong năm [N-1] | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P3.20 | Tiết kiệm chi phí vật liệu sơ cấp (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P3.21 | Tiết kiệm hóa chất (tấn/năm) trong năm [N-1] | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P3.22 | Tiết kiệm chi phí hóa chất (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| **PHẦN IV – TÌNH HÌNH THỰC HIỆN CỘNG SINH CÔNG NGHIỆP** | | | | | |  |
| P4.1 | Số lượng cộng sinh công nghiệp đã thực hiện đến năm [N] | Number | Null | x | x | Nhập tay. Số nguyên dương. Tham chiếu: CMR_05. |
| P4.2 | Loại hình cộng sinh công nghiệp | Multi-select Checkbox | Không chọn | x | x | 5 lựa chọn:<br>- Trao đổi yếu tố đầu vào, đầu ra phục vụ sản xuất (nguyên vật liệu, nước, năng lượng, chất thải, sản phẩm phụ, phế liệu...);<br>- Sử dụng chung hạ tầng phục vụ sản xuất trong khu công nghiệp (không bao gồm hạ tầng kỹ thuật và xã hội dùng chung do doanh nghiệp đầu tư phát triển hạ tầng khu công nghiệp cung cấp);<br>- Sử dụng dịch vụ hoạt động sản xuất kinh doanh trong khu công nghiệp do nhà đầu tư thực hiện dự án đầu tư xây dựng và kinh doanh kết cấu hạ tầng khu công nghiệp hoặc bên thứ 3 cung cấp (dịch vụ đào tạo nhân viên, dịch vụ bảo dưỡng, dịch vụ cung cấp hơi, dịch vụ kho hàng, dịch vụ kho đông lạnh...);<br>- Liên kết cộng tác giữa các doanh nghiệp trong các khu công nghiệp khác trong việc thu gom, xử lý, tái sử dụng và tái chế nguyên vật liệu, chất thải, phế liệu, thu hồi năng lượng và nhiệt dư, tái sử dụng và tuần hoàn nước.<br>- Các liên kết cộng sinh khác (nếu có, đề nghị mô tả) |
| P4.3 | Thông qua cam kết được ký với doanh nghiệp trong khu công nghiệp | Dropdown | Null | x | x | Multiple-select. Danh sách DN trong cùng KCN. Tham chiếu: CMR_07. |
| P4.4 | Thông qua cam kết được ký với doanh nghiệp bên ngoài khu công nghiệp | Textarea | Null | x | x | Nhập tay. Mô tả tên DN ngoài KCN. Placeholder: "Nhập Thông qua cam kết với DN ngoài KCN". Tham chiếu: CMR_06. |
| P4.5 | Hỗ trợ của nhà đầu tư thực hiện dự án đầu tư xây dựng và kinh doanh kết cấu hạ tầng khu công nghiệp trong thực hiện cộng sinh công nghiệp | Textarea | Null | x | x | Nhập tay. Mô tả tự do. Hiển thị ghi chú "(nếu có)". Placeholder: "Nhập Hỗ trợ của NĐT hạ tầng KCN". Tham chiếu: CMR_06. |
| P4.6 | Tiết kiệm điện năng từ cộng sinh (kWh) | Number | Null | x | x | Nhập tay. Số dương. Nhóm tiêu đề: "Mức tiết kiệm năng lượng trong năm [N-1]". Tham chiếu: CMR_05. |
| P4.7 | Giảm CO2 từ tiết kiệm điện – cộng sinh (tấn/năm) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P4.8 | Tiết kiệm chi phí điện từ cộng sinh (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P4.9 | Lợi ích khác từ tiết kiệm điện | Textarea | Null | x | x | Nhập tay. Mô tả tự do. Placeholder: "Nhập Lợi ích khác từ tiết kiệm điện". Tham chiếu: CMR_06. |
| P4.10 | Nhiên liệu năm [N-1]  | String | Null | x | x | Nhập số và đơn vị đo. Tham chiếu: CMR_06. |
| P4.11 | Giảm CO2 từ tiết kiệm nhiên liệu  (tấn/năm) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P4.12 | Tiết kiệm chi phí nhiên liệu – cộng sinh (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P4.13 | Lợi ích khác từ tiết kiệm nhiên liệu | Textarea | Null | x | x | Nhập tay. Mô tả tự do. Placeholder: "Nhập Lợi ích khác từ tiết kiệm nhiên liệu". Tham chiếu: CMR_06. |
| P4.14 | Giảm phát thải CO2 tương đương (tấn/năm) trong năm [N-1] | Number | Null | x | x | Nhập tay hoặc hệ thống gợi ý auto-sum: P4.7 + P4.11 (hiển thị tooltip). Hệ thống chỉ là gợi ý, nếu người dùng nhập số khác hệ thống vẫn lưu và không warning gì cả. Tham chiếu: CMR_05. |
| P4.15 | Tiết kiệm nước (m³/năm) trong năm [N-1] | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P4.16 | Tiết kiệm chi phí nước từ cộng sinh (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P4.17 | Giảm nước thải (m³/năm) trong năm [N-1] | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P4.18 | Tiết kiệm chi phí nước thải từ cộng sinh (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P4.19 | Giảm chất thải phải xử lý trong năm [N-1] (tấn/năm) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P4.20 | Tái sử dụng (tấn/năm) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P4.21 | Tiết kiệm chi phí từ tái sử dụng (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P4.22 | Tái chế (tấn/năm) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P4.23 | Tiết kiệm chi phí từ tái chế (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P4.24 | Tiết kiệm vật liệu sơ cấp (tấn/năm) trong năm [N-1] | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P4.25 | Tiết kiệm chi phí từ tiết kiệm vật liệu sơ cấp (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P4.26 | Sử dụng vật liệu thứ cấp từ DN khác (tấn/năm) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P4.27 | Tiết kiệm chi phí từ sử dụng vật liệu thứ cấp (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P4.28 | Cung cấp vật liệu thứ cấp cho DN khác (tấn/năm) | String | Null | x | x | Nhập tay. Tham chiếu: CMR_06. |
| P4.29 | Thu được chi phí từ cung cấp vật liệu thứ cấp (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P4.30 | Tiết kiệm hóa chất (tấn/năm) trong năm [N-1] | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P4.31 | Tiết kiệm chi phí hóa chất – cộng sinh (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| P4.32 | Chia sẻ dịch vụ/dịch vụ dùng chung trong năm [N-1] | Textarea | Null | x | x | Nhập tay. Mô tả các dịch vụ dùng chung. Placeholder: "Nhập Chia sẻ dịch vụ/dịch vụ dùng chung trong năm [N-1]". Tham chiếu: CMR_06. |
| P4.33 | Tiết kiệm chi phí từ dịch vụ dùng chung (triệu đồng) | Number | Null | x | x | Nhập tay. Số dương. Tham chiếu: CMR_05. |
| **CÁC BUTTON** | | | | | |  |
| B1 | Hủy | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]"). |
| B2 | Xem trước | Button | | | | Mở popup PDF Preview báo cáo (không rời màn Lập). Tham chiếu: CF_07.1. |
| B3 | Lưu nháp | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]"). |
| B4 | Nộp báo cáo | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |

---

### 3. Mô tả các xử lý của chức năng

Xử lý chung: Tham chiếu: CF_01 (Lập báo cáo), CMR_18, CF_04 (Xuất báo cáo), CF_05 (In).

Xử lý đặc thù biểu mẫu B.4:

- Khởi tạo màn hình: Toàn bộ các trường Phần I ở trạng thái Disabled và bỏ trống. Các Phần II, III, IV bị khoá tương tác cho đến khi Nhà đầu tư chọn Dự án. Tham chiếu: CF_01.
- Xử lý Auto-fill (Phần I): Khi chọn Dự án, hệ thống gọi API Quản lý dự án nội bộ để điền dữ liệu. Giá trị Loại nhà đầu tư trả về từ API xác định hiển thị Mục 1.1 (Cá nhân) hoặc Mục 1.2 + 1.2a (DN/Tổ chức). Với dự án có nhiều NĐT, hệ thống ưu tiên điền thông tin của NĐT đang đăng nhập vào hệ thống. Khi API không trả về Quốc tịch của User, hoặc bất kỳ trường thông tin nào khác được auto-fill từ API nhưng không thành công thì trường đó sẽ được enable để user có thể tự nhập thủ công. Tham chiếu: CMR_12.
- Xử lý nhãn động (Mục 1.2a): Nhãn trường Số định danh cá nhân (1.2a.4) thay đổi thành "CCCD" nếu Quốc tịch người đại diện là Việt Nam, hoặc "Số hộ chiếu" nếu là người nước ngoài.
- Phần II – Bảng Động: Hệ thống cung cấp tối thiểu 1 dòng mặc định. Người dùng nhấn [+ Thêm dòng] để thêm sản phẩm mới. Nhấn [Xóa] ở mỗi dòng để xóa. Không được xóa dòng cuối cùng còn lại.
- Gợi ý Auto-sum (P3.10, P4.14): Các trường CO2 tổng hiển thị tooltip gợi ý giá trị bằng tổng của 2 trường CO2 thành phần. Người dùng có thể chấp nhận hoặc tự nhập giá trị khác tổng gợi ý. Chấp nhận số thập phân có tối đa 2 chữ số sau dấu phẩy đối với các trường quy đổi CO2.

---


## UC353-358.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ – Xem chi tiết, Xem vòng đời, In, Xuất báo cáo, Nộp, Chỉnh sửa
- Chức năng cho phép Nhà đầu tư thực hiện tác vụ theo trạng thái báo cáo (Lưu nháp / Yêu cầu chỉnh sửa).

Phân quyền: Nhà đầu tư/Tổ chức kinh tế thực hiện dự án. Tham chiếu: CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC353-358.1) → Cột Hành động → Chọn tác vụ tương ứng

Chức năng đáp ứng usecase số: 355, 356, 357, 358

---

### 2. Mô tả giao diện

**Các Button theo Action Mapping:**

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |  
| --- | --- | --- | --- | --- | --- |  
| 1 | Nộp | Button | Chỉ khi Lưu nháp | Người tạo | Tham chiếu: CF_09. Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |
| 2 | Chỉnh sửa | Button | Chỉ khi Lưu nháp hoặc Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Tất cả người dùng | Khi click mở màn hình Xem chi tiết (toàn bộ trường Disabled). Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Tất cả người dùng | Khi click mở popup Vòng đời. Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Tất cả người dùng | Kết xuất file Docx. Tham chiếu: CF_04. |
| 7 | Xóa | Button | Lưu nháp **VÀ** chưa từng nộp | Người tạo | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết: Tham chiếu: CF_07.
- Xem vòng đời: Tham chiếu: CF_06.
- In báo cáo: Tham chiếu: CF_05.
- Xuất báo cáo: Kết xuất ra file Docx. Tham chiếu: CF_04.
- Chỉnh sửa: Tham chiếu: CF_03.

---

## 4. Acceptance Criteria

| ID | Kịch bản kiểm thử (Scenario) | Điều kiện (Given) | Hành động (When) | Kết quả mong đợi (Then) |
|---|---|---|---|---|


| AC1 | Kiểm tra Table động Phần II | Đang ở Phần II | Nhấn nút "Thêm dòng" | Thêm 1 dòng mới vào cuối bảng |
| AC2 | Kiểm tra Table động Phần II | Đang ở Phần II có nhiều dòng | Nhấn nút "Xóa" tại một dòng | Xóa dòng đó khỏi bảng |
| AC3 | Kiểm tra Table động Phần II | Đang ở Phần II chỉ còn 1 dòng | Quan sát nút "Xóa" | Nút "Xóa" bị ẩn đi |
| AC4 | Kiểm tra auto-fill Phần I | Chọn Dự án từ Dropdown Phần I | Đã chọn xong dự án | Các trường thông tin Dự án và NĐT ở Phần I tự động điền giá trị. Disabled toàn bộ |

---

## 5. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |  
| --- | --- | --- | --- | --- | --- |  
| --- | --- | --- | --- | --- | --- |
| 2026-05-07 | 1.1 → 1.2 | Khung lọc & tìm kiếm | Kỳ báo cáo (Dropdown) | Năm (YearPicker) | Cập nhật điều kiện lọc theo yêu cầu |
| 2026-05-08 | 1.2 → 1.3 | Chọn dự án | (Không có) | Thêm Popup Confirm khi đổi Dự án | Cập nhật theo Implementation Plan |
| 2026-05-08 | 1.2 → 1.3 | Auto-sum | Gợi ý Auto-sum | Hệ thống vẫn lưu nếu nhập khác gợi ý | Cập nhật theo Implementation Plan |
| 2026-05-08 | 1.2 → 1.3 | Fallback API | (Không có) | Enable trường auto-fill nếu API lỗi | Cập nhật theo Implementation Plan |
| 2026-05-08 | 1.2 → 1.3 | Label CCCD/Passport | Label động | Gộp chung thành 1 label không phân biệt | Cập nhật theo Implementation Plan |
| 2026-05-08 | 1.2 → 1.3 | NFR | (Không có) | Chấp nhận tối đa 2 chữ số thập phân cho CO2 | Cập nhật theo Implementation Plan |
| 2026-05-11 | +1 | Tên cột | `Ngày cập nhật / Nộp` | `Ngày cập nhật` | Đồng bộ tên cột theo CS_02 (INS-03) |
| 2026-05-11 | +1 | Điều kiện hiển thị nút | `Luôn hiển thị` | `Tất cả trạng thái` | Chuẩn hóa điều kiện (INS-07) |
| 2026-05-11 | +1 | Dòng phân cách Markdown | Sai số cột | 6 cột đúng | Sửa lỗi Markdown (INS-05) |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma du an / ten du an | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (2 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them , CMR_18 vao tham chieu CF_01 tren man hinh lap bao cao | Tuan thu CMR_18 Tab Navigation (STD-07) |
| 2026-05-17 | CMR v2.0 | STD-01 Them CMR_16 vao filter dropdown rows (2 dong) | Chua co CMR_16 | Them tham chieu CMR_16 | Filter phai co Tat ca default |
| 2026-05-17 | CMR v2.0 | STD-04a Placeholder text/numeric (10 truong) | Nhap du lieu | Nhap [ten truong cu the] | CMR_06 STD-04a |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-18 | 1.3 → 1.4 | Bảng thuộc tính | (Không có) | Bổ sung Loại quy trình: Quy trình 2 bước, CMCĐT_BCTK_01 | Phân loại luồng quy trình theo yêu cầu |
| 2026-05-20 | 1.4 → 1.5 | P2.5 Tiêu thụ năng lượng | Number + Multiple-selection Dropdown (kèm chọn nhiều loại) | Number + Single choice dropdown (mặc định là Điện) | Cập nhật theo yêu cầu |
| 2026-05-21 | 1.5 → 1.6 | Toàn bộ tài liệu | Các trường thông tin cũ của phiên bản 1.5 | Thêm trường P3.16a; bỏ tiêu đề nhóm ở P3.15; cập nhật 5 lựa chọn ở P4.2; chuẩn hóa hàng loạt tên trường trong các Phần I, II, III, IV | Cập nhật theo yêu cầu của người dùng, chuẩn hóa thuật ngữ và thông tin cộng sinh |
| 2026-05-23 | 1.6 → 1.7 | Ghi chú các dòng Auto-fill (Phần I) | Auto-fill. Disabled. ... | Auto-fill. Disabled. ... | Thêm ghi chú không hiển thị placeholder cho các trường auto-fill |
| 2026-05-23 | 1.6 → 1.7 | P3.2 Tham chiếu | Tham chiếu: CMR_08 | Tham chiếu: CMR_05 | Sửa tham chiếu CMR theo yêu cầu |
| 2026-05-23 | 1.6 → 1.7 | P3.5 Tham chiếu | Tham chiếu: CMR_06 | Tham chiếu: CMR_06. Tham chiếu: CMR_07 | Bổ sung tham chiếu CMR_07 |
