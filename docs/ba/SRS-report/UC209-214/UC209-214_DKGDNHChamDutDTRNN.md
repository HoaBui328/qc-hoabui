# UC209-214: Báo cáo về tình hình đăng ký giao dịch ngoại hối và chấm dứt hoạt động đầu tư ra nước ngoài (Mẫu II.5)

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | anh.luu |
| **Phân hệ** | Quản lý đầu tư ra nước ngoài |
| **Mẫu biểu** | II.5 |
| **Loại báo cáo** | Theo sự kiện (Event trigger) |
| **Hình thức nộp** | Báo cáo đơn lẻ |
| **Phạm vi dữ liệu đầu vào** | Không có phạm vi |
| **Cơ quan nhận** | Bộ Tài chính (Cục Đầu tư nước ngoài) |
| **Giao diện** | Admin site |
| **Đối tượng lập** | Ngân hàng Nhà nước Việt Nam |
| **Ngày tạo** | 2026-04-27 |
| **Phiên bản** | 1.7 |
| **Quy tắc sinh mã báo cáo** | ODI_II5_[ID] |
| **Loại quy trình** | Quy trình 3 bước, CMCĐT_BCTK_09 |

> **Lưu ý kiến trúc:** Báo cáo **theo sự kiện (Event trigger)** — không có deadline cố định. Danh sách hiển thị dạng phẳng (CS_02), sắp xếp theo Ngày cập nhật giảm dần. Nút [Lập báo cáo] và [Nhập từ file] hiển thị mọi lúc — không áp dụng CMR_04. Không có trường chọn Dự án. Phân quyền: Người tạo (CMR_03). Không áp dụng CMR_01/CMR_02.

---

## UC209-214.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

- Tên chức năng: Xem danh sách báo cáo tình hình ĐKGDNH và chấm dứt HĐĐTRNN (Mẫu II.5)
- Chức năng cho phép Cán bộ NHNN xem danh sách các báo cáo theo sự kiện. Danh sách hiển thị dạng phẳng, sắp xếp theo Ngày cập nhật giảm dần (mới nhất lên trên).

Phân quyền: Cán bộ Ngân hàng Nhà nước Việt Nam (Admin site). Mỗi tài khoản chỉ thấy bản ghi do mình tạo.

Truy cập chức năng: Phân hệ Báo cáo → Quản lý ĐTRNN → Báo cáo ĐKGDNH và chấm dứt HĐĐTRNN (Mẫu II.5)

Chức năng đáp ứng usecase số: 209, 210, 211, 212, 213, 214

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện: **Non-periodic** — Danh sách phẳng, sắp xếp theo Ngày cập nhật giảm dần. Tham chiếu: CS_02.

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | | |
| 1 | Năm | Yearpicker | Năm hiện tại | x | | Lọc danh sách theo năm (dựa trên Ngày cập nhật bản ghi). Kết quả hiển thị ngay sau khi chọn. Tham chiếu: CMR_07, CS_02. |
| 2 | Trạng thái báo cáo | Multiple-selection Dropdown | Null | x | | Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07., CMR_16 |
| 3 | Mã báo cáo | Search bar | Null | x | | Live Search theo mã báo cáo. Nếu không tìm thấy: "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| **Nút hành động Header** | | | | | | |
| 4 | Lập báo cáo | Button | Null | | | Hiển thị mọi lúc (không conditional). Tham chiếu: CF_01, CMR_18, CMR_17. |
| 5 | Nhập từ file | Button | Null | | | Hiển thị mọi lúc (không conditional). Tham chiếu: CF_02. |
| **Bảng Danh sách Báo cáo** | | | | | | |
| 6 | Mã báo cáo | Label | Null | | | ODI_II5_[ID]. Tham chiếu: CMR_09. |
| 7 | Thời gian | Label | Null | | | Hiển thị thông tin tháng/ quý/ năm đã lập của báo cáo |
| 8 | Ngày cập nhật | Label | Null | | | Định dạng: dd/MM/yyyy HH:mm. |
| 9 | Trạng thái | Label | Null | | | Tham chiếu: CMR_03. |
| 10 | Hành động | Button group | Null | | | Chi tiết: UC209-214.3. |

