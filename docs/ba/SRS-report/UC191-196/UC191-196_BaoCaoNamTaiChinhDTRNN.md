# UC191-196: Báo cáo tình hình hoạt động đầu tư ra nước ngoài cho năm tài chính

| Thuộc tính               | Giá trị                                      |
| --- | --- |
| **BA phụ trách**   | anh.luu                                        |
| **Phân hệ**        | Quản lý đầu tư ra nước ngoài           |
| **Mẫu biểu**       | I.17                                           |
| **Loại báo cáo**  | Định kỳ (Periodically)                      |
| **Hình thức nộp** | Báo cáo đơn lẻ (Single report form)       |
| **Phạm vi dữ liệu đầu vào** | Có (chọn dự án) |
| **Cơ quan nhận**   | Bộ Tài chính                                 |
| **Đối tượng lập** | Nhà đầu tư (ĐTRNN) thuộc dự án đang hoạt động tại nước ngoài |
| **Giao diện**      | User site (Phía người dùng)                    |
| **Ngày tạo**       | 2026-04-27                                     |
| **Phiên bản**      | 1.7                                            |
| **Quy tắc sinh mã báo cáo** | ODI_I17_[ID]                                     |
| **Loại quy trình** | Quy trình 2 bước, CMCĐT_BCTK_03 |

---

## UC191-196.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo tình hình hoạt động đầu tư ra nước ngoài cho năm tài chính
- Chức năng cho phép Nhà đầu tư truy cập màn hình chính để theo dõi danh sách các báo cáo định kỳ năm, được nhóm theo từng Năm báo cáo. Áp dụng luồng nghiệp vụ Case B (ĐTRNN).

Phân quyền: Nhà đầu tư (ĐTRNN) thuộc dự án đang hoạt động tại nước ngoài.

Truy cập chức năng: Phân hệ Báo cáo → Quản lý đầu tư ra nước ngoài → Báo cáo tình hình hoạt động đầu tư ra nước ngoài cho năm tài chính

Chức năng đáp ứng usecase số: 191, 192, 193, 194, 195, 196

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện:

**Periodic-single**: Giao diện mẫu cho báo cáo có kỳ hạn (theo năm) và gửi lẻ từng báo cáo

Mô tả giao diện:

| #                                                     | Tên trường           | Kiểu trường              | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả                                                                                                                                                                                                                                                                                                         |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm**        |                         |                             |                       |              |            |                                                                                                                                                                                                                                                                                                                 |
| 1                                                     | Năm                     | Yearpicker                  | Năm hiện tại       | x            |            | Người dùng nhấp để chọn năm từ calendar picker. Hệ thống lọc và nhóm danh sách theo năm được chọn. Kết quả hiển thị ngay lập tức sau khi chọn, không cần nhấn thêm nút. Tham chiếu: CMR_07.                                                                                    |
| 2                                                     | Trạng thái kỳ hạn       | Multiple-selection Dropdown | Null                  | x            |            | Lọc theo trạng thái của kỳ hạn. Người dùng chọn một hoặc nhiều giá trị: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_04, CMR_07., CMR_16                                                                                        |
| 3                                                     | Trạng thái báo cáo  | Multiple-selection Dropdown | Null                  | x            |            | Lọc theo trạng thái của bản ghi báo cáo. Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07., CMR_16                                                                                        |
| 4                                                     | Dự án                 | Multiple-selection Dropdown | Null                  | x            |            | Hệ thống cung cấp danh sách Dự án để chọn (không cho phép nhập tự do). Chọn một hoặc nhiều dự án để lọc. Kết quả hiển thị ngay sau khi chọn. Tham chiếu: CMR_07., CMR_16                                                                                                                    |
| 5                                                     | Mã báo cáo           | Search bar                  | Null                  | x            |            | Nhập liệu tự do để tìm theo mã báo cáo. Kết quả hiển thị ngay khi nhập. Nếu không tìm thấy kết quả: hiển thị màn hình trắng với text "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |                                                                                     |
| **Khung Danh sách Báo cáo**  |                         |                             |                       |              |            |                                                                                                                                                                                                                                                                                                                 |
| 6                                                     | Mã báo cáo           | Label                       | Null                  |              |            | Hiển thị mã báo cáo do hệ thống sinh theo quy tắc. Tham chiếu: CMR_09.                                                                                                                                                                                                                                 |
| 7                                                     | Tên dự án            | Label                       | Null                  |              |            | Hiển thị tên đầy đủ của dự án đầu tư ra nước ngoài.                                                                                                                                                                                                                                             |
| 8                                                    | Ngày cập nhật | Label                       | Null                  |              |            | Hiển thị ngày giờ của thao tác gần nhất (Tạo mới / Chỉnh sửa / Lưu nháp / Nộp). Định dạng: dd/MM/yyyy HH:mm.                                                                                                                                                                                  |
| 9                                                    | Trạng thái báo cáo  | Label                       | Null                  |              |            | Trạng thái cấp bản ghi. Tham chiếu: CMR_03. Riêng trạng thái "Đã được lập bởi NĐT khác" hiển thị Tooltip với nội dung: *"Báo cáo kỳ này đã được lập bởi [Tên đầy đủ NĐT A]."* Tham chiếu: CMR_02. |
| 10                                                    | Hành động            | Button group                | Null                  |              |            | Hiển thị các nút thao tác theo trạng thái bản ghi. Chi tiết tham chiếu: UC191-196.3.                                                                                                                                                                                                                  |
| **Nút hành động**                    |                         |                             |                       |              |            |                                                                                                                                                                                                                                                                                                                 |
| 11                                                    | Lập báo cáo          | Button                      | —                     |              |            | Click: Mở màn hình Tạo mới (UC191-196.2). Tham chiếu: CMR_04.                                                                                                                    |
| 12                                                    | Nhập từ file               | Button                      | —                     |              |            | Click: Mở dialog chọn file Excel template → validate format → fill form. Tham chiếu: CMR_04.                                                                                                                    |

