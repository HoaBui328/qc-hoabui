# UC161-166: Báo cáo định kỳ 6 tháng tình hình hoạt động dự án đầu tư tại nước ngoài

| Thuộc tính               | Giá trị                                      |
| --- | --- |
| **BA phụ trách** | anh.luu |
| **Phân hệ** | Quản lý đầu tư ra nước ngoài |
| **Mẫu biểu** | I.15 [MBFS] | Phân hệ Báo cáo | Quản lý đầu tư ra nước ngoài |
| **Loại báo cáo** | Định kỳ (Periodically) |
| **Hình thức nộp** | Báo cáo đơn lẻ (Single report form) |
| **Phạm vi dữ liệu đầu vào** | Có (chọn dự án) |
| **Cơ quan nhận** | Bộ Tài chính (Cục Đầu tư nước ngoài) |
| **Đối tượng lập** | Nhà đầu tư (ĐTRNN) thuộc dự án đang hoạt động tại nước ngoài |
| **Giao diện** | User site (Phía người dùng) |
| **Ngày tạo** | 2026-04-20 |
| **Phiên bản** | 1.6 |
| **Quy tắc sinh mã báo cáo** | ODI_I15_[ID] |
| **Loại quy trình** | Quy trình 2 bước, CMCĐT_BCTK_03 |

---

## UC161-166.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo định kỳ 6 tháng tình hình hoạt động dự án đầu tư tại nước ngoài
- Chức năng cho phép Nhà đầu tư truy cập màn hình chính để theo dõi danh sách các báo cáo định kỳ 6 tháng, được nhóm theo từng Kỳ hạn báo cáo. Áp dụng luồng nghiệp vụ Case B (ĐTRNN).

Phân quyền: Nhà đầu tư (ĐTRNN) thuộc dự án đang hoạt động tại nước ngoài.

Truy cập chức năng: Phân hệ Báo cáo → Quản lý đầu tư ra nước ngoài → Báo cáo định kỳ 6 tháng tình hình hoạt động dự án đầu tư tại nước ngoài

Chức năng đáp ứng usecase số: 161, 162, 163, 164, 165, 166

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện:

**Periodic-single**: Giao diện mẫu cho báo cáo có kỳ hạn và gửi lẻ từng báo cáo

Mô tả giao diện:

| #                                                     | Tên trường           | Kiểu trường              | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả                                                                                                                                                                                                                                                                                                         |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm**        |                         |                             |                       |              |            |                                                                                                                                                                                                                                                                                                                 |
| 1                                                     | Năm                    | Yearpicker                  | Năm hiện tại       | x            |            | Người dùng nhấp để chọn năm từ calendar picker. Hệ thống lọc và nhóm danh sách theo năm được chọn. Kết quả hiển thị ngay lập tức sau khi chọn, không cần nhấn thêm nút. Tham chiếu: CMR_07.                                                                                    |
| 2                                                     | Trạng thái kỳ        | Multiple-selection Dropdown | Null                  | x            |            | Lọc theo trạng thái của kỳ hạn. Người dùng chọn một hoặc nhiều giá trị: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_04, CMR_07, CMR_16                                                                                        |
| 3                                                     | Trạng thái báo cáo  | Multiple-selection Dropdown | Null                  | x            |            | Lọc theo trạng thái của bản ghi báo cáo. Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07, CMR_16                                                                                        |
| 4                                                     | Dự án                 | Multiple-selection Dropdown | Null                  | x            |            | Hệ thống cung cấp danh sách Dự án để chọn (không cho phép nhập tự do). Chọn một hoặc nhiều dự án để lọc. Kết quả hiển thị ngay sau khi chọn. Tham chiếu: CMR_07, CMR_16                                                                                                                    |
| 5                                                     | Mã báo cáo           | Search bar                  | Null                  | x            |            | Nhập liệu tự do để tìm theo mã báo cáo. Kết quả hiển thị ngay khi nhập. Nếu không tìm thấy kết quả: hiển thị màn hình trắng với text "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| **Khung Danh sách kỳ hạn**                   |                         |                             |                       |              |            |                                                                                                                                                                                                                                                                                                                 |
| 6                                                     | Kỳ hạn báo cáo      | Label                       | Null                  |              |            | Hiển thị tên kỳ hạn. Báo cáo 6 tháng có 2 kỳ/năm: **"Kỳ I năm [YYYY]"** (01/01–30/06), **"Kỳ II năm [YYYY]"** (01/07–31/12). Hệ thống tự động xác định kỳ dựa trên ngày hiện tại. |
| 7                                                     | Trạng thái kỳ | Label                       | Null                  |              |            | Hiển thị trạng thái tổng hợp của kỳ: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04.                                                                                                                                                                                       |
| 7a | Lập báo cáo | Button | | | | Hiển thị khi kỳ hạn ở trạng thái "Trong thời hạn". Cho phép NĐT tạo mới báo cáo cho kỳ tương ứng. Tham chiếu: CF_01, CMR_04. |
| 7b | Nhập từ file | Button | | | | Hiển thị khi kỳ hạn ở trạng thái "Trong thời hạn". Cho phép NĐT nhập từ file dữ liệu báo cáo từ file. Tham chiếu: CF_02, CMR_04. |
| **Khung Danh sách Báo cáo** (trong mỗi kỳ) |                         |                             |                       |              |            |                                                                                                                                                                                                                                                                                                                 |
| 8                                                     | Mã báo cáo           | Label                       | Null                  |              |            | Hiển thị mã báo cáo do hệ thống sinh theo quy tắc. Tham chiếu: CMR_09.                                                                                                                                                                                                                                 |
| 9                                                     | Tên dự án            | Label                       | Null                  |              |            | Hiển thị tên đầy đủ của dự án đầu tư ra nước ngoài.                                                                                                                                                                                                                                             |
| 10 | Ngày cập nhật | Label | Null | | | Hiển thị ngày giờ của thao tác gần nhất (Chỉnh sửa / Lưu nháp / Nộp). Định dạng: dd/MM/yyyy HH:mm. |
| 11                                                    | Trạng thái báo cáo  | Label                       | Null                  |              |            | Trạng thái cấp bản ghi. Tham chiếu: CMR_03. **Lưu ý:** Giá trị "Đã được lập bởi NĐT khác" **không phải trạng thái bản ghi** — đây là label hiển thị đặc biệt dành cho NĐT chưa từng tương tác với bản ghi. Khi NĐT nhấn vào bản ghi (Xem/Sửa), label chuyển thành trạng thái thực (CMR_03). Bộ lọc "Trạng thái báo cáo" **không bao gồm** giá trị này. Tooltip: *"Báo cáo kỳ này đã được lập bởi [Tên đầy đủ NĐT A]. Bạn không thể tạo thêm báo cáo cho cùng dự án trong kỳ này."* Tham chiếu: CMR_02. |
| 12                                                    | Hành động            | Button group                | Null                  |              |            | Hiển thị các nút thao tác theo trạng thái bản ghi. Chi tiết tham chiếu: UC161-166.3.                                                                                                                                                                                                                  |

---

### 3. Mô tả các xử lý của chức năng

- Thao tác của nhiều NĐT:
  - Chỉ cho phép 1 NĐT lập BC. Các NĐT chỉ xem và chỉnh sửa. Chỉnh sửa follow theo CMR
- Yêu cầu về hiển thị tại khung danh sách kỳ hạn:
  - Hệ thống tự động nhóm danh sách theo Kỳ hạn báo cáo (Kỳ I / Kỳ II theo năm).
  - Thực hiện phân trang cho danh sách kỳ hạn. Tham chiếu: CMR_10.
  - Sắp xếp giảm dần theo thời gian (kỳ mới nhất lên đầu).
- Thao tác lọc & tìm kiếm:
  - Tất cả bộ lọc (Năm, Trạng thái, Dự án) và ô tìm kiếm Mã báo cáo đều hiển thị kết quả ngay lập tức sau khi người dùng tương tác, không cần nhấn thêm nút xác nhận.
  - Nếu không có kết quả: màn hình trắng hiển thị text "Không tìm thấy kết quả".

---


## UC161-166.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Tạo mới báo cáo định kỳ 6 tháng tình hình hoạt động dự án đầu tư tại nước ngoài
- Chức năng cho phép Nhà đầu tư nhập liệu và khởi tạo báo cáo theo đúng biểu mẫu I.15. Dữ liệu từ API được tự động điền sau khi người dùng chọn Dự án. Tham chiếu: CF_01.

