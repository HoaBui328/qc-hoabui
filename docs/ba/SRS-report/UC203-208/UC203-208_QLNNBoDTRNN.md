# UC203-208: Báo cáo tình hình quản lý nhà nước về hoạt động đầu tư ra nước ngoài của các Bộ, ngành có liên quan

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | anh.luu |
| **Phân hệ** | Quản lý đầu tư ra nước ngoài |
| **Mẫu biểu** | II.4 |
| **Loại báo cáo** | Định kỳ (Năm) |
| **Hình thức nộp** | Báo cáo đơn lẻ |
| **Phạm vi dữ liệu đầu vào** | Không có phạm vi |
| **Cơ quan nhận** | Bộ Tài chính (Cục Đầu tư nước ngoài) |
| **Đối tượng lập** | Cán bộ Bộ/cơ quan ngang Bộ (Admin site) |
| **Giao diện** | Admin site |
| **Ngày tạo** | 2026-04-27 |
| **Phiên bản** | 1.3 |
| **Quy tắc sinh mã báo cáo** | ODI_II4_[ID] |
| **Loại quy trình** | Quy trình 3 bước, CMCĐT_BCTK_09 |

> **Lưu ý kiến trúc:** Báo cáo **định kỳ năm** trên **Admin site** — danh sách nhóm theo Năm (CS_01, collapsible). Nút [Lập báo cáo] và [Nhập từ file] hiển thị theo trạng thái kỳ hạn (CMR_04). Không có trường chọn Dự án. Phân quyền theo CMR_03 (người tạo quản lý bản ghi của mình). Không áp dụng CMR_01/CMR_02.

---

## UC203-208.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo tình hình QLNN về HĐĐTRNN của các Bộ, ngành (Mẫu II.4)
- Chức năng cho phép Cán bộ thuộc Bộ/cơ quan truy cập màn hình chính để theo dõi danh sách các báo cáo định kỳ năm, được nhóm theo từng Năm báo cáo. Mỗi kỳ có trạng thái kỳ hạn riêng và kiểm soát hiển thị nút [Lập báo cáo]/[Nhập từ file].

Phân quyền: Cán bộ thuộc Bộ/cơ quan ngang bộ (Admin site). Mỗi tài khoản chỉ thấy bản ghi do mình tạo.

Truy cập chức năng: Phân hệ Báo cáo → Quản lý đầu tư ra nước ngoài → Báo cáo QLNN về HĐĐTRNN các Bộ, ngành (Mẫu II.4)

Chức năng đáp ứng usecase số: 203, 204, 205, 206, 207, 208

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện: **Periodic-single** — Danh sách nhóm theo Năm báo cáo, mặc định collapse, click để expand. Tham chiếu: CS_01.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | | |
| 1 | Năm | Yearpicker | Năm hiện tại | x | | Lọc và nhóm danh sách theo năm báo cáo. Kết quả hiển thị ngay sau khi chọn. Tất cả các năm đều được Enable — người dùng có thể chọn bất kỳ năm nào. Nếu năm không có dữ liệu → danh sách hiển thị trạng thái "Không có dữ liệu". Tham chiếu: CMR_07, CS_01 Mục 2. |
| 2 | Trạng thái kỳ hạn | Multiple-selection Dropdown | Null | x | | Người dùng chọn một hoặc nhiều giá trị: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_04, CMR_07., CMR_16 |
| 3 | Trạng thái báo cáo | Multiple-selection Dropdown | Null | x | | Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07., CMR_16 |
| 4 | Mã báo cáo | Search bar | Null | x | | Nhập liệu tự do tìm theo mã báo cáo (Live Search, debounce 300ms). Nếu không tìm thấy: hiển thị text "Không tìm thấy dữ liệu phù hợp" kèm hình ảnh placeholder theo CS_01 Mục 3. Tham chiếu: CMR_06, CMR_09, CS_01 Mục 3. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| **Khung Kỳ hạn báo cáo (Collapsible Section)** | | | | | | |
| 5 | Năm báo cáo | Label (collapsible) | Mặc định collapse | | | Hiển thị nhãn năm (VD: "Năm 2026"). Mặc định collapse. Click → expand danh sách bản ghi trong kỳ. Tham chiếu: CMR_08. |
| 6 | Trạng thái kỳ hạn | Label | Null | | | Trạng thái kỳ hạn: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| 7 | Lập báo cáo | Button | Null | | | Chỉ hiển thị khi kỳ ở trạng thái **Trong thời hạn**. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CF_01, CMR_04. |
| 8 | Nhập từ file | Button | Null | | | Chỉ hiển thị khi kỳ ở trạng thái **Trong thời hạn**. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CF_02, CMR_04. |
| **Bảng Danh sách Báo cáo (trong mỗi kỳ)** | | | | | | |
| 9 | Mã báo cáo | Label | Null | | | Mã hệ thống sinh tự động ODI_II4_[ID]. Tham chiếu: CMR_09. |
| 10 | Ngày cập nhật | Label | Null | | | Thời điểm thao tác gần nhất. Định dạng: dd/MM/yyyy HH:mm. |
| 11 | Trạng thái | Label | Null | | | Trạng thái bản ghi: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Tham chiếu: CMR_03. |
| 12 | Hành động | Button group | Null | | | Các nút thao tác theo trạng thái bản ghi. Chi tiết: UC203-208.3. |