---

### 3. Mô tả các xử lý của chức năng

- Danh sách hiển thị dạng phẳng (flat list), sắp xếp theo Ngày cập nhật giảm dần. Tham chiếu: CS_02.
- Phân trang theo bản ghi (mặc định 10 bản ghi/trang). Tham chiếu: CMR_10.
- Nút [Lập báo cáo] và [Nhập từ file]: hiển thị mọi lúc trên header màn hình. Không áp dụng CMR_04.
- Tất cả bộ lọc hiển thị kết quả ngay lập tức. Tham chiếu: CMR_07.

---

## UC209-214.2: Lập Báo Cáo

### 1. Mô tả chức năng

- Tên chức năng: Tạo mới báo cáo ĐKGDNH và chấm dứt HĐĐTRNN (Mẫu II.5)
- Chức năng cho phép Cán bộ NHNN lập báo cáo theo biểu mẫu II.5, bao gồm HEADER và 2 bảng động (add/remove rows). Tham chiếu: CF_01, CMR_18, CMR_17.

Phân quyền: Cán bộ NHNN (Admin site). Không áp dụng CMR_04 (báo cáo theo sự kiện — lập bất kỳ lúc nào).

Truy cập chức năng: Màn danh sách báo cáo (UC209-214.1) → Nhấn nút [Lập báo cáo] trên header màn hình

Chức năng đáp ứng usecase số: 209, 210

---

### 2. Mô tả giao diện

