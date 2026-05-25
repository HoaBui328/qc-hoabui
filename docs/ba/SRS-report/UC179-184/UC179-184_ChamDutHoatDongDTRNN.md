# UC179-184: Thông báo về việc chấm dứt hoạt động đầu tư ra nước ngoài — Mẫu I.20

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | anh.luu |
| **Phân hệ** | Quản lý đầu tư ra nước ngoài |
| **Mẫu biểu** | Mẫu I.20 |
| **Loại báo cáo** | Không định kỳ (Ad-hoc) |
| **Hình thức nộp** | Báo cáo đơn lẻ |
| **Phạm vi dữ liệu đầu vào** | Có (chọn dự án) |
| **Cơ quan nhận** | NHNN / Bộ Tài chính |
| **Đối tượng lập** | Nhà đầu tư (NĐT) |
| **Giao diện** | User site |
| **Ngày tạo** | 2026-04-25 |
| **Phiên bản** | 1.4 |
| **Quy tắc sinh mã báo cáo** | ODI_I20_[ID] |
| **Loại quy trình** | Quy trình 2 bước, CMCĐT_BCTK_03 |

> **Lưu ý kiến trúc:** Báo cáo **không định kỳ** — danh sách phẳng, không nhóm theo kỳ hạn. Nút [Tạo mới] đặt trực tiếp trên header màn hình Danh sách. Phân quyền theo **CMR_02 (ĐTRNN):** tất cả NĐT có full quyền thao tác trên bản ghi đã tạo; chỉ 1 NĐT khởi tạo; mọi thao tác ghi vào Lifecycle Log. Checkbox **CAM KẾT** là trường bắt buộc trong form — phải tick trước khi Nộp thành công.

### Objective

Cho phép Nhà đầu tư (NĐT) có dự án ĐTRNN lập và nộp thông báo về việc chấm dứt hoạt động đầu tư ra nước ngoài theo Mẫu I.20 (Nghị định 103/2026/NĐ-CP), gửi NHNN / Bộ Tài chính qua hệ thống MBFS.

### In Scope

- Xem danh sách thông báo chấm dứt (UC179-184.1)
- Lập mới thông báo theo biểu mẫu I.20 (UC179-184.2)
- Chỉnh sửa thông báo ở trạng thái Lưu nháp / Yêu cầu chỉnh sửa (UC179-184.3)
- Nộp thông báo (UC179-184.3)
- Xem chi tiết, Xem vòng đời, In, Xuất báo cáo (UC179-184.3)
- Xóa thông báo (chỉ khi Lưu nháp và chưa từng nộp) (UC179-184.3)

### Out of Scope

- Quy trình duyệt/tiếp nhận phía cơ quan (NHNN / Bộ Tài chính)
- Nhập từ file báo cáo (không đề cập trong UC này)
- Quản lý trạng thái dự án ĐTRNN
- Trigger thông báo/email đến cơ quan tiếp nhận

### Preconditions

1. NĐT đã đăng nhập thành công vào hệ thống MBFS (User site).
2. NĐT có ít nhất 1 dự án ĐTRNN (hoặc sử dụng option "Khác" cho dự án chưa có GCNĐK trên hệ thống).
3. Hệ thống có kết nối API để lấy thông tin dự án (Master Data / IRC).

### Postconditions

| Sau khi hoàn thành... | Trạng thái hệ thống |
| --- | --- |
| Lập mới + Lưu nháp | Bản ghi mới trong danh sách, trạng thái "Lưu nháp". Toast: *"Đã lưu báo cáo thành công"*. |
| Lập mới + Nộp | Trạng thái → **"Đã tiếp nhận"** (quy trình 2 bước, CMR_03). Bản ghi khóa vĩnh viễn (không Sửa/Xóa/Nộp lại). Lifecycle Log ghi nhận. |
| Chỉnh sửa + Lưu nháp | Dữ liệu cập nhật, trạng thái bảo toàn (Lưu nháp → Lưu nháp / YCCS → YCCS). Toast: *"Đã chỉnh sửa báo cáo thành công"*. |
| Chỉnh sửa + Nộp | Trạng thái → "Đã tiếp nhận". Bản ghi khóa vĩnh viễn. |
| Xóa | Bản ghi xóa khỏi danh sách. Toast: *"Xóa báo cáo thành công"*. |
| Xuất báo cáo | File .docx tải xuống thành công. Toast: *"Đã xuất báo cáo thành công"*. |

**Quy trình nộp:** Báo cáo Mẫu I.20 theo quy trình **2 bước** (Nộp → Tiếp nhận). Khi NĐT nộp thành công, trạng thái chuyển sang **"Đã tiếp nhận"** (CMR_03).

