# UC323-328: Tình hình điều chỉnh quyết định chủ trương đầu tư/GCNĐKĐT về vốn và quy mô tại các KCN, KKT trong kỳ báo cáo

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | yen.trinh |
| **Phân hệ** | Báo cáo KKT/KCN |
| **Mẫu biểu** | 2115.H.QLKKT |
| **Loại báo cáo** | Định kỳ quý/năm |
| **Phạm vi báo cáo** | Không có phạm vi |
| **Hình thức nộp** | Báo cáo đơn lẻ (Single report form) |
| **Cơ quan nhận** | Cục Đầu tư nước ngoài |
| **Đối tượng lập** | Ban Quản lý các khu công nghiệp, kinh tế |
| **Giao diện** | Admin site |
| **Ngày tạo** | 2026-04-23 |
| **Phiên bản** | 1.8 |
| **Quy tắc sinh mã báo cáo** | EZ_2115HQLKKT_[ID] |
| **Loại quy trình** | Quy trình > 2 bước, CMCĐT_BCTK_04 |

---

## UC323-328.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo tình hình điều chỉnh quyết định chủ trương đầu tư/GCNĐKĐT về vốn và quy mô tại các KCN, KKT trong kỳ báo cáo
- Chức năng cho phép Ban Quản lý các KCN, KKT truy cập màn hình chính để theo dõi danh sách báo cáo, được nhóm theo từng Kỳ hạn báo cáo.

**Precondition:** Người dùng đã đăng nhập thành công và được phân quyền "Cán bộ chuyên môn Ban Quản lý các khu công nghiệp, kinh tế".

Phân quyền: Ban Quản lý các khu công nghiệp, kinh tế.

Truy cập chức năng: Phân hệ Báo cáo → Báo cáo KKT/KCN → Tình hình điều chỉnh quyết định chủ trương đầu tư/GCNĐKĐT về vốn và quy mô tại các KCN, KKT

Chức năng đáp ứng usecase số: 323, 324, 325, 326, 327, 328

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện: Periodic-single — Giao diện mẫu cho báo cáo có kỳ hạn và gửi lẻ từng báo cáo.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | | |
| 1 | Năm | YearPicker | Null | x | | Lọc danh sách theo năm báo cáo. Kết quả hiển thị ngay khi chọn. |
| 2 | Trạng thái | Multiple-selection Dropdown | Tất cả trạng thái | x | | Lọc theo trạng thái của báo cáo. Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07., CMR_16 |
| 3 | Mã báo cáo | Search bar | Null | x | | Search theo mã báo cáo. Kết quả hiển thị ngay khi nhập. Nếu không tìm thấy kết quả: hiển thị màn hình trắng với text "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| 4 | Trạng thái kỳ | Multiple-selection Dropdown | Null | x | | Lọc theo trạng thái:Chưa tới hạn/ Trong thời hạn/ Qua kỳ báo cáo. Tham chiếu: CMR_04. Tham chiếu: CMR_16. |
| **Khung Danh sách Kỳ hạn** | | | | | | |
| 5 | Kỳ hạn báo cáo | Label | Null | | | Hiển thị tên kỳ hạn. Mặc định ở trạng thái collapse; khi click vào mũi tên sẽ expand ra danh sách các báo cáo đã gửi của kỳ đó. Tham chiếu: CMR_08. |
| 6 | Trạng thái kỳ báo cáo | Label | Null | | | Hiển thị trạng thái kỳ theo thời gian: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| 7 | Lập báo cáo | Button | Null | | | Chỉ hiển thị và enable khi Kỳ báo cáo ở trạng thái "Trong thời hạn", các trạng thái khác của kỳ báo cáo thì button này sẽ bị ẩn đi. Tham chiếu CF_01, CMR_04 |
| 8 | Nhập từ file | Button | Null | | | Chỉ hiển thị và enable khi Kỳ báo cáo ở trạng thái "Trong thời hạn", các trạng thái khác của kỳ báo cáo thì button này sẽ bị ẩn đi. Tham chiếu CF_01, CMR_04 |
| **Khung Danh sách Báo cáo** (trong mỗi kỳ) | | | | | | |
| 9 | Mã báo cáo | Label | Null | | | Hiển thị mã báo cáo do hệ thống sinh theo quy tắc. Tham chiếu: CMR_09. |
| 10 | Ngày cập nhật | Label | Null | | | Hiển thị ngày giờ của thao tác gần nhất (Lưu nháp / Nộp). Định dạng: dd/MM/yyyy HH:mm. |
| 11 | Trạng thái | Label | Null | | | Trạng thái của bản ghi báo cáo. Tham chiếu: CMR_03. |
| 12 | Hành động | Button group | Null | | | Hiển thị các nút thao tác theo trạng thái bản ghi. Chi tiết tham chiếu: UC323-328.3. |