---

### 3. Mô tả các xử lý của chức năng

- Yêu cầu về hiển thị tại khung danh sách:
  - Hệ thống tự động nhóm danh sách theo Năm báo cáo.
  - Thực hiện phân trang cho danh sách nhóm năm. Tham chiếu: CMR_10.
  - Sắp xếp giảm dần theo thời gian (năm mới nhất lên đầu).
- Thao tác lọc & tìm kiếm:
  - Tất cả bộ lọc (Năm, Trạng thái kỳ hạn, Trạng thái báo cáo, Dự án) và ô tìm kiếm Mã báo cáo đều hiển thị kết quả ngay lập tức sau khi người dùng tương tác, không cần nhấn thêm nút xác nhận.
  - Nếu không có kết quả: màn hình trắng hiển thị text "Không tìm thấy kết quả".
- Xử lý quyền theo kỳ hạn (Tham chiếu: CMR_04):
  - Nút [Lập báo cáo] và [Nhập từ file] **chỉ hiển thị khi kỳ ở trạng thái Trong thời hạn**. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo.
  - Khi NĐT chọn Dự án đã có bản ghi báo cáo được tạo bởi NĐT khác trong kỳ hiện tại → Hiển thị Toast lỗi (theo CF_01). Không ẩn nút — mỗi NĐT vẫn có thể lập báo cáo cho Dự án khác. Tham chiếu: CMR_02.

---

## UC191-196.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Tạo mới báo cáo tình hình hoạt động đầu tư ra nước ngoài cho năm tài chính
- Chức năng cho phép Nhà đầu tư nhập liệu và khởi tạo báo cáo theo đúng biểu mẫu I.17. Dữ liệu từ API và IRC được tự động điền sau khi người dùng chọn Dự án. Tham chiếu: CF_01.

Phân quyền: Nhà đầu tư (ĐTRNN) chỉ được phép tạo báo cáo khi kỳ hạn ở trạng thái **Trong thời hạn**. Ẩn nút [Lập báo cáo] khi kỳ ở trạng thái Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CMR_04.