---

## UC179-184.1: Xem Danh Sách Thông Báo

### 1. Mô tả chức năng

- Tên chức năng: Xem danh sách thông báo chấm dứt hoạt động ĐTRNN (Mẫu I.20)
- Chức năng cho phép Nhà đầu tư (NĐT) xem danh sách các thông báo đã lập, lọc theo Năm / Trạng thái / Dự án.

Phân quyền: Nhà đầu tư (NĐT). Tham chiếu: CMR_02.

Truy cập chức năng: Phân hệ Báo cáo → Quản lý ĐTRNN → Thông báo chấm dứt hoạt động đầu tư ra nước ngoài (Mẫu I.20)

Chức năng đáp ứng usecase số: 179, 180, 181, 182, 183, 184

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện: **Non-periodic** — Danh sách phẳng, phân trang theo bản ghi. Không nhóm theo kỳ hạn.

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | | |
| 1 | Năm | Yearpicker | Năm hiện tại | x | | Lọc theo năm của Ngày cập nhật bản ghi gần nhất. Kết quả hiển thị ngay. Tham chiếu: CMR_07. |
| 2 | Trạng thái báo cáo | Multiple-selection Dropdown | Null | x | | Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07., CMR_16 |
| 3 | Dự án | Multiple-selection Dropdown | Null | x | | Lọc theo tên/mã dự án. Kết quả hiển thị ngay. Tham chiếu: CMR_07., CMR_16 |
| 4 | Mã báo cáo | Search bar | Null | x | | Tìm theo mã báo cáo. Hiển thị ngay khi nhập. Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| **Khung Danh sách Báo cáo** | | | | | | |
| 6 | Mã báo cáo | Label | Null | | | Tham chiếu: CMR_09. |
| 7 | Tên dự án | Label | Null | | | Tên dự án liên kết; "Khác" nếu chọn option thủ công. |
| 8 | Ngày cập nhật | Label | Null | | | Định dạng: dd/MM/yyyy HH:mm. |
| 9 | Trạng thái | Label | Null | | | Tham chiếu: CMR_03. |
| 10 | Hành động | Button group | Null | | | Chi tiết: UC179-184.3. |
| **Header màn hình** | | | | | | |
| 11 | Tạo mới | Button | Null | | | Hiển thị trực tiếp trên header. Báo cáo không định kỳ — không có kỳ hạn, không phụ thuộc CMR_04. Tham chiếu: CF_01, CMR_18, CMR_17. |
| 12 | Nhập từ file | Button | Null | | | Hiển thị trực tiếp trên header. Báo cáo không định kỳ — không có kỳ hạn, không phụ thuộc CMR_04. Tham chiếu: CF_01, CMR_18, CMR_17. |

---

### 3. Mô tả các xử lý của chức năng

- Danh sách hiển thị phẳng, sắp xếp mặc định theo Ngày cập nhật giảm dần. Tham chiếu: CMR_10.
- Tất cả bộ lọc hiển thị kết quả ngay lập tức. Tham chiếu: CMR_07.
- Nút [Tạo mới] Tất cả trạng thái trên header (báo cáo không định kỳ, không phụ thuộc kỳ hạn).
- **Empty State:** Khi danh sách không có bản ghi nào (hoặc bộ lọc không trả kết quả): Hiển thị text *"Không tìm thấy kết quả"* ở giữa vùng bảng.
- **Phân trang:** Mặc định 10 bản ghi/trang. Options: 10, 20, 50, 100. Thanh phân trang cố định cuối danh sách. Tham chiếu: CMR_10.

---


## UC179-184.2: Lập Báo Cáo Thông Báo

### 1. Mô tả chức năng

- Tên chức năng: Tạo mới thông báo chấm dứt hoạt động ĐTRNN (Mẫu I.20)
- Chức năng cho phép NĐT lập thông báo theo biểu mẫu I.20, bao gồm thông tin chấm dứt, dữ liệu vốn auto-fill từ IRC, checkbox cam kết bắt buộc và đính kèm tài liệu. Tham chiếu: CF_01, CMR_18, CMR_17.

Phân quyền: Nhà đầu tư (NĐT). Tham chiếu: CMR_02.

Truy cập chức năng: Màn danh sách báo cáo (UC179-184.1) → Nhấn nút [Tạo mới]

Chức năng đáp ứng usecase số: 179, 180

---

### 2. Mô tả giao diện