**Giao diện tạo mới**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **HEADER** | | | | | | |
| 1 | Đơn vị lập | Label | "Ngân hàng Nhà nước Việt Nam" | | | Giá trị cố định (hardcode). Disabled — không cho phép chỉnh sửa. |
| 2 | Số văn bản | Textbox | Null | x | x | Nhập tay. Max 50 ký tự. Hiển thị lỗi "Vui lòng nhập Số văn bản" nếu để trống. Áp dụng định dạng công văn theo CMR_13 (ký tự cho phép, auto-uppercase, format `/`, `-`). Tham chiếu: CMR_06, CMR_13. Placeholder: "Nhập Số văn bản". |
| 3 | Tháng/ Quý/ Năm | Dropdown | | | Single select mỗi field. Placeholder: "Tháng" /"Quý" /"Năm". Click -> hiển thị dropdown: Tháng: Từ tháng 1 -> tháng 12; Quý: Quý 1 -> Quý 4; Năm: các năm theo thư viện |
| **BẢNG 1 – TÌNH HÌNH CẤP ĐKGDNH** | | | | | | Bảng động. Tối thiểu 1 dòng. Cho phép bảng rỗng khi Nộp. |
| **Quy tắc Add/Remove Row Bảng 1:** | | | | | | Tham chiếu: CMR_15. |
| 4 | Số lượng dự án | Calculated | Auto | | | = count(dòng có dữ liệu Bảng 1). Integer. Disabled, nền xám. Cập nhật real-time khi thêm/xóa dòng. Chỉ đếm dòng đã nhập ≥ 1 trường (dòng trống không tính). |
| 5 | STT | Number | Auto-increment | | | Tự động tăng theo thứ tự dòng. Disabled. |
| 6 | Tên NĐT | Textbox | Null | x | x | Nhập tay. Validate: không rỗng. Tham chiếu: CMR_06. Placeholder: "Nhập Tên NĐT". |
| 7 | Mã số DN / CCCD | Textbox | Null | x | x | Nhập tay. Validate: không rỗng. Tham chiếu: CMR_06. Placeholder: "Nhập Mã số DN / CCCD". |
| 8 | Mã số ĐKGDNH | Textbox | Null | x | x | Nhập tay. Validate: không rỗng. Tham chiếu: CMR_06. Placeholder: "Nhập Mã số ĐKGDNH". |
| 9 | Địa chỉ trụ sở | Textbox | Null | x | x | Nhập tay. Validate: không rỗng. Tham chiếu: CMR_06. Placeholder: "Nhập Địa chỉ trụ sở". |
| 10 | Hình thức ĐT | Textbox | Null | x | x | Nhập tay tự do (freetext). Validate: không rỗng. Tham chiếu: CMR_06. Placeholder: "Nhập Hình thức ĐT". |
| 11 | Mục tiêu HĐ | Textbox | Null | x | x | Nhập tay. Validate: không rỗng. Tham chiếu: CMR_06. Placeholder: "Nhập Mục tiêu HĐ". |
| 12 | Vốn ĐTRNN (USD) | Number | Null | x | x | Nhập tay. Validate: > 0; Tham chiếu: CMR_05, CMR_06. |
| 13 | Quốc gia / vùng lãnh thổ | Dropdown | Null | x | x | Danh mục quốc gia chuẩn từ hệ thống (API Master Data, chuẩn ISO 3166-1). Chọn 1 giá trị. Tham chiếu: CMR_07. |
| **Dòng Tổng Bảng 1** | | | | | | |
| 14 | Tổng Vốn ĐTRNN (USD) | Calculated | Auto | | | = Tổng cột Vốn ĐTRNN (USD) của tất cả dòng dữ liệu. Disabled, nền xám. Cập nhật real-time. |
| **BẢNG 2 – TÌNH HÌNH CHẤM DỨT HĐ ĐTRNN** | | | | | | Bảng động. Tối thiểu 1 dòng. Cho phép bảng rỗng khi Nộp. |
| **Quy tắc Add/Remove Row Bảng 2:** | | | | | | Tham chiếu: CMR_15. Áp dụng độc lập với Bảng 1. |
| 15 | Số lượng dự án | Calculated | Auto | | | = count(dòng có dữ liệu Bảng 2). Integer. Disabled, nền xám. Cập nhật real-time khi thêm/xóa dòng. Chỉ đếm dòng đã nhập ≥ 1 trường (dòng trống không tính). |
| 16 | STT | Number | Auto-increment | | | Tự động tăng. Disabled. |
| 17 | Tên NĐT | Textbox | Null | x | x | Nhập tay. Validate: không rỗng. Tham chiếu: CMR_06. Placeholder: "Nhập Tên NĐT". |
| 18 | Mã số DN / CCCD | Textbox | Null | x | x | Nhập tay. Validate: không rỗng. Tham chiếu: CMR_06. Placeholder: "Nhập Mã số DN / CCCD". |
| 19 | Mã số ĐKGDNH | Textbox | Null | x | x | Nhập tay. Validate: không rỗng. Tham chiếu: CMR_06. Placeholder: "Nhập Mã số ĐKGDNH". |
| 20 | Địa chỉ trụ sở | Textbox | Null | x | x | Nhập tay. Validate: không rỗng. Tham chiếu: CMR_06. Placeholder: "Nhập Địa chỉ trụ sở". |
| 21 | Hình thức ĐT | Textbox | Null | x | x | Nhập tay tự do (freetext). Validate: không rỗng. Tham chiếu: CMR_06. Placeholder: "Nhập Hình thức ĐT". |
| 22 | Mục tiêu HĐ | Textbox | Null | x | x | Nhập tay. Validate: không rỗng. Tham chiếu: CMR_06. Placeholder: "Nhập Mục tiêu HĐ". |
| 23 | Vốn đã chuyển ra NN (USD) | Number | Null | x | x | Nhập tay. Validate: ≥ 0; phần nguyên tối đa 15 chữ số, phần thập phân tối đa 5 chữ số. Tham chiếu: CMR_05, CMR_06. |
| 24 | Quốc gia / vùng lãnh thổ | Dropdown | Null | x | x | Danh mục quốc gia chuẩn từ hệ thống (API Master Data, chuẩn ISO 3166-1). Chọn 1 giá trị. Tham chiếu: CMR_07. |
| **Dòng Tổng Bảng 2** | | | | | | |
| 25 | Tổng Vốn đã chuyển ra NN (USD) | Calculated | Auto | | | = Tổng cột Vốn đã chuyển ra NN (USD) của tất cả dòng dữ liệu. Disabled, nền xám. Cập nhật real-time. |
| **MỤC 3 – ĐỀ XUẤT KIẾN NGHỊ** | | | | | | |
| 26 | Đề xuất, kiến nghị | Textarea | Null | x | | Optional. Max 3000 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập Đề xuất, kiến nghị". |
| **CÁC NÚT HÀNH ĐỘNG** | | | | | | |
| 27 | Hủy | Button | | | | Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Hủy]"). |
| 28 | Xem trước | Button | | | | Popup PDF Preview. Tham chiếu: CF_07.1. |
| 29 | Lưu nháp | Button | | | | Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Lưu nháp]"). |
| 30 | Nộp báo cáo | Button | | | | Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Nộp báo cáo]"). |