---

### 3. Mô tả các xử lý của chức năng

- Danh sách nhóm theo Năm báo cáo, mặc định collapse. Người dùng click vào header kỳ để expand. Tham chiếu: CS_01.
- Hiển thị tối đa 10 bản ghi trong mỗi kỳ. Nếu vượt quá 10, kích hoạt scroll dọc bên trong kỳ đó. Tham chiếu: CS_01 Mục 4.
- Sắp xếp mặc định: Năm mới nhất lên trên.
- Tất cả bộ lọc và ô tìm kiếm hiển thị kết quả ngay lập tức, không cần nhấn thêm nút xác nhận. Tham chiếu: CMR_07.
- Nút [Lập báo cáo] và [Nhập từ file]: chỉ hiển thị khi kỳ ở trạng thái **Trong thời hạn**. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CF_01, CF_02, CMR_04.
- Empty states trong mỗi kỳ: Hiển thị text "Không tìm thấy dữ liệu phù hợp" kèm hình ảnh placeholder. Tham chiếu: CS_01 mục 3.

---

## UC203-208.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Tạo mới báo cáo tình hình QLNN về HĐĐTRNN của các Bộ, ngành (Mẫu II.4)
- Chức năng cho phép Cán bộ lập báo cáo theo biểu mẫu II.4, bao gồm thông tin Header và 5 mục nội dung dạng Textarea. Mục 4 có thể đính kèm tài liệu minh chứng. Tham chiếu: CF_01.

Phân quyền: Cán bộ thuộc Bộ/cơ quan (Admin site). Kỳ hạn phải ở trạng thái **Trong thời hạn**. Ẩn nút [Lập báo cáo] khi kỳ ở trạng thái Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CMR_04.