**Giao diện tạo mới**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **PHẦN PHẠM VI BÁO CÁO** | | | | | | |
| 1 | Dự án | Dropdown | Null | x | x | Danh sách dự án ĐTRNN của NĐT đăng nhập. Bao gồm option **"Khác"** (dành cho dự án chưa có GCNĐK). Khi chọn dự án: auto-fill các trường từ IRC. Placeholder: "Chọn dự án". Tham chiếu: CMR_12. |
| **PHẦN THÔNG TIN NHÀ ĐẦU TƯ** | | | | | | Card riêng. Có nút [+ Thêm nhà đầu tư] ở góc phải header. |
| 2 | Tên nhà đầu tư | Text (Repeatable) | Null | x | x | Danh sách nhà đầu tư — cho phép thêm nhiều dòng. Mỗi dòng gồm: label "Nhà đầu tư [N]" + trường "Tên nhà đầu tư*" + icon Xóa (🗑). Ít nhất 1 nhà đầu tư bắt buộc. Placeholder: "Nhập tên nhà đầu tư". Auto-fill từ IRC khi chọn dự án; Enabled khi chọn "Khác". |
| 3 | Cơ quan cấp Văn bản đăng ký xác nhận giao dịch ngoại hối | Text | Null | x | x | Placeholder: "Nhập tên cơ quan cấp". Tham chiếu: CMR_06. |
| 4 | Số Văn bản đăng ký xác nhận giao dịch ngoại hối | Text | Auto-fill IRC | x | x | Disabled khi chọn dự án. Enabled + Required khi chọn "Khác" hoặc khi API IRC trả null. Placeholder: "Nhập số văn bản". Tham chiếu: CMR_12. |
| 5 | Ngày cấp | Date Picker | Auto-fill IRC | x | x | Disabled khi chọn dự án. Enabled + Required khi chọn "Khác" hoặc khi API IRC trả null. Hiển thị cùng hàng với mục 4. Tham chiếu: CMR_12. |
| **PHẦN THÔNG TIN CHẤM DỨT ĐẦU TƯ** | | | | | | Card riêng. |
| 6 | Quốc gia/vùng lãnh thổ tiếp nhận đầu tư | Dropdown | Null | x | x | Danh mục quốc gia/vùng lãnh thổ từ Master Data. Tham chiếu: CMR_07. |
| 7 | Văn bản chấp thuận chấm dứt — Số văn bản | Text | Null | x | | Nằm trong sub-card "Văn bản chấp thuận chấm dứt". Optional. Placeholder: "Nhập số văn bản". Max 255 ký tự. Lỗi: *"Số văn bản không được vượt quá 255 ký tự!"*. Tham chiếu: CMR_06. |
| 8 | Văn bản chấp thuận chấm dứt — Ngày | Date Picker | Null | x | | Hiển thị cùng hàng với mục 7. Optional. Validate: <= Ngày hôm nay (nếu có giá trị). Tham chiếu: CMR_05. |
| 9 | Vốn đầu tư ra nước ngoài (USD) | Number | 0 | x | x | Decimal >= 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số. Suffix: "USD". Tham chiếu: CMR_11. |
| 10 | Vốn đã chuyển ra nước ngoài (USD) | Number | 0 | x | x | Decimal >= 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số. Suffix: "USD". Validate: <= Vốn đầu tư ra nước ngoài (mục 9). Tooltip: "Tổng lũy kế vốn đã chuyển ra nước ngoài tính đến thời điểm chấm dứt". Tham chiếu: CMR_05, CMR_11. |
| 11 | Vốn đã chuyển về Việt Nam (USD) | Number | 0 | x | x | Decimal >= 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số. Suffix: "USD". Tooltip: "Bao gồm thu hồi vốn và các khoản thu từ thanh lý". Tham chiếu: CMR_05, CMR_11. |
| 12 | Ngày chấm dứt hoạt động | Date Picker | Null | x | x | Required. Validate: (1) <= Ngày hôm nay; (2) >= Ngày cấp (mục 5). Tham chiếu: CMR_05. |
| 13 | Lý do chấm dứt | Textarea | Null | x | x | Required. Max 3000 ký tự. Placeholder: "Nhập lý do chấm dứt hoạt động đầu tư". Tham chiếu: CMR_06. |
| **PHẦN CAM KẾT** | | | | | | Card riêng. Checkbox bắt buộc tick trước khi Nộp. |
| 14 | Checkbox cam kết | Checkbox | Unchecked | x | x | Nhãn: *"Nhà đầu tư cam kết đã hoàn thành việc thanh lý dự án đầu tư tại nước ngoài và chuyển về nước toàn bộ các khoản thu từ việc thanh lý dự án đầu tư (nếu có) theo quy định tại Điều 29 Nghị định 103/2026/NĐ-CP"*. Required khi Nộp. Có thể Lưu nháp khi chưa tick. Nếu chưa tick khi nhấn [Nộp báo cáo]: hiển thị lỗi inline màu đỏ bên dưới checkbox: *"Bạn cần xác nhận cam kết trước khi nộp"*. |
| **PHẦN TÀI LIỆU GỬI KÈM** | | | | | | Card riêng. Drag & drop upload area. |
| 15 | Tài liệu gửi kèm | File upload (Drag & Drop) | Null | x | x | Required (ít nhất 1 file khi Nộp). Định dạng: PDF, JPG, PNG. Giới hạn: 10MB/file. Cho phép upload nhiều file. Vùng upload hiển thị: "Kéo thả file vào đây hoặc **chọn file**". Hỗ trợ: PDF, JPG, PNG - Tối đa 10MB/file. Hướng dẫn loại tài liệu: (a) Bản sao Văn bản đăng ký xác nhận giao dịch ngoại hối; (b) Bản sao văn bản chấp thuận chấm dứt hoạt động đầu tư của quốc gia/vùng lãnh thổ tiếp nhận đầu tư / Bản sao văn bản thanh lý hợp đồng (đối với trường hợp đầu tư theo hợp đồng/góp vốn, mua cổ phần, mua phần vốn góp) / Bản sao các văn bản khác có giá trị pháp lý tương đương; (c) Bản sao tài liệu xác nhận về việc đã chuyển vốn về Việt Nam; (d) Bản sao các tài liệu liên quan khác (nếu có). |
| **CÁC NÚT HÀNH ĐỘNG** | | | | | | |
| 16 | Hủy | Button | | | | Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Hủy]"). |
| 17 | Xem trước | Button | | | | Mở popup PDF Preview báo cáo (không rời màn Lập). Tham chiếu: CF_07.1. |
| 18 | Lưu nháp | Button | | | | Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Lưu nháp]"). |
| 19 | Nộp báo cáo | Button | | | | Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Nộp báo cáo]"). Bổ sung validate Checkbox cam kết (mục 14). |