Truy cập chức năng: Màn danh sách báo cáo (UC191-196.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 191, 192

---

### 2. Mô tả giao diện

**Giao diện thêm mới**

Giao diện: Màn hình tạo mới theo biểu mẫu I.17.

Mô tả giao diện:


| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **Chọn Dự án** | | | | | | |
| 1 | Dự án | Dropdown | Null | x | x | Người dùng chọn Dự án từ danh sách. Ngay khi chọn, hệ thống gọi API và điền tự động các trường liên quan. Nếu Lưu nháp/Nộp mà chưa chọn: hiển thị lỗi "Vui lòng chọn Dự án". Tham chiếu: CF_01, CMR_07. |
| **THÔNG TIN NHÀ ĐẦU TƯ** | | | | | | |
| 2 | Báo cáo tình hình hoạt động dự án đầu tư tại nước ngoài đến ngày | Datepicker | Từ API | | x | Tự động điền từ API sau khi chọn Dự án. Định dạng dd/MM/yyyy. Trạng thái trường theo CMR_12. Placeholder: "Ngày". |
| 3 | Nhà đầu tư 1 — Tên nhà đầu tư | Textbox | Từ API | | x | Tự động điền từ API sau khi chọn Dự án. Hiển thị tên NĐT thứ nhất thuộc dự án. Trạng thái trường theo CMR_12. Placeholder: "Nhập tên nhà đầu tư". |
| 4 | Nhà đầu tư 2 — Tên nhà đầu tư | Textbox | Từ API | | | Tự động điền từ API sau khi chọn Dự án. Hiển thị tên NĐT thứ hai (nếu có). Trạng thái trường theo CMR_12. Placeholder: "Nhập tên nhà đầu tư". |
| 5 | Số giấy chứng nhận đăng ký đầu tư ra nước ngoài | Textbox | Từ API | | x | Tự động điền từ API sau khi chọn Dự án. Trạng thái trường theo CMR_12. Placeholder: "Nhập số giấy chứng nhận đăng ký đầu tư ra nước ngoài". |
| 6 | Ngày cấp | Datepicker | Từ API | | x | Tự động điền từ API sau khi chọn Dự án. Định dạng dd/MM/yyyy. Trạng thái trường theo CMR_12. |
| 7 | Điều chỉnh lần ... ngày ... | Textbox | Từ API | | x | Tự động điền từ API sau khi chọn Dự án. Ví dụ: "lần 2 ngày 20/04/2026". Trạng thái trường theo CMR_12. Placeholder: "Nhập Điều chỉnh lần ... ngày ... (Ví dụ: lần 2 ngày 20/04/2026)". |
| 8 | Tên dự án/tổ chức kinh tế ở nước ngoài | Textbox | Từ API | | | Tự động điền từ API sau khi chọn Dự án. Trạng thái trường theo CMR_12. Placeholder: "Nhập tên dự án/tổ chức kinh tế ở nước ngoài". |
| **Tài khoản chuyển vốn** | | | | | | Sub-header hiển thị: "Tài khoản chuyển vốn bằng tiền mặt ra nước ngoài". |
| 9 | Tài khoản chuyển vốn bằng tiền mặt ra nước ngoài | Textbox | Null | x | x | Nhập tay. Max 255 ký tự.  Placeholder: "Nhập tài khoản chuyển vốn bằng tiền mặt ra nước ngoài". Tham chiếu: CMR_06. |
| 9 | Số tài khoản | Textbox | Null | x | x | Nhập tay. Max 50 ký tự. Hiển thị lỗi "Vui lòng nhập Số tài khoản" nếu để trống. Placeholder: "Nhập số tài khoản". Tham chiếu: CMR_06. |
| 10 | Ngân hàng | Textbox | Null | x | x | Nhập tay. Max 200 ký tự. Hiển thị cạnh nhau (inline) với trường Số tài khoản. Hiển thị lỗi "Vui lòng nhập Ngân hàng" nếu để trống. Placeholder: "Nhập tên ngân hàng". Tham chiếu: CMR_06. |
| **PHẦN I – TÌNH TRẠNG HOẠT ĐỘNG DỰ ÁN** | | | | | | |
| 11 | Tình trạng hoạt động | Textarea | Null | x | x | Nhập tay. Max 3000 ký tự. Người dùng mô tả tình trạng hoạt động hiện tại của dự án. Hiển thị lỗi "Vui lòng nhập Tình trạng hoạt động" nếu để trống. Placeholder: "Nhập tình trạng hoạt động dự án". Tham chiếu: CMR_06. |
| **PHẦN II – ĐÁNH GIÁ KẾT QUẢ ĐẦU TƯ KINH DOANH** | | | | | | |
| 12 | Năm tài chính báo cáo | Yearpicker | Null | x | x | Người dùng chọn năm tài chính từ picker. Hệ thống tự sinh khoảng thời gian: 01/01/[Năm] – 31/12/[Năm]. Hiển thị lỗi "Vui lòng chọn Năm tài chính báo cáo" nếu để trống. Tham chiếu: CMR_06. |
| 13 | Bảng đánh giá hiệu quả | Grid | Null | | | Đơn vị: USD (trừ các ô có ghi chú VND). Bao gồm 2 cột nhập liệu: Cột "Năm tài chính" và Cột "Lũy kế từ đầu". Chi tiết từng chỉ tiêu xem bảng mô tả bên dưới. |
| 14 | Giải trình nghĩa vụ chuyển LN về nước và nghĩa vụ TC với NN VN | Textarea | Null | x | x | Nhập tay. Max 3000 ký tự. Placeholder: "Nhập Giải trình nghĩa vụ chuyển LN về nước và nghĩa vụ TC với NN VN (Giải trình theo quy định pháp luật hiện hành về nghĩa vụ chuyển lợi nhuận về nước)". Tham chiếu: CMR_06. |
| **PHẦN III – KIẾN NGHỊ** | | | | | | |
| 15 | Kiến nghị | Textarea | Null | x | | Optional. Max 3000 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập Kiến nghị". |
| **PHẦN IV – CAM KẾT** | | | | | | |
| 16 | Nhà đầu tư cam kết chịu trách nhiệm hoàn toàn trước pháp luật về tính chính xác, trung thực của các thông tin nêu trong báo cáo này. | Checkbox | Unchecked | x | x* | Người dùng tick xác nhận. Không bắt buộc khi Lưu nháp. Bắt buộc phải tick khi thực hiện Nộp báo cáo. Nếu Nộp mà chưa tick: báo lỗi "Vui lòng nhập [tên trường]". |
| **PHẦN V – ĐÍNH KÈM** | | | | | | |
| 17 | Upload tài liệu đính kèm | File Upload | Null | x | x | Bắt buộc có ít nhất 1 file. Tối đa 5 file. Gửi kèm: Báo cáo tài chính hoặc báo cáo quyết toán thuế hoặc VB có giá trị PL tương đương. Định dạng: PDF, JPG, PNG. Max 10MB/file. Tổng dung lượng ≤ 50MB. Error messages: Vượt số file → "Số lượng file vượt quá giới hạn cho phép (tối đa 5 file)"; Vượt dung lượng → "File vượt quá dung lượng cho phép (tối đa 10MB)"; Sai định dạng → "Định dạng file không được hỗ trợ. Chỉ chấp nhận PDF, JPG, PNG"; Thiếu file → "Vui lòng nhập Upload tài liệu đính kèm". |
| **Các Button** | | | | | | |
| 18 | Hủy | Button | — | | | Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]"). |
| 19 | Xem trước | Button | — | | | Mở popup PDF Preview từ bên trong màn hình Tạo mới. Tham chiếu: CF_07.1. |
| 20 | Lưu nháp | Button | — | | | Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]"). Tham chiếu: CMR_02. |
| 21 | Nộp báo cáo | Button | — | | | Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |

**Bảng chi tiết chỉ tiêu — Bảng đánh giá hiệu quả (Row 13):**

| STT | Chỉ tiêu | Đơn vị | Cột "Năm tài chính" | Cột "Lũy kế từ đầu" | Validate | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Doanh thu | USD | Nhập tay (Textbox) | Disable | ≥ 0 | Placeholder: "Nhập Doanh thu". |
| 2 | Lợi nhuận sau thuế | USD | Nhập tay (Textbox) | Nhập tay (Textbox) | Có thể âm | Placeholder: "Nhập Lợi nhuận sau thuế". |
| 2.1 | Lợi nhuận được chia của NĐT VN | USD | Nhập tay (Textbox) | Nhập tay (Textbox) | ≥ 0; Nếu dòng 2 > 0 thì 2.1 ≤ 2 (hard-block) | Error: "Lợi nhuận được chia không được vượt quá Lợi nhuận sau thuế". Placeholder: "Nhập Lợi nhuận được chia của NĐT VN". |
| 2.1a | + Tái đầu tư ở nước ngoài | USD | Nhập tay (Textbox) | Nhập tay (Textbox) | ≥ 0 | Placeholder: "Nhập + Tái đầu tư ở nước ngoài". |
| 2.1b | + Chuyển về VN | USD | Nhập tay (Textbox) | Nhập tay (Textbox) | ≥ 0 | Placeholder: "Nhập + Chuyển về VN". |
| 2.1c | + Nghĩa vụ với NN VN | VND | Nhập tay (Textbox) | Nhập tay (Textbox) | ≥ 0 | Đơn vị VND. Không tự động quy đổi tỷ giá. Placeholder: "Nhập + Nghĩa vụ với NN VN". |
| 3 | Tình hình, tỷ lệ thu hồi vốn | USD | Nhập tay (Textbox) | Nhập tay (Textbox) | ≥ 0 | Placeholder: "Nhập Tình hình, tỷ lệ thu hồi vốn". |

**Cross-validation cho Bảng đánh giá hiệu quả:**