---

### 3. Mô tả các xử lý của chức năng

- Yêu cầu về hiển thị tại khung danh sách kỳ hạn:
  - Hệ thống tự động nhóm danh sách theo Kỳ hạn báo cáo.
  - Sắp xếp báo cáo bên trong mỗi kỳ theo thứ tự từ mới → cũ.
  - Phân trang: Chọn hiển thị số kỳ báo cáo/trang. Tham chiếu: CMR_10.
- Thao tác lọc & tìm kiếm:
  - Tất cả bộ lọc và ô tìm kiếm hiển thị kết quả ngay lập tức, không cần nhấn thêm nút.
  - Nếu không có kết quả: màn hình trắng hiển thị text "Không tìm thấy kết quả".
- Xử lý hiển thị Action theo kỳ báo cáo:
  - Các button [Lập báo cáo] và [Nhập từ file] bị ẩn hoàn toàn đối với kỳ báo cáo chưa bắt đầu. Tham chiếu: CF_01.

---


## UC323-328.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Lập mới báo cáo tình hình điều chỉnh quyết định chủ trương đầu tư/GCNĐKĐT về vốn và quy mô tại các KCN, KKT trong kỳ báo cáo
- Chức năng cho phép Ban Quản lý chọn danh sách các dự án có điều chỉnh và điền các thông số điều chỉnh. Bảng dữ liệu được phân làm 2 mục: Điều chỉnh dự án ĐTNN và Điều chỉnh dự án ĐTTN. Hệ thống tự động phân loại dự án vào đúng mục khi chọn. Tham chiếu: CF_01.

**Precondition:** Dữ liệu Master Data về danh sách dự án phải có sẵn trên hệ thống. Tài khoản có quyền lập báo cáo.

**Postcondition:** Khi Lưu nháp, báo cáo có trạng thái "Lưu nháp". Khi nộp, bản ghi được lưu vào DB với trạng thái "Chờ duyệt", đồng thời trigger quy trình workflow tiếp theo.

Phân quyền: Ban Quản lý các khu công nghiệp, kinh tế. Tham chiếu: CMR_04.