**CÁC BUTTON**

| #  | Tên           | Kiểu   | Điều kiện hiển thị | Phân quyền       | Mô tả                                                                                |
| -- | -------------- | ------- | ----------------------- | -------------------- | ------------------------------------------------------------------------------------- |
| B1 | Hủy           | Button | Luôn                   | Người tạo         | Luôn Enabled. Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Hủy]").                                     |
| B2 | Xem trước | Button | Luôn                   | Người tạo         | Luôn Enabled. Mở popup PDF Preview báo cáo (không rời màn Lập). Tham chiếu: CF_07.1.        |
| B3 | Lưu nháp     | Button | Luôn                   | Người tạo         | Luôn Enabled. Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Lưu nháp]").                                |
| B4 | Nộp báo cáo | Button | Lưu nháp, Yêu cầu CS | Người tạo         | Luôn Enabled. Validate toàn bộ trường bắt buộc + Checkbox cam kết (mục 14) trước khi nộp. Tham chiếu: CF_01, CMR_18, CMR_17.         |
---



### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu: CF_01, CMR_18, CF_04 (Xuất báo cáo), CF_05 (In).

**A. Xử lý chọn Phạm vi báo cáo:**
- Khi chọn dự án từ Dropdown: Auto-fill Tên nhà đầu tư (mục 2), Số VB ĐKGDNH (mục 4), Ngày cấp (mục 5) từ IRC — Disabled. Tham chiếu: CMR_12.
- Khi chọn **"Khác"**: Tất cả trường auto-fill chuyển sang Enabled, Required — người dùng nhập thủ công.
- Khi thay đổi dự án sau khi đã điền:
  - Nếu form đã có dữ liệu (dirty): Popup xác nhận *"Thay đổi dự án sẽ xóa dữ liệu auto-fill hiện tại. Tiếp tục?"* → [Xác nhận] / [Hủy].
  - Nếu [Xác nhận]: Xóa toàn bộ dữ liệu auto-fill (mục 2, 4, 5). Giữ nguyên dữ liệu NĐT đã nhập thủ công (mục 6–13). Gọi API mới cho dự án vừa chọn.
  - Nếu [Hủy]: Đóng popup, giữ nguyên dự án cũ và toàn bộ dữ liệu.
  - Nếu form chưa có dữ liệu (clean): Chuyển dự án ngay, không hiển thị popup.