| Rule | Loại | Điều kiện | Error/Warning | Thời điểm validate |
| --- | --- | --- | --- | --- |
| 2.1 ≤ 2 khi 2 > 0 | Hard-block | Dòng 2 > 0 và Dòng 2.1 > Dòng 2 | "Lợi nhuận được chia không được vượt quá Lợi nhuận sau thuế" | Blur + Nộp |
| 2.1a + 2.1b + 2.1c ≤ 2.1 | Soft-warning | Tổng (2.1a + 2.1b + 2.1c) > 2.1 | Tooltip ⚠️: "Tổng các khoản phân bổ (2.1a + 2.1b + 2.1c) vượt quá lợi nhuận được chia (2.1)" | Blur. Không block submit. |

---

### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu: CF_01 (Lập báo cáo), CMR_18, CMR_17, CF_04 (Xuất báo cáo), CF_05 (In), CF_07 (nút [Xem trước] — PDF Preview Popup từ bên trong màn hình).

**Xử lý đặc thù biểu mẫu I.17:**

- Khởi tạo màn hình: Form mở ra với tất cả trường ở trạng thái trống. Trường Dự án cho phép chọn bất kỳ lúc nào. Các trường trong section THÔNG TIN NHÀ ĐẦU TƯ (Báo cáo...đến ngày, Nhà đầu tư 1, Nhà đầu tư 2, Số GCNĐKĐTRNN, Ngày cấp, Điều chỉnh lần...ngày..., Tên dự án/tổ chức kinh tế) giữ trạng thái Disabled cho đến khi Dự án được chọn. Tham chiếu: CF_01, CMR_12.
- Chọn Dự án: Ngay khi chọn, hệ thống gọi API và điền tự động các trường trong section THÔNG TIN NHÀ ĐẦU TƯ. Trạng thái trường sau khi API phản hồi: Tham chiếu: CMR_12. Tham chiếu luồng: CF_01 (mục "Xử lý chọn Phạm vi báo cáo").
- Xử lý xung đột (Tham chiếu: CMR_02): Nếu người dùng chọn Dự án đã có bản ghi báo cáo được tạo bởi NĐT khác trong năm hiện tại → Hiển thị Toast lỗi theo CF_01.
- Cross-validation:
  - 2.1a + 2.1b + 2.1c ≤ 2.1: Khi giá trị (2.1a + 2.1b + 2.1c) lớn hơn 2.1, hiển thị alert icon (⚠️) bên cạnh dòng vi phạm. Khi người dùng hover vào icon sẽ hiển thị warning tooltip: "Tổng các khoản phân bổ (2.1a + 2.1b + 2.1c) vượt quá lợi nhuận được chia (2.1)". Hệ thống **không block** submit, người dùng vẫn có thể nộp thành công. So sánh số thuần, không quy đổi tỷ giá.
  - Lợi nhuận sau thuế (2) có thể âm, nhưng nếu (2) > 0 thì (2.1) ≤ (2). Đây là **hard-block** — chặn submit. Validate inline ngay khi người dùng blur khỏi trường 2.1 (và re-validate khi nhấn Nộp). Error message inline: "Lợi nhuận được chia không được vượt quá Lợi nhuận sau thuế".
  - Cột Lũy kế ≥ Năm TC: áp dụng cho dòng 1 (Doanh thu). Đây là **hard-block** — chặn submit. Validate inline ngay khi người dùng blur khỏi trường Lũy kế (và re-validate khi nhấn Nộp). Error message inline: "Giá trị Luỹ kế phải lớn hơn hoặc bằng giá trị Năm tài chính".
- Cam kết: Checkbox phần IV chỉ bắt buộc khi Nộp. Khi người dùng nhấn Nộp, ngoài popup xác nhận chuẩn của CF_01, hệ thống cũng kiểm tra checkbox phần IV này.

**Postconditions:**

| Hành động hoàn tất | Trạng thái hệ thống |
|---|---|
| Lưu nháp thành công | Bản ghi chuyển trạng thái "Lưu nháp", ghi Lifecycle Log, Toast "Đã lưu báo cáo thành công", quay về Danh sách. |
| Nộp báo cáo thành công | Bản ghi chuyển trạng thái "Chờ duyệt" hoặc "Đã tiếp nhận", ghi Lifecycle Log, Toast "Đã nộp báo cáo thành công", quay về Danh sách. |
| Xóa báo cáo thành công | Bản ghi bị xóa khỏi hệ thống, trạng thái kỳ cập nhật lại, Toast "Đã xóa báo cáo thành công", refresh Danh sách. |
| Xuất báo cáo thành công | File PDF/Excel được tải về máy người dùng, không thay đổi trạng thái bản ghi. |
| In thành công | Mở cửa sổ in trình duyệt, không thay đổi trạng thái bản ghi. |

---