Phân quyền: Nhà đầu tư (ĐTRNN) được phép tạo báo cáo trong kỳ **Trong thời hạn**. Không được phép tạo báo cáo cho kỳ **Chưa tới hạn** và **Qua kỳ báo cáo**. Tham chiếu: CMR_04.

Truy cập chức năng: Màn danh sách báo cáo (UC161-166.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 161, 162

---

### 2. Mô tả giao diện

Giao diện: Màn hình tạo mới theo biểu mẫu I.15.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **THÔNG TIN CHUNG** | | | | | | |
| 1 | Từ tháng | Dropdown (Month) | Tính tự động | | | Hệ thống tự động tính toán dựa trên kỳ lập báo cáo (Kỳ I: tháng 1, Kỳ II: tháng 7). Disabled — chỉ hiển thị, không cho phép chỉnh sửa. |
| 2 | Đến tháng | Dropdown (Month) | Tính tự động | | | Hệ thống tự động tính toán dựa trên kỳ lập báo cáo (Kỳ I: tháng 6, Kỳ II: tháng 12). Disabled — chỉ hiển thị, không cho phép chỉnh sửa. |
| 3 | Năm | Dropdown (Year) | Tính tự động | | | Hệ thống tự động điền năm hiện tại dựa trên kỳ lập báo cáo. Disabled — chỉ hiển thị, không cho phép chỉnh sửa. |
| **Chọn Dự án** | | | | | | |
| 4 | Dự án | Dropdown | Null | x | x | Người dùng chọn Dự án từ danh sách. Có thể chọn trước hoặc sau khi nhập liệu. Ngay khi chọn, hệ thống gọi API và điền tự động các trường liên quan (Phần I, Phần II). Nếu Lưu nháp/Nộp mà chưa chọn: hiển thị lỗi "Vui lòng chọn Dự án". Tham chiếu: CF_01, CMR_07. |
| **PHẦN I - THÔNG TIN NHÀ ĐẦU TƯ & DỰ ÁN** | | | | | | |
| 5 | Kỳ báo cáo | Label | Tính tự động | | | Hệ thống tự tính và hiển thị nhãn kỳ báo cáo. Báo cáo 6 tháng: "Kỳ I năm [YYYY]" (01/01–30/06), "Kỳ II năm [YYYY]" (01/07–31/12). |
| 6 | Mã số dự án / Số xác nhận giao dịch ngoại hối | Label | Từ API | | | Tự động điền từ API sau khi chọn Dự án. Không cho phép chỉnh sửa. Tham chiếu: CF_01, CMR_12. |
| 7 | Ngày cấp lần đầu | Label | Từ API | | | Tự động điền từ API sau khi chọn Dự án. Định dạng dd/MM/yyyy. Không cho phép chỉnh sửa. Tham chiếu: CF_01, CMR_12. |
| 8 | Ngày cấp điều chỉnh (nếu có) | Label | Từ API | | | Tự động điền từ API sau khi chọn Dự án. Không cho phép chỉnh sửa. Tham chiếu: CF_01, CMR_12. |
| 9 | Danh sách Nhà đầu tư | Grid/Accordion | Từ API | | | Hiển thị danh sách NĐT trong dự án theo cấu trúc mở rộng (Accordion). Dữ liệu hoàn toàn từ API sau khi chọn Dự án. Mỗi NĐT gồm: Tên NĐT, Địa chỉ, Số điện thoại (từ IRC), Vốn đăng ký đầu tư (USD) — Disabled. Tham chiếu: CMR_12. |
| 10 | Số điện thoại người làm báo cáo | Textbox | Từ API | x | x | Tự động điền từ API (thông tin profile người lập). Nếu để trống: hiển thị lỗi "Vui lòng nhập Số điện thoại người làm báo cáo". Không validate format SĐT — chỉ validate trường bắt buộc. Tham chiếu: CMR_06. Cho phép chỉnh sửa. Placeholder: "Nhập số điện thoại". |
| 11 | Email người làm báo cáo | Textbox | Từ API | x | x | Tự động điền từ API (thông tin profile người lập). Nếu để trống: hiển thị lỗi "Vui lòng nhập Email người làm báo cáo". Không validate format Email — chỉ validate trường bắt buộc. Tham chiếu: CMR_06. Cho phép chỉnh sửa. Placeholder: "Nhập email". |
| **PHẦN II - TÌNH HÌNH THỰC HIỆN (Bảng số liệu)** | | | | | | |
| 12 | Đơn vị: USD | Label | USD | | | Đơn vị tính phải hiển thị rõ ràng tại tiêu đề bảng. |
| | **Cấu trúc bảng số liệu** | | | | | **Bảng dạng grid 2 chiều:**<br/>- **Hàng (Dynamic theo số NĐT ở Phần I):** Số hàng = số NĐT từ API tại Phần I (#9). Khi Dự án được chọn → bảng tự động render đúng số hàng NĐT tương ứng. Cột đầu tiên hiển thị Tên NĐT (Disabled).<br/>- **Cột:** Mỗi chỉ tiêu (#13, #14) gồm **3 cột con**: *Tiền / Máy móc, thiết bị / Tài sản khác* (header 2 cấp). Chỉ tiêu #15, #16 chỉ có 1 cột (vì bản chất là tiền chuyển về).<br/>- **Dòng Tổng (#17):** Auto-sum theo cột dọc cho tất cả NĐT. Hiển thị ở cuối bảng. |
| 13 | Số vốn đã chuyển ra nước ngoài trong kỳ báo cáo (không phải lũy kế) | Textbox | Null | x | x | Nhập tay theo từng NĐT × từng cột con (Tiền / Máy móc, thiết bị / Tài sản khác). Tham chiếu: CMR_05, CMR_06. Validate: chấp nhận số, dấu chấm, dấu phẩy, dấu âm. Nếu để trống: lỗi "Vui lòng nhập Số vốn đã chuyển ra". Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Placeholder: "Nhập số tiền (USD)". |
| 14 | Số vốn đã chuyển ra nước ngoài lũy kế từ khi bắt đầu hoạt động đến thời điểm báo cáo | Textbox | Null | x | x | Nhập tay theo từng NĐT × từng cột con (Tiền / Máy móc, thiết bị / Tài sản khác). Tham chiếu: CMR_05, CMR_06. Validate: tương tự trường 13. Nếu để trống: lỗi "Vui lòng nhập Số vốn lũy kế". Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Placeholder: "Nhập số tiền (USD)". |
| 15 | Số tiền đã chuyển về nước trong kỳ báo cáo | Textbox | Null | x | x | Nhập tay theo từng NĐT (1 cột). Tham chiếu: CMR_05, CMR_06. Validate: tương tự trường 13. Nếu để trống: lỗi "Vui lòng nhập Số tiền chuyển về trong kỳ". Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Placeholder: "Nhập số tiền (USD)". |
| 16 | Số tiền đã chuyển về nước lũy kế đến thời điểm báo cáo | Textbox | Null | x | x | Nhập tay theo từng NĐT (1 cột). Tham chiếu: CMR_05, CMR_06. Validate: tương tự trường 13. Nếu để trống: lỗi "Vui lòng nhập Số tiền lũy kế chuyển về". Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Placeholder: "Nhập số tiền (USD)". |
| 17 | Dòng Tổng | Label | Tính tự động | | | Auto-sum toàn bộ chỉ tiêu của tất cả NĐT theo cột dọc. Cập nhật real-time khi NĐT nhập liệu. Không cho phép chỉnh sửa. |
| **PHẦN III - TIẾN ĐỘ THỰC HIỆN** | | | | | | |
| 18 | Tiến độ thực hiện | Checkbox (Multiple choice) | Đúng tiến độ | x | x | Cho phép chọn nhiều giá trị: Đúng tiến độ / Chậm tiến độ / Gặp khó khăn / Không có khả năng triển khai. Bắt buộc chọn ít nhất 1 giá trị. |
| 19 | Lý do — Chậm tiến độ | Textarea | Null | x | x* | Ẩn mặc định. Chỉ hiển thị và trở thành Bắt buộc khi tick "Chậm tiến độ". Khi bỏ tick → textarea ẩn và dữ liệu đã nhập bị xóa. Nếu để trống khi bắt buộc: lỗi "Vui lòng nhập Lý do chậm tiến độ". Max 3000 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập lý do chậm tiến độ". |
| 20 | Lý do — Gặp khó khăn | Textarea | Null | x | x* | Ẩn mặc định. Chỉ hiển thị và trở thành Bắt buộc khi tick "Gặp khó khăn". Khi bỏ tick → textarea ẩn và dữ liệu đã nhập bị xóa. Nếu để trống khi bắt buộc: lỗi "Vui lòng nhập Lý do gặp khó khăn". Max 3000 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập lý do gặp khó khăn". |
| 21 | Lý do — Không có khả năng triển khai | Textarea | Null | x | x* | Ẩn mặc định. Chỉ hiển thị và trở thành Bắt buộc khi tick "Không có khả năng triển khai". Khi bỏ tick → textarea ẩn và dữ liệu đã nhập bị xóa. Nếu để trống khi bắt buộc: lỗi "Vui lòng nhập Lý do không có khả năng triển khai". Max 3000 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập lý do không có khả năng triển khai". |
| **PHẦN IV - TÌNH HÌNH HOẠT ĐỘNG HIỆN NAY** | | | | | | |
| 22 | Mô tả tình hình hiện tại | Textarea | Null | x | x | Nhập tay. Mô tả chi tiết tình trạng thực tế của dự án (đang hoạt động / tạm dừng / chấm dứt) kèm lý do. Nếu để trống: lỗi "Vui lòng nhập Mô tả tình hình hiện tại". Max 3000 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập mô tả tình hình hiện tại". |
| **Các Button** | | | | | | |
| 23 | Hủy | Button | | | | Luôn Enabled. Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]"). |
| 24 | Xem trước | Button | | | | Luôn Enabled. Mở popup PDF Preview báo cáo (không rời màn Lập). Tham chiếu: CF_07.1. |
| 25 | Lưu nháp | Button | | | | Luôn Enabled. Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]"). Sau khi lưu: các NĐT khác trong dự án sẽ thấy bản ghi này kèm Tooltip. Tham chiếu: CMR_02. |
| 26 | Nộp báo cáo | Button | | | | Luôn Enabled. Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |

---

### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu: CF_01 (Lập báo cáo), CMR_18, CF_04 (Xuất báo cáo), CF_05 (In), CF_07 (Xem chi tiết), CF_07.1 (Popup PDF Preview — nút [Xem preview] trong màn hình tạo mới).

**Xử lý đặc thù biểu mẫu I.15:**

- Quy trình nộp: Báo cáo I.15 theo quy trình **2 bước** (Nộp → Tiếp nhận). Khi NĐT nộp thành công, trạng thái chuyển sang **"Đã tiếp nhận"** (CMR_03).
- Khởi tạo màn hình: Form mở ra với section Thông tin chung đã được tự động điền (Từ tháng / Đến tháng / Năm dựa trên kỳ hiện tại). Trường Dự án cho phép chọn bất kỳ lúc nào — không bắt buộc ngay khi mở. Các trường dữ liệu từ API giữ trạng thái Disabled cho đến khi Dự án được chọn. Tham chiếu: CF_01.
- Chọn Dự án: Ngay khi chọn, hệ thống gọi API và điền tự động các trường tại Phần I (bao gồm danh sách NĐT) và render bảng Phần II với số hàng NĐT tương ứng. Các trường API sau khi điền → trạng thái Disabled (Khóa). Tham chiếu: CF_01 (mục "Xử lý chọn Phạm vi dữ liệu nguồn input").
- Đồng bộ Phần I ↔ Phần II: Số hàng NĐT trong bảng Phần II luôn bằng số NĐT hiển thị tại Phần I (#9). Dữ liệu NĐT hoàn toàn từ API — không cho phép thêm/xóa thủ công.
- Xử lý xung đột (Tham chiếu: CMR_02): Nếu người dùng chọn Dự án đã có bản ghi báo cáo được tạo bởi NĐT khác trong kỳ hiện tại → Hiển thị Toast lỗi theo CF_01 và danh sách thông báo T06.
- Phần III — Tiến độ thực hiện: Cho phép chọn nhiều giá trị (checkbox). Mỗi option (trừ "Đúng tiến độ") khi được tick sẽ hiển thị textarea Lý do tương ứng. Khi bỏ tick → textarea ẩn và dữ liệu bị xóa.

---


## UC161-166.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ - Xem chi tiết, Xem vòng đời, In, Kết xuất, Nộp, Chỉnh sửa
- Chức năng cho phép người dùng thực hiện các tác vụ bổ trợ tương ứng trạng thái bản ghi. Quyền truy cập được kiểm soát theo CMR_03. Tất cả NĐT trong dự án có quyền ngang nhau trên bản ghi (CMR_02).

Phân quyền: Kiểm soát theo trạng thái bản ghi. Tất cả NĐT trong dự án có quyền ngang nhau (Xem, Chỉnh sửa, Nộp, Xóa, In, Xuất báo cáo) khi bản ghi thỏa điều kiện trạng thái. Tham chiếu: CMR_02, CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC161-166.1) → Cột Hành động → Chọn tác vụ tương ứng