**A1. Xử lý khi API IRC không trả về dữ liệu (CMR_12):**
- Khi chọn dự án cụ thể (không phải "Khác") nhưng API trả về dữ liệu rỗng (null): Các trường auto-fill (mục 2, 4, 5) chuyển sang **Enabled** — NĐT nhập thủ công. Trường vẫn Required. Tham chiếu: CMR_12.
- Khi API gọi thất bại (lỗi kết nối): Hiển thị Toast lỗi — Tiêu đề: *"Lỗi hệ thống"*, Nội dung: *"Không thể kết nối đến hệ thống. Vui lòng thử lại sau."*. Các trường auto-fill giữ trạng thái Disabled.

**B. Validate Vốn:**
- Mục 10 (Vốn đã chuyển ra nước ngoài) <= Mục 9 (Vốn đầu tư ra nước ngoài). Nếu vi phạm → lỗi inline: *"Vốn đã chuyển ra nước ngoài không được vượt quá vốn đăng ký"*.

**C. Validate Ngày chấm dứt (mục 12):**
- Điều kiện 1: <= Ngày hôm nay. Nếu vi phạm → lỗi inline: *"Ngày chấm dứt không được là ngày trong tương lai"*.
- Điều kiện 2: >= Ngày cấp (mục 5). Nếu vi phạm → lỗi inline: *"Ngày chấm dứt không được sớm hơn ngày cấp GCNĐKĐTRNN/VB ĐKGDNH"*.

**D. Xử lý Checkbox cam kết (mục 14) — Bổ sung vào CF_01 Nộp:**
- Người dùng có thể **Lưu nháp mà không cần tick** checkbox. Tham chiếu: CF_01, CMR_18, CMR_17.
- Khi nhấn [Nộp báo cáo]: Hệ thống validate checkbox **trước** các validate khác (Bước 0 trong luồng CF_01). Nếu chưa tick → hiển thị lỗi inline màu đỏ bên dưới checkbox: *"Bạn cần xác nhận cam kết trước khi nộp"*. Dừng luồng, không mở popup xác nhận.
- Nếu đã tick → tiếp tục luồng Nộp bình thường theo CF_01.

**E. Phần TÀI LIỆU GỬI KÈM:**
- Tối thiểu 1 file khi Nộp. Nếu không có file → lỗi inline: *"Vui lòng đính kèm ít nhất 1 tài liệu"*.
- Hướng dẫn loại tài liệu hiển thị dưới dạng danh sách gợi ý (không bắt buộc upload theo đúng thứ tự/loại).

**F. Xử lý section THÔNG TIN NHÀ ĐẦU TƯ (mục 2):**
- Mặc định hiển thị 1 dòng "Nhà đầu tư 1".
- Nhấn [+ Thêm nhà đầu tư]: Thêm 1 dòng mới "Nhà đầu tư [N+1]".
- Nhấn icon Xóa (🗑) trên dòng: Xóa dòng đó. Nếu chỉ còn 1 dòng → không cho xóa (ít nhất 1 nhà đầu tư bắt buộc).
- Khi Nộp: Validate ít nhất 1 nhà đầu tư có "Tên nhà đầu tư" không rỗng.

**G. Xuất báo cáo:** Kết xuất file **.docx**. Tham chiếu: CF_04.

**H. Quy trình nộp:** Báo cáo Mẫu I.20 theo quy trình **2 bước** (Nộp → Tiếp nhận). Khi NĐT nộp thành công, trạng thái chuyển sang **"Đã tiếp nhận"** (CMR_03).

**I. Concurrency (CMR_02):**
- Báo cáo ad-hoc: Không giới hạn 1 bản ghi/dự án. NĐT có thể tạo nhiều thông báo chấm dứt cho cùng 1 dự án.
- Xung đột đồng thời: Nếu 2 NĐT cùng mở chỉnh sửa cùng bản ghi → **Last Write Wins** (CMR_02). Cả 2 đều được ghi vào Lifecycle Log.

**J. Tích hợp hệ thống:**

| Module | Loại | Mô tả |
| --- | --- | --- |
| IRC (API) | Read-only | Auto-fill dữ liệu Tên nhà đầu tư, Số VB ĐKGDNH, Ngày cấp theo dự án. |
| Master Data | Read-only | Danh mục Quốc gia/vùng lãnh thổ, Danh sách dự án ĐTRNN. |
| Lifecycle Log | Write | Ghi nhận mọi thao tác (Tạo, Sửa, Nộp, Xóa) kèm Tên NĐT + Timestamp. |
| Xuất báo cáo Engine | Read-only | Kết xuất file .docx theo biểu mẫu I.20. |

---


## UC179-184.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