Truy cập chức năng: Màn danh sách báo cáo (UC203-208.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 203, 204

---

### 2. Mô tả giao diện

**Giao diện tạo mới**

Giao diện: Màn hình tạo mới theo biểu mẫu II.4.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **HEADER** | | | | | | |
| 1 | Tên cơ quan | Label | Từ profile tổ chức | | | Auto-fill từ session profile tổ chức của tài khoản đăng nhập (luôn có sẵn sau đăng nhập, không gọi API riêng). Disabled — không cho phép chỉnh sửa. Không áp dụng case null/lỗi của CMR_12. |
| 2 | Số văn bản | Textbox | Null | x | x | Nhập tay. Free-text, max 50 ký tự. Không áp dụng CMR_13. Placeholder: "Nhập Số văn bản (VD: 123/2026/VB-BTC)". Hiển thị lỗi "Vui lòng nhập Số văn bản" nếu để trống. Tham chiếu: CMR_06. |
| 3 | Ngày ký | Datepicker | Null | x | x | Chọn ngày từ calendar. Validate: ≤ ngày hôm nay. Hiển thị lỗi "Vui lòng chọn Ngày ký" nếu để trống; lỗi inline nếu chọn ngày tương lai. Tham chiếu: CMR_06. |
| **NỘI DUNG BÁO CÁO** | | | | | | |
| 5 | 1. Tình hình xây dựng và ban hành chính sách liên quan đến HĐĐTRNN thuộc chức năng của cơ quan | Textarea | Null | x | x | Nhập tay. Max 3000 ký tự. Hiển thị lỗi "Vui lòng nhập [tên trường]" nếu để trống khi Nộp. Tham chiếu: CMR_06. Placeholder: "Nhập Tình hình xây dựng và ban hành chính sách liên quan đến HĐĐTRNN thuộc chức năng của cơ quan". |
| 6 | 2. Tình hình QLNN về ĐTRNN thuộc chức năng của cơ quan | Textarea | Null | x | x | Nhập tay. Max 3000 ký tự. Hiển thị lỗi "Vui lòng nhập Tình hình QLNN về ĐTRNN thuộc chức năng của cơ quan" nếu để trống khi Nộp. Tham chiếu: CMR_06. Placeholder: "Nhập Tình hình QLNN về ĐTRNN thuộc chức năng của cơ quan". |
| 7 | 3. Kiểm tra, thanh tra, giám sát HĐ ĐTRNN thuộc chức năng quản lý | Textarea | Null | x | x | Nhập tay. Max 3000 ký tự. Hiển thị lỗi "Vui lòng nhập Kiểm tra, thanh tra, giám sát HĐ ĐTRNN thuộc chức năng quản lý" nếu để trống khi Nộp. Tham chiếu: CMR_06. Placeholder: "Nhập Kiểm tra, thanh tra, giám sát HĐ ĐTRNN thuộc chức năng quản lý". |
| 8 | 4. Tình hình thực hiện chế độ BC về HĐĐTRNN của NĐT đối với cơ quan | Textarea | Null | x | x | Nhập tay. Max 3000 ký tự. Hiển thị lỗi "Vui lòng nhập Tình hình thực hiện chế độ BC về HĐĐTRNN của NĐT đối với cơ quan" nếu để trống khi Nộp. Tham chiếu: CMR_06. Placeholder: "Nhập Tình hình thực hiện chế độ BC về HĐĐTRNN của NĐT đối với cơ quan". |
| **ĐÍNH KÈM (cho Mục 4)** | | | | | | Tài liệu minh chứng cho Mục 4. |
| 9 | File đính kèm Mục 4 | File Upload | Null | x | | Optional — không bắt buộc. Định dạng chấp nhận: PDF, Excel (.xlsx/.xls), Word (.docx/.doc). Cho phép upload nhiều file. Mỗi file có icon Xóa [✕] để loại bỏ và chọn lại. Tham chiếu: CMR_17. |
| 10 | 5. Đề xuất, kiến nghị | Textarea | Null | x | | Optional. Max 1000 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập Đề xuất, kiến nghị". |
| **CÁC NÚT HÀNH ĐỘNG** | | | | | | |
| 11 | Lưu nháp | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]"). |
| 12 | Xem trước | Button | | | | Mở popup PDF Preview từ bên trong màn hình Tạo mới. Lưu ý: nút này khác với [Xem chi tiết] trên Danh sách (CF_07). Tham chiếu: CF_07.1. |
| 13 | Nộp báo cáo | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |
| 14 | Hủy | Button | | | | Áp dụng CMR_14 (Dirty Form Guard): khi form có thay đổi chưa lưu, hiển thị popup P02 "Dữ liệu chưa được lưu" trước khi rời trang. Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]"), CMR_14. |


**CÁC BUTTON**

| #  | Tên           | Kiểu   | Điều kiện hiển thị | Phân quyền       | Mô tả                                                                                |
| -- | -------------- | ------- | ----------------------- | -------------------- | ------------------------------------------------------------------------------------- |
| B1 | Hủy           | Button | Luôn                   | Người tạo         | Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]").                                     |
| B2 | Xem trước | Button | Luôn                   | Người tạo         | Mở popup PDF Preview báo cáo (không rời màn Lập). Tham chiếu: CF_07.1.        |
| B3 | Lưu nháp     | Button | Luôn                   | Người tạo         | Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]").                                |
| B4 | Nộp báo cáo | Button | Lưu nháp, Yêu cầu CS | Người tạo         | Validate toàn bộ trường bắt buộc trước khi nộp. Tham chiếu: CF_01.         |
---



### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu: CF_01 (Lập báo cáo), CMR_18, CMR_17, CF_04 (Xuất báo cáo), CF_05 (In), CF_07.1 (nút [Xem trước] — PDF Preview Popup từ bên trong màn hình).

**Xử lý đặc thù biểu mẫu II.4:**