Chức năng đáp ứng usecase số: 163, 164, 165, 166

---

### 2. Mô tả giao diện

**Popup Xem chi tiết**

Tham chiếu: CF_07.

**Popup Xem vòng đời (Audit Trail)**

Tham chiếu: CF_06.

**Các Button theo Action Mapping:**

| # | Tên            | Kiểu  | Điều kiện hiển thị                                          | Phân quyền                  | Mô tả                       |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Chỉ Lưu nháp và Yêu cầu chỉnh sửa | Tất cả NĐT trong dự án (CMR_02) | Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |
| 2 | Chỉnh sửa | Button | Chỉ Lưu nháp và Yêu cầu chỉnh sửa | Tất cả NĐT trong dự án (CMR_02) | Tham chiếu: CF_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Tất cả NĐT trong dự án | Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Tất cả NĐT trong dự án | Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | Tất cả NĐT trong dự án | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Tất cả NĐT trong dự án | Tham chiếu: CF_04. |
| 7 | Xóa | Button | Chỉ Lưu nháp | Tất cả NĐT trong dự án (CMR_02) | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Nộp: Tham chiếu: CF_09. Tham chiếu: CF_01. Cho phép nộp từ Lưu nháp và Yêu cầu chỉnh sửa (CMR_03).
- Chỉnh sửa: Tham chiếu: CF_03.
- Xem chi tiết: Tham chiếu: CF_07. Nút [Chỉnh sửa] ẩn nếu không đủ điều kiện (CMR_03). Nút [Xem trước] → Mở popup PDF Preview. Tham chiếu: CF_07.1.
- Xem vòng đời: Tham chiếu: CF_06.
- In: Tham chiếu: CF_05.
- Xuất báo cáo: .docx. Tham chiếu: CF_04.
- Xóa: Tham chiếu: CF_08.