---

### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu: CF_01, CMR_18, CF_04 (Xuất báo cáo .docx), CF_05 (In), CF_07.1 (PDF Preview).

**Xử lý đặc thù biểu mẫu II.5:**

- **Khởi tạo màn hình:**
  - Đơn vị lập (mục 1): hardcode "Ngân hàng Nhà nước Việt Nam" — không lấy từ profile.
  - Kỳ báo cáo (mục 3): Dropdown Tháng (1-12) + Yearpicker Năm. Mặc định: Tháng hiện tại, Năm hiện tại. Người dùng có thể thay đổi. Bắt buộc chọn trước khi Nộp.
  - Bảng 1 và Bảng 2: mỗi bảng khởi tạo với 1 dòng trống.

- **Add/Remove Row (áp dụng riêng biệt cho từng bảng):** Tham chiếu: CMR_15. STT tự động tăng, tự động cập nhật lại khi xóa dòng.

- **Dòng Tổng (mỗi bảng):** Auto-sum real-time. Disabled, nền xám. Không cho phép sửa trực tiếp.

- **Số lượng dự án (mỗi bảng):** Calculated field, auto = count(dòng có dữ liệu) trong bảng tương ứng. Cập nhật real-time khi thêm/xóa dòng (CMR_15). Disabled, nền xám. Quy tắc đếm: chỉ đếm dòng đã nhập ≥ 1 trường — dòng trống (chưa nhập bất kỳ trường nào) không tính. Khi bảng rỗng (tất cả dòng đều trống): Số lượng dự án = 0.

- **Validate khi Nộp:**
  - Bảng 1 và Bảng 2 **được phép rỗng** (không có dòng dữ liệu hoặc không phát sinh nghiệp vụ trong kỳ). Không bắt buộc ≥ 1 dòng.
  - Nếu bảng có dữ liệu: tất cả trường Required trên từng dòng phải có giá trị trước khi Nộp.
  - Số văn bản (mục 2) bắt buộc có giá trị.
  - **Quy tắc xử lý dòng rỗng:** Bảng khởi tạo 1 dòng trống. Nếu người dùng KHÔNG nhập bất kỳ trường nào trong dòng đó → hệ thống coi bảng là "rỗng" (0 dòng dữ liệu hợp lệ) → cho phép Nộp mà không báo lỗi required trên dòng trống. Nếu người dùng đã nhập ≥ 1 trường bất kỳ trong dòng → dòng đó được coi là "có dữ liệu" → validate tất cả trường required trên dòng đó.
  - **Lưu ý:** Nút [Xóa hàng] ẩn khi chỉ còn 1 dòng (CMR_15). Người dùng không thể xóa dòng cuối để bảng có 0 dòng trên UI.