Truy cập chức năng: Màn danh sách báo cáo (UC323-328.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 323, 324

---

### 2. Mô tả giao diện

**Giao diện lập báo cáo**

Giao diện: Màn hình nhập liệu dạng bảng Grid với 2 Section phân nhóm.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **MỤC 1 – ĐIỀU CHỈNH DỰ ÁN ĐẦU TƯ NƯỚC NGOÀI (ĐTNN)** | | | | | | Hệ thống tự động phân loại bản ghi vào mục này nếu dự án thuộc loại ĐTNN theo API. |
| **MỤC 2 – ĐIỀU CHỈNH DỰ ÁN ĐẦU TƯ TRONG NƯỚC (ĐTTN)** | | | | | | Hệ thống tự động phân loại bản ghi vào mục này nếu dự án thuộc loại ĐTTN theo API. |
| **CỘT THÔNG TIN (áp dụng cho tất cả bản ghi trong cả 2 mục)** | | | | | | |
| 1 | STT | Label | Tự tăng | | | Số thứ tự tự động tăng theo từng dòng trong mỗi mục, bắt đầu từ 1. |
| 2 | Tên dự án đầu tư | Dropdown | Null | x | x | Khi người dùng click vào Tên dự án đâu tư thì sẽ hiển thị ra các dự án đã được trả qua API và filter sẵn theo từng mục (mục 1 là các dự án của mục 1, mục 2 là các dự án của mục 2). Sau khi chọn dự án, các cột 3- 6 sẽ được autofill theo dự án đã chọn (Nếu thay đổi dự án, các cột 3-6 cũng sẽ thay đổi giá trị theo dự án mới). Khi người dùng chọn dự án đã được chọn trước ở dòng trước đó trong báo cáo thì không cho chọn và hiển thị thông báo lỗi như sau: Dự án này đã được chọn trước ở dòng trước đó trong báo cáo. Vui lòng kiểm tra lại. Tham chiếu: CMR_07. |
| 3 | KCN/KKT | Textbox | Null | | x | Tự động điền theo dự án đã chọn ở cột 2. Trạng thái: Disabled. Tham chiếu: CMR_12, CMR_06. |
| 4 | Văn bản thành lập hoặc tương đương | Textbox | Null | | x | Tự động điền theo dự án đã chọn ở cột 2. Trạng thái: Disabled. Tham chiếu: CMR_12, CMR_06. |
| 5 | Ngày cấp | Textbox | Null | | x | Tự động điền theo dự án đã chọn ở cột 2. Định dạng: dd/MM/yyyy. Trạng thái: Disabled. Tham chiếu: CMR_12, CMR_06. |
| 6 | Nhà đầu tư | Textbox | Null | | x | Tự động điền theo dự án đã chọn ở cột 2. Với dự án có nhiều nhà đầu tư, hệ thống liệt kê tên các NĐT ngăn cách bằng dấu phẩy. Trạng thái: Disabled. Tham chiếu: CMR_12, CMR_06. |
| **Khung Vốn điều lệ (tr. USD)** | | | | | | |
| 7 | Tăng | Number | Null | x | | Chấp nhận số >= 0 hoặc rỗng. Bắt buộc ít nhất 1 cột trong nhóm Tăng/Giảm của một dòng phải có giá trị > 0. Tham chiếu: CMR_05. |
| 8 | Giảm | Number | Null | x | | Chấp nhận số >= 0 hoặc rỗng. Bắt buộc ít nhất 1 cột trong nhóm Tăng/Giảm của một dòng phải có giá trị > 0. Tham chiếu: CMR_05. |
| **Khung Vốn đầu tư (tr. USD)** | | | | | | |
| 9 | Tăng | Number | Null | x | | Chấp nhận số >= 0 hoặc rỗng. Bắt buộc ít nhất 1 cột trong nhóm Tăng/Giảm của một dòng phải có giá trị > 0. Tham chiếu: CMR_05. |
| 10 | Giảm | Number | Null | x | | Chấp nhận số >= 0 hoặc rỗng. Bắt buộc ít nhất 1 cột trong nhóm Tăng/Giảm của một dòng phải có giá trị > 0. Tham chiếu: CMR_05. |
| **Khung Quy mô diện tích đất điều chỉnh (ha)** | | | | | | |
| 11 | Tăng | Number | Null | x | | Chấp nhận số >= 0 hoặc rỗng. Bắt buộc ít nhất 1 cột trong nhóm Tăng/Giảm của một dòng phải có giá trị > 0. Tham chiếu: CMR_05. |
| 12 | Giảm | Number | Null | x | | Chấp nhận số >= 0 hoặc rỗng. Bắt buộc ít nhất 1 cột trong nhóm Tăng/Giảm của một dòng phải có giá trị > 0. Tham chiếu: CMR_05. |
| 13 | Thêm dòng dự án đầu tư nước ngoài | Button | Null | | | Luôn enable, khi click vào hệ thống sẽ thêm 1 dòng mới vào trước dòng tính tổng của mục 1 Điều chỉnh dự án đầu tư nước ngoài. |
| 14 | Thêm dòng dự án đầu tư trong nước | Button | Null | | | Luôn enable, khi click vào hệ thống sẽ thêm 1 dòng mới vào trước dòng tính tổng của mục 2 Điều chỉnh dự án đầu tư nước. |
| 15 | Xóa | Button | Null | | | Chỉ hiển thị và enable khi mỗi mục (mục 1 và mục 2) có ít nhất 2 dòng. Nếu mỗi mục chỉ có 1 dòng thì button "Xóa" sẽ ẩn đi. Khi click vào nút Xóa thì dòng chứa nó sẽ bị xóa và các dòng dưới dòng xóa sẽ được đẩy lên. Dòng Tổng của từng mục sẽ tự động được tính lại. |
| **HÀNG TỔNG (cuối mỗi mục)** | | | | | | |
| T1 | Tổng – Mục 1 (ĐTNN) | Number | Tính tự động | | | Auto-sum các cột 7–12 của tất cả bản ghi trong Mục 1. Cập nhật ngay khi người dùng thay đổi giá trị. Không cho phép chỉnh sửa. Tham chiếu CMR_05 |
| T2 | Tổng – Mục 2 (ĐTTN) | Number | Tính tự động | | | Auto-sum các cột 7–12 của tất cả bản ghi trong Mục 2. Cập nhật ngay khi người dùng thay đổi giá trị. Không cho phép chỉnh sửa. Tham chiếu CMR_05 |
| **CÁC BUTTON** | | | | | | |
| B1 | Hủy | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]"). |
| B2 | Xem trước | Button | | | | Mở popup PDF Preview báo cáo (không rời màn Lập). Tham chiếu: CF_07.1. |
| B3 | Lưu nháp | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]"). |
| B4 | Nộp báo cáo | Button | | | | Tham chiếu: CF_01. |