---




---

## Yêu cầu phi chức năng (NFR)

| Hạng mục | Yêu cầu |
|---|---|
| Performance | Thời gian load danh sách báo cáo ≤ 3 giây. Thời gian phản hồi API auto-fill ≤ 3 giây. |
| Concurrency | Áp dụng Last Write Wins khi nhiều NĐT cùng chỉnh sửa (CMR_02). Mọi thao tác ghi vào Lifecycle Log. |
| Browser Compatibility | Chrome, Edge, Safari phiên bản mới nhất. |
| Audit Trail | Mọi thao tác (Lập, Sửa, Nộp, Xóa) ghi vào Lifecycle Log kèm tên tài khoản + thời gian (CMR_02). |

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-06 | 1.0 → 1.1 | UC161-166.3 — Phân quyền | "NĐT đã khởi tạo bản ghi" | "Tất cả NĐT trong dự án (CMR_02)" | Q1: Đồng bộ với CMR_02 và pattern 5/6 UC ĐTRNN khác |
| 2026-05-06 | 1.0 → 1.1 | UC161-166.2 #6 — Tham chiếu | Tham chiếu: CF_12 | Tham chiếu: CMR_12 (bỏ CF_12) | Q2: CF_12 không tồn tại, inline mô tả |
| 2026-05-06 | 1.0 → 1.1 | UC161-166.2 — Quy trình nộp | (Không xác định) | Quy trình 2 bước → "Đã tiếp nhận" | Q3: NĐT nộp trực tiếp Bộ Tài chính |
| 2026-05-06 | 1.0 → 1.1 | UC161-166.2 — Cấu trúc bảng Phần II | "Nhập tay theo NĐT × chỉ tiêu" | Bổ sung mô tả grid 2 chiều: hàng dynamic theo NĐT, cột con (Tiền/Máy móc/Tài sản khác) | Q4: Wireframe để sau |
| 2026-05-06 | 1.0 → 1.1 | UC161-166.2 #7, #8 — Validate SĐT/Email | (Không đề cập) | "Không validate format — chỉ validate trường bắt buộc" | Q5: Dữ liệu profile API đã đảm bảo |
| 2026-05-06 | 1.0 → 1.1 | UC161-166.2 #16 — Radio toggle | "Ẩn mặc định, hiển thị khi ≠ Đúng tiến độ" | Bổ sung: khi chọn lại "Đúng tiến độ" → textarea ẩn + dữ liệu bị xóa | Q6: Approach 1 |
| 2026-05-06 | 1.0 → 1.1 | UC161-166.2 — Phân quyền kỳ hạn | "Trong thời hạn / Qua kỳ báo cáo" | Chỉ "Trong thời hạn". Qua kỳ → ẩn nút Lập BC (CMR_04) | Q7: Đồng bộ CMR_04 |
| 2026-05-06 | 1.0 → 1.1 | UC161-166.1 #11 — Label NĐT khác | "Đã được lập bởi NĐT khác" (không rõ bản chất) | Bổ sung: đây là label hiển thị, không phải trạng thái. Bộ lọc không bao gồm giá trị này | Q8 |
| 2026-05-06 | 1.0 → 1.1 | UC161-166.1 #6, UC161-166.2 #2 — Kỳ hạn | Tham chiếu: CMR_08 | Inline: "Kỳ I năm [YYYY]" (01/01–30/06), "Kỳ II năm [YYYY]" (01/07–31/12) | Q9: Bỏ CMR_08, inline định nghĩa |
| 2026-05-06 | 1.0 → 1.1 | NFR | (Không có) | Bổ sung section NFR: Performance ≤ 3s, Browser, Concurrency, Audit Trail | Q11 |
| 2026-05-06 | 1.0 → 1.1 | UC161-166.2 #10-13, #16, #17 — Max length | "Không giới hạn độ dài" | Bỏ, follow CMR_05/CMR_06 (default max 500 ký tự) | Q13 |
| 2026-05-07 | 1.1 → 1.2 | Bảng thuộc tính — Phạm vi dữ liệu đầu vào | (Không có) | Có (chọn dự án) | Bổ sung metadata phân loại phạm vi báo cáo |
| 2026-05-07 | 1.1 → 1.2 | Định dạng bảng Markdown | Dòng phân cách không khớp số cột | Sửa dòng phân cách khớp đúng số cột tiêu đề | Chuẩn hóa định dạng Markdown |
| 2026-05-08 | 1.2 → 1.3 | Tên nút Submit | Nộp báo cáo (3 lần) | Nộp báo cáo | Thống nhất tên nút toàn hệ thống |
| 2026-05-11 | +1 | Tên cột | `Ngày cập nhật / Nộp` | `Ngày cập nhật` | Đồng bộ tên cột theo CS_02 (INS-03) |
| 2026-05-11 | +1 | Label Trạng thái kỳ | `Trạng thái (cấp kỳ)` | `Trạng thái kỳ` | Chuẩn hóa tên label (INS-06) |
| 2026-05-11 | +1 | Dòng phân cách bảng Markdown | Thiếu cột (1 chỗ) | Đủ số cột theo header | Chuẩn hóa separator (INS-05) |
| 2026-05-13 | 1.2 → 1.3 | UC161-166.1 — Khung Danh sách kỳ hạn | (Không có) | Bổ sung 2 button: Lập báo cáo (CF_01), Nhập từ file (CF_02) | Bổ sung mô tả UI cho button đã có trong common flow |
| 2026-05-13 | 1.3 → 1.4 | UC161-166.2 — Bổ sung section THÔNG TIN CHUNG | (Không có) | Thêm section Thông tin chung (Từ tháng / Đến tháng / Năm) — auto-calculated, disabled | Theo template UI |
| 2026-05-13 | 1.3 → 1.4 | UC161-166.2 — Tách Dropdown Dự án | Dự án nằm trong Phần I (row #1) | Dự án đứng riêng (row #4), không thuộc phần nào | Cấu trúc lại theo đúng layout UI |
| 2026-05-13 | 1.3 → 1.4 | UC161-166.2 — Phần II đồng bộ NĐT | "Hàng dynamic theo NĐT từ API" | Số hàng NĐT = số NĐT tại Phần I (#9). Dữ liệu hoàn toàn từ API | Làm rõ cơ chế đồng bộ Phần I ↔ Phần II |
| 2026-05-13 | 1.3 → 1.4 | UC161-166.2 — Phần III kiểu trường | Radio Button (single choice) | Checkbox (multiple choice) + mỗi option có textarea Lý do riêng | Cho phép chọn nhiều tiến độ đồng thời |
| 2026-05-17 | 1.4 → 1.5 | Placeholder Search bar (UC161-166.1 #5) | `"Nhập dữ liệu"` | `"Tìm kiếm nhanh theo mã báo cáo"` | Chuẩn hóa theo CMR_06 v2.0 (STD-04b) |
| 2026-05-17 | 1.4 → 1.5 | Required message — Dropdown Dự án (#4) | `"Vui long chon 4 → 1.5"` | `"Vui lòng chọn Dự án"` | Chuẩn hóa theo CMR_07 v2.0 (STD-02a) |
| 2026-05-17 | 1.4 → 1.5 | Required message — Textbox SĐT/Email (#10,#11) | `"Vui long nhap 4 → 1.5"` | `"Vui lòng nhập [tên trường]"` | Chuẩn hóa theo CMR_06 v2.0 (STD-02b) |
| 2026-05-17 | 1.4 → 1.5 | Placeholder Textbox SĐT/Email (#10,#11) | `"Nhap 4 → 1.5"` | `"Nhập số điện thoại"` / `"Nhập email"` | Chuẩn hóa theo CMR_06 v2.0 (STD-04a) |
| 2026-05-17 | 1.4 → 1.5 | Required message + Placeholder — Numeric fields (#13-16) | `"Vui long nhap 4 → 1.5"` / `"Nhap 4 → 1.5"` | `"Vui lòng nhập [tên trường]"` / `"Nhập số tiền (USD)"` + ghi rõ Max length 20 ký tự | Chuẩn hóa theo CMR_05 v2.0 (STD-02b, STD-04a) |
| 2026-05-17 | 1.4 → 1.5 | Required message + Placeholder — Textarea Lý do (#19-21) | `"Vui long nhap 4 → 1.5"` / `"Nhap 4 → 1.5"` | `"Vui lòng nhập [tên trường]"` / `"Nhập lý do [...]"` | Chuẩn hóa theo CMR_06 v2.0 (STD-02b, STD-04a) |
| 2026-05-17 | 1.4 → 1.5 | Required message + Placeholder — Textarea Mô tả (#22) | `"Vui long nhap 4 → 1.5"` / `"Nhap 4 → 1.5"` | `"Vui lòng nhập Mô tả tình hình hiện tại"` / `"Nhập mô tả tình hình hiện tại"` | Chuẩn hóa theo CMR_06 v2.0 |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (3 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them , CMR_18 vao tham chieu CF_01 tren man hinh lap bao cao | Tuan thu CMR_18 Tab Navigation (STD-07) |
| 2026-05-17 | CMR v2.0 | STD-02 Required messages (5 truong) | Truong bat buoc | Vui long nhap/chon [ten truong] | Dong bo CMR_05/06/07 v2.0 |
| 2026-05-17 | CMR v2.0 | STD-04b Search placeholder fix (1) | Tim kiem theo... | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 STD-04b |
| 2026-05-17 | CMR v2.0 | STD-04a Placeholder text/numeric (4 truong) | Nhap du lieu | Nhap [ten truong cu the] | CMR_06 STD-04a |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-18 | 1.5 → 1.6 | Bảng thuộc tính — Loại quy trình | (Không có) | Quy trình 2 bước, CMCĐT_BCTK_03 | Bổ sung metadata loại quy trình |
| 2026-05-22 | CMR Alignment v5 | Numeric precision 15+5 (Fields 13-16); Textarea max 3000 (Fields 19-22); Trailing `.` removed from CMR_07 refs; Buttons "Luôn Enabled" | Đồng bộ CMR_05/06 v2.4 |