- **Khởi tạo màn hình:**
  - Trường Tên cơ quan (mục 1): tự động điền từ session profile tổ chức của tài khoản đăng nhập (luôn có sẵn, không gọi API riêng) → Disabled.
  - Trường Năm báo cáo (mục 4): mặc định điền năm hiện tại → Enabled, cho phép chỉnh sửa.
  - Tất cả trường còn lại: trống, Enabled cho nhập tay.

- **Validate Ngày ký (mục 3):** ≤ ngày hôm nay. Nếu chọn ngày tương lai → lỗi inline: *"Ngày ký không được là ngày trong tương lai"*.

- **Validate Năm báo cáo (mục 4):** Số nguyên 4 chữ số, ≤ năm hiện tại. Nếu nhập ký tự không hợp lệ → lỗi inline: *"Năm báo cáo không hợp lệ"*. Nếu nhập năm > năm hiện tại → lỗi inline: *"Năm báo cáo không được vượt quá năm hiện tại"*.

- **Validate Lưu nháp:** Chỉ validate trường Phạm vi báo cáo (không áp dụng ở đây — không có dự án). Validate duy nhất: ít nhất 1 trường có dữ liệu. Tham chiếu: CF_01.

- **Validate khi Nộp:** Tất cả trường Required (mục 2, 3, 4, 5, 6, 7, 8) phải có giá trị. Mục 10 (Đề xuất, kiến nghị) và Đính kèm (mục 9) không bắt buộc. Tham chiếu: CF_01.

- **Đính kèm Mục 4 (mục 9):** Optional. Cho phép upload nhiều file cùng lúc (tối đa 5 file, tổng dung lượng ≤ 50MB). Cho phép upload file trùng tên. Định dạng: PDF, Excel (.xlsx/.xls), Word (.docx/.doc). Giới hạn 10MB/file. File sai định dạng → lỗi inline: *"Định dạng file không được hỗ trợ. Vui lòng sử dụng PDF, Excel hoặc Word"*. File vượt 10MB → lỗi inline: *"File vượt quá dung lượng cho phép (10MB)"*. Lỗi hiển thị dạng inline error bên dưới khu vực upload.

- **Xuất báo cáo:** Kết xuất file **.docx**. Tên file theo CF_04: `[Mã-Báo-Cáo]_[Kỳ-Báo-Cáo]_[Mã-cơ-quan]`. Mã cơ quan lấy từ session profile tổ chức. VD: `ODI-II4_nam-2026_BKHDT.docx`. Tham chiếu: CF_04.

- **Nhập từ file:** Áp dụng CF_02 Case 2 (không chọn Phạm vi). Template format: .xlsx. Tên file template: `Mau_ODI_II4_[YYYYMMDD]_[HHMM].xlsx`. Tham chiếu: CF_02.

- **Nộp thành công:** Trạng thái chuyển thành **"Chờ duyệt"**. Cục ĐTNN duyệt → chuyển "Đã tiếp nhận" hoặc "Yêu cầu chỉnh sửa". Tham chiếu: CMR_03.

- **Dirty Form Guard:** Màn hình Lập (CF_01) và Chỉnh sửa (CF_03) áp dụng CMR_14. Khi form có thay đổi chưa lưu và user nhấn [Hủy] hoặc navigate ra ngoài → hiển thị popup P02 *"Dữ liệu chưa được lưu"*. Tham chiếu: CMR_14.

---

## UC203-208.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ — Xem chi tiết, Chỉnh sửa, Nộp, Xem vòng đời, In, Xuất báo cáo, Xóa
- Chức năng cho phép Cán bộ thực hiện các tác vụ trên bản ghi của mình theo trạng thái. Áp dụng CMR_03.

Phân quyền: Cán bộ thuộc Bộ/cơ quan (Admin site). Mỗi tài khoản chỉ thao tác trên bản ghi do mình tạo. Áp dụng CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC203-208.1) → Cột Hành động → Chọn tác vụ

Chức năng đáp ứng usecase số: 205, 206, 207, 208

---

### 2. Mô tả giao diện

**Màn hình Xem chi tiết (Full-Page View Screen)**

Tham chiếu: CF_07.