---

### 3. Mô tả các xử lý của chức năng

Xử lý chung: Tham chiếu: CF_01 (Lập báo cáo), CMR_18, CF_04 (Xuất báo cáo), CF_05 (In).

Xử lý đặc thù biểu mẫu 2115.H:

- Khởi tạo màn hình: Bảng mở ra với 1 dòng trống mặc định ở mỗi mục Điều chỉnh Dự án đầu tư nước ngoài và Điều chỉnh dự án đầu tư trong nước. Các cột 3–6 ở trạng thái Disabled cho đến khi Dự án ở cột 2 được chọn. Tham chiếu: CF_01.
- Chọn Dự án (Cột 2): Ngay khi chọn, hệ thống gọi API Quản lý dự án nội bộ và điền tự động các cột 3, 4, 5, 6. Đồng thời hệ thống đọc thuộc tính loại dự án từ API để phân loại bản ghi vào Mục 1 (ĐTNN) hoặc Mục 2 (ĐTTN). Tham chiếu: CMR_12.
- Hàng Tổng: Tự động cập nhật (Auto-calc) ngay khi người dùng thay đổi bất kỳ giá trị nào ở cột 7–12. Trạng thái: Disabled. Không cho phép chỉnh sửa trực tiếp.
- Lỗi API: Thêm thông báo và kịch bản xử lý khi API gọi danh sách dự án bị timeout/error. Tham chiếu: CMR_12.

---


## UC323-328.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ – Xem chi tiết, Xem vòng đời, In, Xuất báo cáo, Nộp, Chỉnh sửa
- Chức năng cho phép người dùng thực hiện các tác vụ bổ trợ tương ứng trạng thái bản ghi. Quyền truy cập được kiểm soát theo CMR_03.

Phân quyền: Ban Quản lý các KCN, KKT. Tham chiếu: CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC323-328.1) → Cột Hành động → Chọn tác vụ tương ứng

Chức năng đáp ứng usecase số: 325, 326, 327, 328

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
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Tất cả người dùng | Khi click vào sẽ mở màn hình Xem chi tiết báo cáo (toàn trang, toàn bộ Disabled). Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Tất cả người dùng | Khi click vào sẽ mở màn hình popup Vòng đời của báo cáo. Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | | Khi click vào sẽ mở màn hình In. Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Tất cả người dùng | Khi click vào sẽ mở màn hình chọn ổ lưu file (định dạng Docx). Tham chiếu: CF_04. |
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
| AC1 | Kiểm tra logic validate cross-field Tăng/Giảm | Người dùng đang nhập liệu cho 1 dự án trên Grid | Để trống tất cả các cột Tăng/Giảm (cột 7-12) hoặc nhập toàn bộ = 0 | Hiển thị lỗi bắt buộc điền ít nhất 1 giá trị > 0 trong nhóm cột Tăng/Giảm |
| AC2 | Kiểm tra logic phân loại ĐTNN / ĐTTN | Người dùng mở form Lập báo cáo | Chọn Dự án từ Dropdown | Hệ thống phân loại dự án vào đúng Mục 1 (ĐTNN) hoặc Mục 2 (ĐTTN) dựa trên thuộc tính API. Danh sách dự án hiển thị ở từng mục được filter tương ứng. |
| AC3 | Kiểm tra cảnh báo trùng lặp dự án | Người dùng thêm mới 1 dòng trên Grid | Chọn Dự án A (đã được chọn ở dòng trước đó) | Hệ thống chặn và hiển thị alert "Dự án đã được chọn ở dòng trên" |

---