## UC191-196.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ - Xem chi tiết, Xem vòng đời, In, Kết xuất, Nộp, Chỉnh sửa, Xóa
- Chức năng cho phép người dùng thực hiện các tác vụ bổ trợ tương ứng trạng thái bản ghi. Quyền truy cập được kiểm soát theo CMR_03.

Phân quyền: Kiểm soát theo trạng thái bản ghi và vai trò (người khởi tạo / NĐT khác). Áp dụng Case B (ĐTRNN) - Full Permission theo CMR_02. Tất cả các NĐT đều có full quyền tương tác trên bản ghi chung của dự án.

Truy cập chức năng: Màn danh sách báo cáo (UC191-196.1) → Cột Hành động → Chọn tác vụ tương ứng

Chức năng đáp ứng usecase số: 193, 194, 195, 196

---

### 2. Mô tả giao diện

**Màn hình Xem chi tiết (Full-Page View Screen)**

Tham chiếu: CF_07.

- Giao diện: Form đọc (toàn bộ trường Disabled), layout giống hệt màn hình Chỉnh sửa (CF_03).
- Nút **[Chỉnh sửa]**: Điều hướng sang màn hình Chỉnh sửa (CF_03). Chỉ hiển thị khi bản ghi ở trạng thái Lưu nháp hoặc Yêu cầu chỉnh sửa (tất cả NĐT đều thấy). Nếu không thỏa mãn → **ẩn hoàn toàn**. Tham chiếu: CF_07, CMR_02, CMR_03.
- Nút **[Xem trước]**: Mở popup PDF Preview. Tham chiếu: CF_07.1.
- Nút **[Hủy]**: Quay về màn hình Danh sách. Không cần popup xác nhận.

**Popup Xem vòng đời (Audit Trail)**

Tham chiếu: CF_06.

**Các Button theo Action Mapping:**

| # | Tên            | Kiểu  | Điều kiện hiển thị                                          | Phân quyền                  | Mô tả                       |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp            | Button | Chỉ Lưu nháp và Yêu cầu chỉnh sửa                        | Tất cả NĐT trong dự án (CMR_02) | Tham chiếu: CF_09. Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |
| 2 | Chỉnh sửa     | Button | Chỉ Lưu nháp và Yêu cầu chỉnh sửa                        | Tất cả NĐT trong dự án (CMR_02) | Tham chiếu: CF_03. |
| 3 | Xem chi tiết   | Button | Tất cả trạng thái                                            | Tất cả người dùng        | Điều hướng đến màn hình Xem toàn trang (full-page). Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái                                            | Tất cả người dùng        | Tham chiếu: CF_06. |
| 5 | In              | Button | Tất cả trạng thái                                            | Tất cả người dùng        | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo         | Button | Tất cả trạng thái                                            | Tất cả người dùng        | Tham chiếu: CF_04. |
| 7 | Xóa            | Button | Chỉ Lưu nháp **VÀ** chưa từng được nộp (không có lịch sử nộp) | Tất cả NĐT trong dự án (CMR_02) | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết (màn hình View full-page): Tham chiếu: CF_07.
  - Nút [Xem trước] trong màn hình View → Mở popup PDF Preview. Tham chiếu: CF_07.1.
  - Nút [Chỉnh sửa] → Điều hướng sang CF_03. Phân quyền theo CMR_02, CMR_03. **Ẩn hoàn toàn** nếu không đủ điều kiện.
  - Nút [Hủy] → Quay về Danh sách (không cần xác nhận).
- Xem vòng đời: Tham chiếu: CF_06.
- In báo cáo: Tham chiếu: CF_05.
- Xuất báo cáo: Tham chiếu: CF_04.
- Chỉnh sửa báo cáo: Tham chiếu: CF_03.
- Xóa báo cáo: Tham chiếu: CF_08. Khi người dùng nhấn [Xóa], hệ thống hiển thị popup xác nhận với nội dung: "Bạn có chắc chắn muốn xóa báo cáo [Mã báo cáo]?". Nút [Xác nhận]: Xóa bản ghi → Toast "Đã xóa báo cáo thành công" → refresh Danh sách. Nút [Hủy]: Đóng popup, không thực hiện thao tác. Nếu API xóa thất bại: Toast lỗi "Không thể kết nối đến hệ thống. Vui lòng thử lại sau.".

---