- Tên chức năng: Các tác vụ bổ trợ — Xem chi tiết, Chỉnh sửa, Nộp, Xem vòng đời, In, Xuất báo cáo
- Phân quyền: **CMR_02** — tất cả NĐT có full quyền Chỉnh sửa, Nộp, Xem; không phân biệt người khởi tạo. Mọi thao tác ghi vào Lifecycle Log.

Truy cập chức năng: Màn danh sách báo cáo (UC179-184.1) → Cột Hành động

Chức năng đáp ứng usecase số: 181, 182, 183, 184

---

### 2. Mô tả giao diện

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Lưu nháp & Yêu cầu chỉnh sửa | Tất cả NĐT trong dự án. Tham chiếu: CMR_02. | Tham chiếu: CF_01, CMR_18, CMR_17. Bổ sung validate Checkbox cam kết (mục 14) trước popup xác nhận. |
| 2 | Chỉnh sửa | Button | Lưu nháp & Yêu cầu chỉnh sửa | Tất cả NĐT. Tham chiếu: CF_03, CMR_02. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Tất cả người dùng | Lifecycle Log ghi nhận tất cả NĐT. Tham chiếu: CF_06, CMR_02. |
| 5 | In | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Tất cả người dùng | Kết xuất file .docx. Tham chiếu: CF_04. |
| 7 | Xóa | Button | Lưu nháp **VÀ** chưa từng nộp | Người tạo | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Chỉnh sửa: Tham chiếu: CF_03. **Tất cả NĐT** đều có quyền theo CMR_02. Mọi thao tác ghi Lifecycle Log.
- Nộp từ Màn hình danh sách: Tham chiếu: CF_09. Bổ sung: validate Checkbox cam kết trước khi hiển thị popup xác nhận. Nếu chưa tick → mở màn hình Chỉnh sửa và hiển thị lỗi inline tại checkbox.

**Luồng Nộp từ Màn hình danh sách (CF_09) — Chi tiết:**
1. NĐT nhấn [Nộp] tại cột Hành động.
2. Hệ thống validate toàn bộ dữ liệu theo thứ tự bên dưới.
3a. Nếu PASS: Hiển thị Popup xác nhận Nộp (theo CF_01).
3b. Nếu FAIL: Mở màn hình Chỉnh sửa, hiển thị lỗi inline tại từng trường vi phạm. Scroll/focus vào lỗi đầu tiên.

**Thứ tự validate khi Nộp (áp dụng cho cả Nộp từ form và Nộp từ danh sách):**

| Bước | Validate | Thông báo lỗi |
| --- | --- | --- |
| 0 | Checkbox cam kết (mục 14) đã tick? | Inline: *"Bạn cần xác nhận cam kết trước khi nộp"* |
| 1 | Ít nhất 1 file đính kèm (mục 15)? | Inline: *"Vui lòng đính kèm ít nhất 1 tài liệu"* |
| 2 | Ít nhất 1 nhà đầu tư có tên (mục 2)? | Inline: *"Vui lòng nhập Ít nhất 1 nhà đầu tư có tên (mục 2)?"* |
| 3 | Tất cả trường Required có giá trị? | Inline: *"Vui lòng nhập Tất cả trường Required có giá trị?"* |
| 4 | Vốn chuyển ra (mục 10) <= Vốn đầu tư ra nước ngoài (mục 9)? | Inline: *"Vốn đã chuyển ra nước ngoài không được vượt quá vốn đăng ký"* |
| 5 | Ngày chấm dứt (mục 12) <= Ngày hôm nay? | Inline: *"Ngày chấm dứt không được là ngày trong tương lai"* |
| 6 | Ngày chấm dứt (mục 12) >= Ngày cấp (mục 5)? | Inline: *"Ngày chấm dứt không được sớm hơn ngày cấp GCNĐKĐTRNN/VB ĐKGDNH"* |
| 7 | Ngày VB chấp thuận (mục 8, nếu có giá trị) <= Ngày hôm nay? | Inline: *"Ngày VB chấp thuận không được là ngày trong tương lai"* |
| 8 | Popup xác nhận (CF_01) | — |
- Xem chi tiết: Tham chiếu: CF_07.
- Xem vòng đời: Tham chiếu: CF_06. Timeline ghi nhận đầy đủ Tên NĐT + Timestamp.
- In báo cáo: Tham chiếu: CF_05.
- Xuất báo cáo: Kết xuất file **.docx**. Tham chiếu: CF_04.


---

## UC179-184.4: Yêu cầu phi chức năng (NFR)