## 5. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-07 | 1.0 → 1.1 | Cập nhật theo Audit | (Nhiều mục) | (Đã cập nhật theo Implementation Plan) | Thêm nút Xóa dòng, sửa logic Tăng/giảm, thêm AC, đổi tên nút, thêm Pre/Post conditions |
| 2026-05-08 | 1.1 → 1.2 | Nút Lập báo cáo / Nhập từ file | Hiển thị luôn enable | Chỉ hiển thị/enable khi Trong thời hạn | Cập nhật theo feedback |
| 2026-05-08 | 1.1 → 1.2 | Tên dự án đầu tư (Dropdown) | Lấy danh sách chung | Filter theo từng mục, validate chọn trùng | Cập nhật theo feedback |
| 2026-05-08 | 1.1 → 1.2 | Nút Thêm dòng, Xóa | Nằm rải rác / Thiếu | Bổ sung rõ ràng thành các trường trên Grid | Cập nhật theo feedback |
| 2026-05-08 | 1.1 → 1.2 | Lỗi API (Exception Flow)| (Không có) | Xử lý lỗi API khi gọi danh sách dự án | Tham chiếu CMR_12 |
| 2026-05-11 | 1.2 → 1.3 | Quy tắc sinh mã báo cáo | `EZ_2115H_[ID]` | `EZ_2115HQLKKT_[ID]` | Chuẩn hóa suffix HQLKKT đầy đủ theo appendices.md v2.0 |
| 2026-05-11 | +1 | Tên cột | `Ngày cập nhật / Nộp` | `Ngày cập nhật` | Đồng bộ tên cột theo CS_02 (INS-03) |
| 2026-05-11 | +1 | Điều kiện hiển thị nút | `Luôn hiển thị` | `Tất cả trạng thái` | Chuẩn hóa điều kiện (INS-07) |
| 2026-05-11 | 1.2 → 1.3 | Precondition & Postcondition | Có đk 2115.H/2116.H; Hậu đk Đã tiếp nhận/Chờ duyệt | Xóa đk 2115.H/2116.H; Hậu đk chỉ còn Chờ duyệt | Cập nhật Hậu điều kiện và Tiền điều kiện lập báo cáo |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (1 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them , CMR_18 vao tham chieu CF_01 tren man hinh lap bao cao | Tuan thu CMR_18 Tab Navigation (STD-07) |
| 2026-05-17 | CMR v2.0 | STD-01 Them CMR_16 vao filter dropdown rows (1 dong) | Chua co CMR_16 | Them tham chieu CMR_16 | Filter phai co Tat ca default |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-18 | 1.3 → 1.4 | Bảng thuộc tính | (Không có) | Bổ sung Loại quy trình: Quy trình > 2 bước, CMCĐT_BCTK_04 | Phân loại luồng quy trình theo yêu cầu |
| 2026-05-20 | 1.4 → 1.5 | Điều kiện Lọc & Tìm kiếm | 1. Kỳ báo cáo (Dropdown) | 1. Năm (YearPicker) | Cập nhật theo yêu cầu |
| 2026-05-21 | 1.5 → 1.6 | Cấu trúc cột bảng Lập báo cáo | (Cột 7-12 có tên cột đầy đủ) | Thêm các Khung nhóm và rút gọn tên cột 7-12 thành Tăng/Giảm | Theo yêu cầu của người dùng |
| 2026-05-23 | 1.6 → 1.7 | Dòng 2 – Ghi chú | (Không có tham chiếu CMR_07) | Thêm "Tham chiếu: CMR_07." vào cuối ghi chú | Bổ sung tham chiếu |
| 2026-05-23 | 1.6 → 1.7 | Dòng 3-6 – Giá trị mặc định | Từ API | Null | Cập nhật theo yêu cầu |
| 2026-05-23 | 1.6 → 1.7 | Dòng 3-6 – Ghi chú | (Không có "Không hiển thị placeholder", không có CMR_06) | Thêm "Không hiển thị placeholder" đầu ghi chú + thêm CMR_06 cuối ghi chú | Bổ sung tham chiếu CMR_06 |
| 2026-05-23 | 1.6 → 1.7 | Dòng 7-12 – Ghi chú | Tham chiếu: CMR_08 | Tham chiếu: CMR_05 | Đổi tham chiếu CMR |
| 2026-05-23 | 1.6 → 1.7 | Dòng 11-12 – Ghi chú | (Không có tham chiếu CMR_05 bổ sung) | Bổ sung "Tham chiếu CMR_05" vào cuối | Theo yêu cầu |
| 2026-05-23 | 1.7 → 1.8 | Dòng 11-12 – Ghi chú | Tham chiếu: CMR_05. Tham chiếu CMR_05 (trùng lặp) | Tham chiếu: CMR_05. (giữ 1 lần) | Fix duplicate theo phản hồi BA |
| 2026-05-23 | 1.7 → 1.8 | Hàng T1, T2 – Kiểu trường | Label | Number | Đổi kiểu trường phù hợp dữ liệu số |
| 2026-05-23 | 1.7 → 1.8 | Hàng T1, T2 – Ghi chú | (Không có tham chiếu CMR_05) | Bổ sung "Tham chiếu CMR_05" vào cuối | Đồng bộ tham chiếu với dòng 7-12 |