- Giao diện: Form đọc (toàn bộ trường Disabled), layout giống hệt màn hình Chỉnh sửa.
- Nút **[Chỉnh sửa]**: Chỉ hiển thị khi bản ghi ở trạng thái Lưu nháp hoặc Yêu cầu chỉnh sửa. Nếu không thỏa mãn → **ẩn hoàn toàn**. Tham chiếu: CF_07, CMR_03.
- Nút **[Xem trước]**: Mở popup PDF Preview. Tham chiếu: CF_07.1.
- Nút **[Hủy]**: Quay về màn hình Danh sách. Không cần popup xác nhận.

**Các Button theo Action Mapping:**

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Lưu nháp & Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_09. Tham chiếu: CF_01, CMR_03. |
| 2 | Chỉnh sửa | Button | Lưu nháp & Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_03, CMR_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Người tạo | Điều hướng màn hình Xem toàn trang. Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Người tạo | Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | Người tạo | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Người tạo | Kết xuất file .docx. Tham chiếu: CF_04. |
| 7 | Xóa | Button | Chỉ Lưu nháp **VÀ** chưa từng được nộp | Người tạo | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết (màn hình View full-page): Tham chiếu: CF_07.
  - Nút [Xem trước] trong màn hình View → Mở popup PDF Preview. Tham chiếu: CF_07.1. Lưu ý: nút [Xem trước] (PDF Preview) khác với nút [Xem chi tiết] trên Danh sách (mở Full-Page View).
  - Nút [Chỉnh sửa] → Điều hướng sang CF_03. **Ẩn hoàn toàn** nếu không đủ điều kiện trạng thái.
  - Nút [Hủy] → Quay về Danh sách (không cần xác nhận).
- Chỉnh sửa báo cáo: Tham chiếu: CF_03. Áp dụng CMR_14 (Dirty Form Guard).
- Nộp từ Màn hình danh sách: Tham chiếu: CF_09. Nếu validate fail, hệ thống mở màn hình Chỉnh sửa (CF_03) và hiển thị lỗi inline + scroll/focus vào lỗi đầu tiên theo CF_09 Step 3b. Nộp thành công → trạng thái chuyển thành "Chờ duyệt".
- Xem vòng đời: Tham chiếu: CF_06.
- In báo cáo: Tham chiếu: CF_05.
- Xuất báo cáo: Kết xuất file **.docx**. Tên file theo CF_04: `[Mã-Báo-Cáo]_[Kỳ-Báo-Cáo]_[Mã-cơ-quan]`. Mã cơ quan lấy từ session profile tổ chức. VD: `ODI-II4_nam-2026_BKHDT.docx`. Tham chiếu: CF_04.
- Xóa báo cáo: Tham chiếu: CF_08.