---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-07 | 1.0 → 1.1 | Bảng thuộc tính — Phạm vi dữ liệu đầu vào | (Không có) | Có (chọn dự án) | Bổ sung metadata phân loại phạm vi báo cáo |
| 2026-05-07 | 1.0 → 1.1 | Định dạng bảng Markdown | Dòng phân cách không khớp số cột | Sửa dòng phân cách khớp đúng số cột tiêu đề | Chuẩn hóa định dạng Markdown |
| 2026-05-11 | +1 | Tên cột | `Ngày cập nhật / Nộp` | `Ngày cập nhật` | Đồng bộ tên cột theo CS_02 (INS-03) |
| 2026-05-11 | +1 | Label Trạng thái kỳ | `Trạng thái (cấp kỳ)` | `Trạng thái kỳ` | Chuẩn hóa tên label (INS-06) |
| 2026-05-12 | 1.1 → 1.2 | UC191-196.1 — Bảng giao diện | Chỉ có 12 rows | Thêm row 13 [Lập báo cáo], row 14 [Nhập từ file] với điều kiện hiển thị CMR_04 | Bổ sung button thiếu theo audit |
| 2026-05-12 | 1.1 → 1.2 | UC191-196.2 — Row 7 Tình trạng hoạt động | Dropdown 6 options, không có conditional input | Khi chọn "Khác" → hiển thị Textbox nhập tự do (Required, Max 500 ký tự) | Form gốc không fix cứng options |
| 2026-05-12 | 1.1 → 1.2 | UC191-196.2 — Row 9 Năm tài chính báo cáo | Kiểu: Textbox, Placeholder: "Nhập 1 → 1.2 (VD: 01/01/2026 – 31/12/2026)" | Kiểu: Yearpicker. Hệ thống tự sinh khoảng 01/01/[Năm] – 31/12/[Năm] | Đổi sang Yearpicker theo business |
| 2026-05-12 | 1.1 → 1.2 | UC191-196.2 — Row 18 Dòng 3 thu hồi vốn | `Validate: ≥ 0` | `Đơn vị: USD. Validate: ≥ 0.` | Ghi rõ đơn vị USD |
| 2026-05-12 | 1.1 → 1.2 | UC191-196.2 — Cross-validation | Không có error message, không phân loại hard/soft | Bổ sung error message cụ thể: Lũy kế < Năm TC → hard-block; (2)>0 mà (2.1)>(2) → hard-block; 2.1a+b+c > 2.1 → soft-warning với tooltip | Audit Q2: thiếu expected result |
| 2026-05-12 | 1.1 → 1.2 | UC191-196.2 — Postconditions | (Không có) | Thêm bảng Postconditions cho Lưu nháp, Nộp, Xóa, Xuất báo cáo, In | Audit: thiếu postcondition |
| 2026-05-12 | 1.1 → 1.2 | UC191-196.3 — Xóa báo cáo | Chỉ ghi "Tham chiếu: CF_08" | Bổ sung nội dung popup xác nhận, Toast thành công/thất bại | Audit Q11: thiếu mô tả popup |
| 2026-05-12 | 1.2 → 1.3 | UC191-196.2 — Row 10 Ngày có BCTC | Không có error message | Bổ sung: Error "Ngày không được vượt quá ngày hiện tại" | Audit Q8: thiếu error message |
| 2026-05-12 | 1.2 → 1.3 | UC191-196.2 — Row 21 Checkbox cam kết | Label bị cắt "...về tính chính xác..." | Full text: "Nhà đầu tư cam kết chịu trách nhiệm hoàn toàn trước pháp luật về tính chính xác, trung thực của các thông tin nêu trong báo cáo này." | Audit Q9: cần text đầy đủ |
| 2026-05-12 | 1.2 → 1.3 | UC191-196.2 — Row 22 File Upload | Chỉ ghi "Cho phép upload multi-file" | Bổ sung: Tối đa 5 file, tổng ≤ 50MB, error messages cho vượt số file/dung lượng/sai định dạng | Audit Q10: thiếu upper boundary |
| 2026-05-12 | 1.2 → 1.3 | UC191-196.2 — Row 19 Giải trình | Placeholder: "Nhập 2 → 1.3 (Nghị định 103/2026/NĐ-CP)" | Placeholder: "Nhập 2 → 1.3 (Nghị định 103/2026/NĐ-CP)" | Audit Q12: tên văn bản pháp lý chưa xác minh |
| 2026-05-14 | 1.3 → 1.4 | UC191-196.2 — Section HEADER | HEADER – THÔNG TIN DỰ ÁN (3 rows: Mã GCNĐKĐTRNN, Ngày cấp, Tên dự án — Label từ API) | THÔNG TIN NHÀ ĐẦU TƯ (6 rows: Nhà đầu tư 1, Nhà đầu tư 2, Số GCNĐKĐTRNN, Ngày cấp, Điều chỉnh lần...ngày..., Tên dự án/tổ chức kinh tế — Textbox từ API) | Bổ sung section Thông tin NĐT theo giao diện thực tế |
| 2026-05-14 | 1.3 → 1.4 | UC191-196.2 — Tài khoản chuyển vốn | Row 5: "Số tài khoản chuyển vốn", Row 6: "Ngân hàng mở tài khoản" | Sub-header "Tài khoản chuyển vốn bằng tiền mặt ra nước ngoài". Row 8: "Số tài khoản", Row 9: "Ngân hàng" (inline) | Cấu trúc lại theo giao diện thực tế |
| 2026-05-14 | 1.3 → 1.4 | UC191-196.2 — Phần I Tình trạng hoạt động | Dropdown 6 options + Textarea "Mô tả chi tiết" (2 rows) | Textarea đơn thuần (1 row, Max 1000 ký tự) | Giao diện thực tế chỉ có 1 textarea |
| 2026-05-14 | 1.3 → 1.4 | UC191-196.2 — Phần II Row "Ngày có BCTC" | Datepicker. Validate: ≤ ngày hiện tại | Yearpicker "Ngày có báo cáo tài chính". Validate: ≤ năm hiện tại | Đổi sang Yearpicker theo giao diện thực tế |
| 2026-05-14 | 1.3 → 1.4 | UC191-196.2 — Phần II Bảng đánh giá hiệu quả | Mô tả từng chỉ tiêu dạng rows trong bảng giao diện chính | Tách thành bảng chi tiết riêng với cột STT, Chỉ tiêu, Đơn vị, Validate, Ghi chú + bảng Cross-validation | Mô tả rõ ràng hơn theo cấu trúc grid thực tế |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (3 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them , CMR_18 vao tham chieu CF_01 tren man hinh lap bao cao | Tuan thu CMR_18 Tab Navigation (STD-07) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_17 (Upload File Dinh kem) | Chua co CMR_17 | Them CMR_17 vao tham chieu man hinh Lap bao cao | UC co chuc nang upload file dinh kem (CMR_17) |
| 2026-05-17 | CMR v2.0 | STD-02 Required messages (6 truong) | Truong bat buoc | Vui long nhap/chon [ten truong] | Dong bo CMR_05/06/07 v2.0 |
| 2026-05-17 | CMR v2.0 | STD-02 Required message (cleanup) | Truong bat buoc | Vui long nhap [ten truong] | Dong bo CMR v2.0 |
| 2026-05-17 | CMR v2.0 | STD-04a Placeholder text/numeric (8 truong) | Nhap du lieu | Nhap [ten truong cu the] | CMR_06 STD-04a |
| 2026-05-17 | CMR v2.0 | STD-04a Custom Placeholder | 4 truong khong chuan | Dong bo Nhap [ten truong] (Goi y) | CMR_06 |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-18 | 1.4 → 1.5 | Bảng thuộc tính — Loại quy trình | (Không có) | Quy trình 2 bước, CMCĐT_BCTK_03 | Bổ sung metadata loại quy trình |
| 2026-05-21 | 1.5 → 1.6 | UC191-196.2 — Section THÔNG TIN NHÀ ĐẦU TƯ | (Không có) | Thêm Row 2 "Báo cáo tình hình hoạt động dự án đầu tư tại nước ngoài đến ngày" (Datepicker, từ API, dd/MM/yyyy) | Bổ sung field theo giao diện thực tế |
| 2026-05-21 | 1.5 → 1.6 | UC191-196.2 — Phần II Row "Ngày có báo cáo tài chính" | Yearpicker "Ngày có báo cáo tài chính". Validate ≤ năm hiện tại. CMR_11 | (Đã xóa) | Doc mô tả thừa field — không có trên giao diện thực tế |
| 2026-05-22 | 1.6 → 1.7 | Field 9 Tài khoản chuyển vốn — Max length | Max 100 ký tự | Max 255 ký tự | Align CMR: CMR_06 (A06) — Textbox max 255 |
| 2026-05-22 | 1.6 → 1.7 | Field 14 Giải trình nghĩa vụ — Max length | Max 2000 ký tự | Max 3000 ký tự | Align CMR: CMR_06 (A06) — Textarea max 3000 |
| 2026-05-22 | 1.6 → 1.7 | Field 11 Tình trạng hoạt động — Max length | Max 1000 ký tự | Max 3000 ký tự | Align CMR: CMR_06 (A06) — Textarea max 3000 |
| 2026-05-22 | 1.6 → 1.7 | Field 15 Kiến nghị — Max length | Max 1000 ký tự | Max 3000 ký tự | Align CMR: CMR_06 (A06) — Textarea max 3000 |