| # | Category | Requirement |
| --- | --- | --- |
| NFR-01 | Performance | Thời gian load danh sách ≤ 3 giây (điều kiện mạng bình thường). |
| NFR-02 | Performance | Thời gian auto-fill từ API IRC ≤ 2 giây sau khi chọn dự án. |
| NFR-03 | File Upload | Hỗ trợ upload file tối đa 10MB/file. Định dạng: PDF, JPG, PNG. Không giới hạn số lượng file. |
| NFR-04 | Browser | Hỗ trợ Chrome, Firefox, Edge, Safari (2 phiên bản mới nhất). |
| NFR-05 | Audit Trail | Mọi thao tác ghi (Tạo, Sửa, Nộp, Xóa) phải được log đầy đủ vào Lifecycle Log kèm Tên NĐT + Timestamp. Tham chiếu: CF_06, CMR_02. |
| NFR-06 | Concurrency | Hệ thống áp dụng Last Write Wins khi 2 NĐT cùng chỉnh sửa đồng thời (CMR_02). |

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-07 | 1.0 → 1.1 | Header — Phiên bản | 1.0 | 1.1 | Update theo kết quả audit QC |
| 2026-05-07 | 1.0 → 1.1 | Bổ sung Objective & Scope | (Không có) | Thêm section Objective, In Scope, Out of Scope | Explicit hóa phạm vi UC |
| 2026-05-07 | 1.0 → 1.1 | Bổ sung Preconditions & Postconditions | (Không có) | Thêm 3 Preconditions + bảng Postconditions + Quy trình nộp 2 bước → "Đã tiếp nhận" | Đồng bộ pattern UC161-166, UC167-172 |
| 2026-05-07 | 1.0 → 1.1 | UC179-184.1 Field 1 — Năm (Mô tả) | Lọc theo năm của Ngày chấm dứt hoạt động | Lọc theo năm của Ngày cập nhật bản ghi gần nhất | Đồng bộ pattern UC173-178 (ad-hoc ĐTRNN). Tránh bản ghi Lưu nháp "biến mất" |
| 2026-05-07 | 1.0 → 1.1 | UC179-184.1 Mục 3 — Empty State + Pagination | (Không có) | Bổ sung: Empty State "Không tìm thấy kết quả" + Phân trang 10/20/50/100 (CMR_10) | Explicit hóa UI behavior |
| 2026-05-07 | 1.0 → 1.1 | UC179-184.2 Mục 3A — Thay đổi dự án | Popup xác nhận ngắn gọn | Chi tiết: dirty check, xóa auto-fill, giữ dữ liệu thủ công, gọi API mới | Explicit hóa UX flow |
| 2026-05-07 | 1.0 → 1.1 | UC179-184.2 Mục 3 — API IRC null (CMR_12) | (Không có) | Bổ sung mục A1: Khi API trả null → Enabled nhập thủ công. Khi API fail → Toast lỗi, giữ Disabled | Explicit hóa CMR_12 cho UC này |
| 2026-05-07 | 1.0 → 1.1 | UC179-184.2 Mục 3 — Quy trình nộp + Concurrency + Integration | (Không có) | Bổ sung mục G (2 bước → Đã tiếp nhận), H (Last Write Wins), I (bảng tích hợp hệ thống) | Đồng bộ pattern UC161-166, UC167-172 |
| 2026-05-07 | 1.0 → 1.1 | UC179-184.3 mục 1 — Phân quyền [Nộp] | Người tạo | Tất cả NĐT trong dự án. Tham chiếu: CMR_02. | Đồng bộ CMR_02 (BA đã xác nhận ở UC161-166, UC167-172) |
| 2026-05-07 | 1.0 → 1.1 | UC179-184.3 Mục 3 — CF_09 + Thứ tự validate | Mô tả ngắn gọn | Bổ sung luồng CF_09 chi tiết + bảng thứ tự validate 7 bước | Explicit hóa luồng Nộp từ danh sách |
| 2026-05-07 | 1.0 → 1.1 | Bổ sung UC179-184.4 — NFR | (Không có) | Thêm section NFR: Performance, File Upload, Browser, Audit Trail, Concurrency | Bổ sung yêu cầu phi chức năng |
| 2026-05-07 | 1.1 → 1.2 | Bảng thuộc tính — Phạm vi dữ liệu đầu vào | (Không có) | Có (chọn dự án) | Bổ sung metadata phân loại phạm vi báo cáo |
| 2026-05-07 | 1.1 → 1.2 | Định dạng bảng Markdown | Dòng phân cách không khớp số cột | Sửa dòng phân cách khớp đúng số cột tiêu đề | Chuẩn hóa định dạng Markdown |
| 2026-05-11 | +1 | Điều kiện hiển thị nút | `Luôn hiển thị` | `Tất cả trạng thái` | Chuẩn hóa điều kiện (INS-07) |
| 2026-05-13 | 1.2 → 1.3 | UC179-184.2 — Xóa field "Đơn vị tiếp nhận" | Dropdown, Required (field #2) | (Đã xóa) | Không có trên UI thực tế |
| 2026-05-13 | 1.2 → 1.3 | UC179-184.2 — Thay "Tên NĐT" bằng section THÔNG TIN NHÀ ĐẦU TƯ | 1 trường Text/Label đơn lẻ | Section repeatable: nhiều nhà đầu tư + nút [+ Thêm nhà đầu tư] + icon Xóa | Khớp UI: cho phép nhập nhiều nhà đầu tư |
| 2026-05-13 | 1.2 → 1.3 | UC179-184.2 — Thêm field "Cơ quan cấp VB ĐKGDNH" | (Không có) | Text input, Required. Placeholder: "Nhập tên cơ quan cấp" | Trường mới trên UI |
| 2026-05-13 | 1.2 → 1.3 | UC179-184.2 — Đổi label field Số VB | "Số VB xác nhận ĐKGDNH" | "Số Văn bản đăng ký xác nhận giao dịch ngoại hối" | Khớp label trên UI |
| 2026-05-13 | 1.2 → 1.3 | UC179-184.2 — Xóa field "Hình thức chấp thuận chấm dứt" | Dropdown, Required | (Đã xóa) — thay bằng sub-card "Văn bản chấp thuận chấm dứt" chứa Số VB + Ngày (Optional) | Không có trên UI |
| 2026-05-13 | 1.2 → 1.3 | UC179-184.2 — Đổi field Quốc gia | Text/Label, Disabled, auto-fill IRC | Dropdown, Required, label: "Quốc gia/vùng lãnh thổ tiếp nhận đầu tư" | Khớp UI: dropdown chọn quốc gia |
| 2026-05-13 | 1.2 → 1.3 | UC179-184.2 — Đổi field Vốn ĐTRNN đăng ký | Number/Label, Disabled, auto-fill IRC | Number, Enabled, Required, default 0, label: "Vốn đầu tư ra nước ngoài (USD)" | Khớp UI: trường editable |
| 2026-05-13 | 1.2 → 1.3 | UC179-184.2 — Cập nhật nhãn Checkbox cam kết | "...thanh lý dự án và chuyển về nước toàn bộ các khoản thu theo quy định..." | "...thanh lý dự án đầu tư tại nước ngoài và chuyển về nước toàn bộ các khoản thu từ việc thanh lý dự án đầu tư (nếu có) theo quy định..." | Khớp nội dung trên UI |
| 2026-05-13 | 1.2 → 1.3 | UC179-184.2 — Đổi label + UI phần đính kèm | "File đính kèm", File upload | "Tài liệu gửi kèm", Drag & Drop area: "Kéo thả file vào đây hoặc chọn file" | Khớp UI |
| 2026-05-13 | 1.2 → 1.3 | UC179-184.2 — Section grouping | Không phân section rõ ràng | 4 card: THÔNG TIN NHÀ ĐẦU TƯ / THÔNG TIN CHẤM DỨT ĐẦU TƯ / Cam kết / Tài liệu gửi kèm | Khớp layout UI |
| 2026-05-13 | 1.2 → 1.3 | UC179-184.3 — Cập nhật bảng validate | Tham chiếu mục 10–15 (cũ) | Tham chiếu mục 9–15 (mới) + thêm bước validate nhà đầu tư | Đồng bộ số thứ tự field mới |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (2 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_17 (Upload File Dinh kem) | Chua co CMR_17 | Them CMR_17 vao tham chieu CF_01 | UC co phan dinh kem tai lieu (CMR_17) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them CMR_18 vao tham chieu CF_01 | Tuan thu CMR_18 Tab Navigation tren form nhap lieu |
| 2026-05-17 | CMR v2.0 | STD-02 Required messages (2 truong) | Truong bat buoc | Vui long nhap/chon [ten truong] | Dong bo CMR_05/06/07 v2.0 |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-18 | 1.3 → 1.4 | Bảng thuộc tính — Loại quy trình | (Không có) | Quy trình 2 bước, CMCĐT_BCTK_03 | Bổ sung metadata loại quy trình |
| 2026-05-22 | CMR Alignment v5 | Textarea max 2000→3000 (Field 13); Numeric precision 15+5 (Fields 9, 10, 11); Textbox max 100→255 (Field 7); Buttons "Luôn Enabled" | Đồng bộ CMR_05/06 v2.4 |