- **Validate Vốn ĐTRNN (Bảng 1, mục 11):** > 0. Nếu ≤ 0 → lỗi inline: *"Giá trị phải lớn hơn 0"*.
- **Validate Vốn đã chuyển ra NN (Bảng 2, mục 21):** ≥ 0 (cho phép 0).
- **Xuất báo cáo:** Kết xuất file **.docx**. Tham chiếu: CF_04.

- **Nhập từ file (CF_02):**
  - Người dùng tải template .xlsx từ hệ thống (nút [Tải template]).
  - Điền dữ liệu vào template theo cấu trúc cột tương ứng: Tên NĐT, Mã số DN/CCCD, Mã số ĐKGDNH, Địa chỉ trụ sở, Hình thức ĐT, Mục tiêu HĐ, Vốn (USD), Quốc gia.
  - Upload file → Hệ thống mapping dữ liệu vào Bảng 1 và Bảng 2 tương ứng. Validate dữ liệu sau khi nhập từ file (cùng rule với nhập tay).
  - Nếu file lỗi format hoặc dữ liệu không hợp lệ → hiển thị thông báo lỗi chi tiết theo dòng.

- **Tích hợp hệ thống:**
  - Việc Nộp báo cáo chỉ lưu trữ nội bộ trên hệ thống MBFS. Không liên thông/gọi API gửi dữ liệu sang hệ thống Bộ Tài chính.
  - Danh mục Quốc gia/vùng lãnh thổ: lấy từ API Master Data nội bộ (chuẩn ISO 3166-1).

---

## UC209-214.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

- Tên chức năng: Các tác vụ bổ trợ — Xem chi tiết, Chỉnh sửa, Nộp, Xem vòng đời, In, Xuất báo cáo, Xóa
- Phân quyền theo CMR_03 (người tạo). Không áp dụng CMR_01/CMR_02.

Phân quyền: Cán bộ NHNN sở hữu bản ghi. Tham chiếu: CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC209-214.1) → Cột Hành động

Chức năng đáp ứng usecase số: 211, 212, 213, 214

---

### 2. Mô tả giao diện

**Màn hình Xem chi tiết (Full-Page View Screen)**

Tham chiếu: CF_07.

- Giao diện: Form đọc (toàn bộ trường và bảng Disabled), layout giống hệt màn hình Chỉnh sửa. Hiển thị đầy đủ 2 bảng + dòng Tổng.
- Nút **[Chỉnh sửa]**: Chỉ hiển thị khi bản ghi ở trạng thái Lưu nháp hoặc Yêu cầu chỉnh sửa. Ẩn hoàn toàn nếu không đủ điều kiện. Tham chiếu: CF_07, CMR_03.
- Nút **[Xem trước]**: Popup PDF Preview. Tham chiếu: CF_07.1.
- Nút **[Hủy]**: Quay về Danh sách, không cần xác nhận.

**Action Mapping:**

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Lưu nháp & Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_09. Tham chiếu: CF_01, CMR_18, CMR_03. |
| 2 | Chỉnh sửa | Button | Lưu nháp & Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_03, CMR_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Người tạo | Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Người tạo | Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | Người tạo | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Người tạo | Kết xuất .docx. Tham chiếu: CF_04. |
| 7 | Xóa | Button | Lưu nháp **VÀ** chưa từng nộp | Người tạo | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết: Tham chiếu: CF_07. Nút [Chỉnh sửa] ẩn nếu không đủ điều kiện.
- Chỉnh sửa: Tham chiếu: CF_03. Bảng 1 và Bảng 2 giữ nguyên dữ liệu đã nhập.
- Nộp từ Màn hình danh sách: Tham chiếu: CF_09.
- Xem vòng đời: Tham chiếu: CF_06.
- In: Tham chiếu: CF_05.
- Xuất báo cáo: .docx. Tham chiếu: CF_04.
- Xóa: Tham chiếu: CF_08.

---

## 5. Yêu cầu phi chức năng (Non-functional Requirements)