---

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-07 | 1.0 → 1.1 | Bảng thuộc tính — Phạm vi dữ liệu đầu vào | (Không có) | Không có phạm vi | Bổ sung metadata phân loại phạm vi báo cáo |
| 2026-05-07 | 1.0 → 1.1 | Định dạng bảng Markdown | Dòng phân cách không khớp số cột | Sửa dòng phân cách khớp đúng số cột tiêu đề | Chuẩn hóa định dạng Markdown |
| 2026-05-11 | +1 | Tên cột | `Ngày cập nhật / Nộp` | `Ngày cập nhật` | Đồng bộ tên cột theo CS_02 (INS-03) |
| 2026-05-11 | +1 | Kiểu field Năm báo cáo | `Number` | `Yearpicker` | Đồng nhất kiểu field (INS-04) |
| 2026-05-11 | +1 | Dòng phân cách bảng Markdown | Thiếu cột (1 chỗ) | Đủ số cột theo header | Chuẩn hóa separator (INS-05) |
| 2026-05-12 | 1.1 → 1.2 | UC203-208.1 mục 1 (Yearpicker) | Không đề cập Enable/Disable | Áp dụng CS_01 Mục 2: chỉ Enable năm có data hoặc năm hiện tại | Q15 |
| 2026-05-18 | 1.2 → 1.3 | UC203-208.1 mục 1 (Yearpicker) | Chỉ Enable năm có data hoặc năm tài chính hiện tại; các năm khác Disabled | Enable toàn bộ tất cả các năm; năm không có data → hiển thị Empty State "Không có dữ liệu". Tham chiếu: CS_01 Mục 2 (v1.7) | Bỏ logic disable năm |
| 2026-05-12 | 1.1 → 1.2 | UC203-208.1 mục 4 (Search bar) | Placeholder "Nhập dữ liệu", empty state "Không tìm thấy kết quả", không debounce | Placeholder "Tìm kiếm theo Mã báo cáo", empty state theo CS_01, debounce 300ms | Q6, Q7, Q8 |
| 2026-05-12 | 1.1 → 1.2 | UC203-208.1 mục 3 (Phân trang) | Tham chiếu CMR_10 (phân trang) | Scroll dọc trong kỳ theo CS_01 Mục 4 | Q9 |
| 2026-05-12 | 1.1 → 1.2 | UC203-208.2 mục 1 (Tên cơ quan) | Tham chiếu CMR_12 | Lấy từ session, không gọi API riêng, không áp dụng case null/lỗi CMR_12 | Q5 |
| 2026-05-12 | 1.1 → 1.2 | UC203-208.2 mục 2 (Số văn bản) | Max 50 ký tự | Free-text, max 50 ký tự, không áp dụng CMR_13 | Q4 |
| 2026-05-12 | 1.1 → 1.2 | UC203-208.2 mục 9 (File đính kèm) | Max 10MB/file, nhiều file | Tối đa 5 file, tổng ≤ 50MB, cho phép trùng tên, inline error | Q11, Q12 |
| 2026-05-12 | 1.1 → 1.2 | UC203-208.2 mục 14 (Hủy) | Chỉ tham chiếu CF_01 | Bổ sung CMR_14 Dirty Form Guard, popup P02 | Q10 |
| 2026-05-12 | 1.1 → 1.2 | UC203-208.2 xử lý — Nộp | "Chờ duyệt" hoặc "Đã tiếp nhận" | Nộp → Chờ duyệt. Cục ĐTNN duyệt → Đã tiếp nhận/YC chỉnh sửa | Q2 |
| 2026-05-12 | 1.1 → 1.2 | UC203-208.2 xử lý — Nhập từ file | Không mô tả | CF_02 Case 2, template .xlsx, naming Mau_ODI_II4_[YYYYMMDD]_[HHMM] | Q13 |
| 2026-05-12 | 1.1 → 1.2 | UC203-208.2 xử lý — Xuất báo cáo | Chỉ tham chiếu CF_04 | Bổ sung tên file: ODI-II4_nam-[YYYY]_[MaCQ].docx | Q16 |
| 2026-05-12 | 1.1 → 1.2 | UC203-208.3 — Nộp từ Danh sách | Chỉ tham chiếu CF_09 | Bổ sung: validate fail → mở Chỉnh sửa + lỗi inline theo CF_09 Step 3b | Q14 |
| 2026-05-12 | 1.1 → 1.2 | UC203-208.3 — Nút [Xem trước] | Không phân biệt rõ với [Xem chi tiết] | Ghi rõ: [Xem] = PDF Preview (CF_07.1), [Xem chi tiết] = Full-Page View (CF_07) | Q3 |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (2 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them , CMR_18 vao tham chieu CF_01 tren man hinh lap bao cao | Tuan thu CMR_18 Tab Navigation (STD-07) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_17 (Upload File Dinh kem) | Chua co CMR_17 | Them CMR_17 vao tham chieu man hinh Lap bao cao | UC co chuc nang upload file dinh kem (CMR_17) |
| 2026-05-17 | CMR v2.0 | STD-02 Required messages (5 truong) | Truong bat buoc | Vui long nhap/chon [ten truong] | Dong bo CMR_05/06/07 v2.0 |
| 2026-05-17 | CMR v2.0 | STD-02 Required message (cleanup) | Truong bat buoc | Vui long nhap [ten truong] | Dong bo CMR v2.0 |
| 2026-05-17 | CMR v2.0 | STD-04b Search placeholder fix (1) | Tim kiem theo... | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 STD-04b |
| 2026-05-17 | CMR v2.0 | STD-04a Placeholder text/numeric (5 truong) | Nhap du lieu | Nhap [ten truong cu the] | CMR_06 STD-04a |
| 2026-05-17 | CMR v2.0 | STD-04a Custom Placeholder | 1 truong khong chuan | Dong bo Nhap [ten truong] (Goi y) | CMR_06 |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-18 | 1.2 → 1.3 | Bảng thuộc tính — Loại quy trình | (Không có) | Quy trình 3 bước, CMCĐT_BCTK_09 | Bổ sung metadata loại quy trình |