| # | Hạng mục | Yêu cầu |
| --- | --- | --- |
| 1 | Hiệu năng | Phân trang danh sách theo CMR_10. Bảng động hỗ trợ tối đa 500 dòng/bảng. Xuất báo cáo .docx hoàn tất trong ≤ 5 giây với bảng ≤ 100 dòng. |
| 2 | Bảo mật | Phân quyền theo CMR_03 (chỉ người tạo truy cập bản ghi). Không áp dụng CMR_01/CMR_02. Session timeout theo chuẩn hệ thống. |
| 3 | Tương thích | Hỗ trợ trình duyệt Chrome, Microsoft Edge (2 phiên bản mới nhất). Responsive trên màn hình ≥ 1280px. |
| 4 | Dữ liệu | Danh mục Quốc gia/vùng lãnh thổ đồng bộ từ API Master Data (chuẩn ISO 3166-1). Cache danh mục tối đa 24 giờ. |

---

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-07 | 1.0 → 1.1 | Bảng thuộc tính — Phạm vi dữ liệu đầu vào | (Không có) | Không có phạm vi | Bổ sung metadata phân loại phạm vi báo cáo |
| 2026-05-07 | 1.0 → 1.1 | Định dạng bảng Markdown | Dòng phân cách không khớp số cột | Sửa dòng phân cách khớp đúng số cột tiêu đề | Chuẩn hóa định dạng Markdown |
| 2026-05-08 | 1.1 → 1.2 | Quy tắc Add/Remove Row | Inline rule chi tiết | Tham chiếu: CMR_15 | Chuẩn hóa quy tắc thêm/xóa hàng |
| 2026-05-11 | +1 | Tên cột | `Ngày cập nhật / Nộp` | `Ngày cập nhật` | Đồng bộ tên cột theo CS_02 (INS-03) |
| 2026-05-11 | +1 | Dòng phân cách bảng Markdown | Thiếu cột (1 chỗ) | Đủ số cột theo header | Chuẩn hóa separator (INS-05) |
| 2026-05-12 | 1.2 → 1.3 | Số văn bản | Chỉ validate không rỗng | Bổ sung áp dụng CMR_13 (định dạng công văn) | Giải quyết gap Preconditions |
| 2026-05-12 | 1.2 → 1.3 | Hình thức ĐT (Bảng 1) | Dropdown 5 options | Textbox freetext (đồng nhất với Bảng 2) | Theo yêu cầu nghiệp vụ thực tế |
| 2026-05-12 | 1.2 → 1.3 | Quốc gia / vùng lãnh thổ | "Danh mục chuẩn từ hệ thống" | Bổ sung: API Master Data, chuẩn ISO 3166-1 | Làm rõ nguồn dữ liệu |
| 2026-05-12 | 1.2 → 1.3 | Validate khi Nộp | Chưa rõ xử lý dòng rỗng | Bổ sung quy tắc: dòng chưa nhập = bảng rỗng, cho phép Nộp | Giải quyết mâu thuẫn tối thiểu 1 dòng vs cho phép rỗng |
| 2026-05-12 | 1.2 → 1.3 | Nhập từ file | Chỉ đề cập nút Nhập từ file | Bổ sung mô tả chi tiết: template .xlsx, mapping, validate sau nhập từ file | Tăng tính đầy đủ Integration |
| 2026-05-12 | 1.2 → 1.3 | Tích hợp hệ thống | Không đề cập | Xác nhận: Nộp chỉ lưu nội bộ MBFS, không liên thông BTC | Làm rõ phạm vi tích hợp |
| 2026-05-12 | 1.2 → 1.3 | NFR | Không có | Bổ sung mục 5: Hiệu năng, Bảo mật, Tương thích, Dữ liệu | Bổ sung yêu cầu phi chức năng |
| 2026-05-14 | 1.3 → 1.4 | Loại báo cáo | Định kỳ (Tháng) — 12 kỳ/năm | Theo sự kiện (Event trigger) | Báo cáo NHNN không có deadline cố định |
| 2026-05-14 | 1.3 → 1.4 | Lưu ý kiến trúc | Periodic-single, nhóm Năm/Tháng, CMR_04 conditional | Event trigger, flat list (CS_02), nút hiển thị mọi lúc, bỏ CMR_04 | Chuyển đổi kiến trúc màn hình |
| 2026-05-14 | 1.3 → 1.4 | Giao diện danh sách | Periodic-single (CS_01): filter Trạng thái kỳ hạn, nhóm Năm/Kỳ tháng, nút conditional | Non-periodic (CS_02): flat list, bỏ filter kỳ hạn, nút luôn hiển thị, thêm cột Kỳ báo cáo | Đơn giản hóa UI |
| 2026-05-14 | 1.3 → 1.4 | Phân trang | Theo số năm/trang | Theo bản ghi (10/trang, CMR_10) | Phù hợp flat list |
| 2026-05-14 | 1.3 → 1.4 | Trường Kỳ báo cáo (form lập) | Label auto-fill từ kỳ đang lập, Disabled (CMR_12) | Dropdown Tháng (1-12) + Yearpicker Năm, Enabled, bắt buộc | Người dùng tự chọn kỳ |
| 2026-05-14 | 1.3 → 1.4 | Phân quyền lập báo cáo | Kỳ hạn phải "Trong thời hạn" (CMR_04) | Không áp dụng CMR_04, lập bất kỳ lúc nào | Bỏ ràng buộc kỳ hạn |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (1 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_17 (Upload File Dinh kem) | Chua co CMR_17 | Them CMR_17 vao tham chieu CF_01 | UC co phan dinh kem tai lieu (CMR_17) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them CMR_18 vao tham chieu CF_01 | Tuan thu CMR_18 Tab Navigation tren form nhap lieu |
| 2026-05-17 | CMR v2.0 | STD-02 Required messages (2 truong) | Truong bat buoc | Vui long nhap/chon [ten truong] | Dong bo CMR_05/06/07 v2.0 |
| 2026-05-17 | CMR v2.0 | STD-04a Placeholder text/numeric (14 truong) | Nhap du lieu | Nhap [ten truong cu the] | CMR_06 STD-04a |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-18 | 1.4 → 1.5 | Bảng thuộc tính — Loại quy trình | (Không có) | Quy trình 3 bước, CMCĐT_BCTK_09 | Bổ sung metadata loại quy trình |
| 2026-05-21 | 1.5 → 1.6 | Bảng 1 — Số lượng dự án | (Không có) | Calculated field: auto = count(dòng có dữ liệu Bảng 1). Integer, Disabled, nền xám. Cập nhật real-time khi thêm/xóa dòng. | Bổ sung field theo biểu mẫu II.5, áp dụng phương án auto-sync (rows drive input) |
| 2026-05-21 | 1.5 → 1.6 | Bảng 2 — Số lượng dự án | (Không có) | Calculated field: auto = count(dòng có dữ liệu Bảng 2). Integer, Disabled, nền xám. Cập nhật real-time khi thêm/xóa dòng. | Bổ sung field theo biểu mẫu II.5, áp dụng phương án auto-sync (rows drive input) |
| 2026-05-21 | 1.5 → 1.6 | Section 3 — Xử lý đặc thù | Không đề cập Số lượng dự án | Bổ sung mô tả logic: auto count dòng có dữ liệu, quy tắc đếm, giá trị khi bảng rỗng | Làm rõ hành vi calculated field |
| 2026-05-22 | 1.6 → 1.7 | Bảng 2 Field 23 Vốn đã chuyển ra NN — Decimal precision | ≥ 0; 2 chữ số thập phân | ≥ 0; phần nguyên tối đa 15 chữ số, phần thập phân tối đa 5 chữ số | Align CMR: CMR_05 (C05b) — BA confirmed 15+5 |
| 2026-05-22 | 1.6 → 1.7 | Field 26 Đề xuất kiến nghị — Max length | (Không khai báo max) | Max 3000 ký tự | Align CMR: CMR_06 (A06) — Textarea max 3000 |
