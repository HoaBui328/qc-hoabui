# UC197-202: Báo cáo về việc cho tổ chức kinh tế ở nước ngoài vay vốn

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | anh.luu |
| **Phân hệ** | Quản lý đầu tư ra nước ngoài |
| **Mẫu biểu** | I.19 |
| **Loại báo cáo** | Không định kỳ (Ad-hoc) |
| **Hình thức nộp** | Báo cáo đơn lẻ |
| **Phạm vi dữ liệu đầu vào** | Không có phạm vi |
| **Cơ quan nhận** | Bộ Tài chính / Ngân hàng Nhà nước |
| **Đối tượng lập** | Nhà đầu tư (Cá nhân / Tổ chức) |
| **Giao diện** | User site (Phía người dùng) |
| **Ngày tạo** | 2026-04-27 |
| **Phiên bản** | 1.4 |
| **Quy tắc sinh mã báo cáo** | ODI_I19_[ID] |
| **Loại quy trình** | Quy trình 2 bước, CMCĐT_BCTK_03 |

> **Lưu ý kiến trúc:** Báo cáo **không định kỳ** — danh sách phẳng, không nhóm theo kỳ hạn. Nút [Tạo mới] đặt trực tiếp trên header màn hình Danh sách. Mỗi NĐT tự lập báo cáo độc lập (bản ghi thuộc về NĐT đăng nhập), không áp dụng CMR_01/CMR_02. Áp dụng CMR_03 chuẩn. Không có trường chọn dự án, không có cột/filter Tên dự án.

---

## UC197-202.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo về việc cho tổ chức kinh tế ở nước ngoài vay vốn
- Chức năng cho phép Nhà đầu tư xem danh sách các báo cáo đã lập, lọc theo Trạng thái báo cáo / Năm / Tìm kiếm Mã báo cáo. Danh sách hiển thị phẳng, không nhóm theo kỳ hạn. Tham chiếu: CS_02.

Phân quyền: Nhà đầu tư (Cá nhân / Tổ chức). Mỗi NĐT chỉ xem bản ghi do mình tạo.

Truy cập chức năng: Phân hệ Báo cáo → Quản lý đầu tư ra nước ngoài → Báo cáo về việc cho tổ chức kinh tế ở nước ngoài vay vốn (Mẫu I.19)

Chức năng đáp ứng usecase số: 197, 198, 199, 200, 201, 202

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện: **Non-periodic** — Danh sách phẳng, scroll dọc khi > 10 bản ghi. Không nhóm theo kỳ hạn. Tham chiếu: CS_02.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | | |
| 1 | Trạng thái báo cáo | Multiple-selection Dropdown | Null | x | | Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07., CMR_16 |
| 2 | Năm | Yearpicker | Năm hiện tại | x | | Lọc theo năm của Ngày cập nhật bản ghi gần nhất. Kết quả hiển thị ngay sau khi chọn. Tham chiếu: CMR_07, CS_02. |
| 3 | Mã báo cáo | Search bar | Null | x | | Nhập liệu tự do tìm theo mã báo cáo. Kết quả hiển thị ngay khi nhập (Live Search). Nếu không tìm thấy: hiển thị empty state "Không tìm thấy dữ liệu phù hợp" kèm hình minh họa. Tham chiếu: CMR_06, CMR_09, CS_01, CS_02. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| **Khung Danh sách Báo cáo** | | | | | | |
| 4 | Mã báo cáo | Label | Null | | | Mã báo cáo do hệ thống sinh theo quy tắc ODI_I19_[ID]. Tham chiếu: CMR_09. |
| 5 | Ngày cập nhật | Label | Null | | | Ngày giờ của thao tác gần nhất (Tạo / Sửa / Lưu nháp / Nộp). Định dạng: dd/MM/yyyy HH:mm. |
| 6 | Trạng thái | Label | Null | | | Trạng thái cấp bản ghi: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Tham chiếu: CMR_03. |
| 7 | Hành động | Button group | Null | | | Các nút thao tác theo trạng thái bản ghi. Chi tiết: UC197-202.3. |
| **Header màn hình** | | | | | | |
| 8 | Lập báo cáo | Button | Null | | | Hiển thị trực tiếp trên header. Báo cáo không định kỳ — Tất cả trạng thái, không phụ thuộc kỳ hạn. Tham chiếu: CF_01, CS_02. |
| 9 | Nhập từ file | Button | Null | | | Hiển thị trực tiếp trên header. Báo cáo không định kỳ — Tất cả trạng thái, không phụ thuộc kỳ hạn. Tham chiếu: CF_02. |

---

### 3. Mô tả các xử lý của chức năng

- Danh sách hiển thị phẳng (flat list), không nhóm theo kỳ hạn. Tham chiếu: CS_02.
- Sắp xếp mặc định theo Ngày cập nhật giảm dần (mới nhất lên trên).
- Scroll dọc khi danh sách > 10 bản ghi. Tham chiếu: CS_02.
- Tất cả bộ lọc và ô tìm kiếm hiển thị kết quả ngay lập tức, không cần nhấn thêm nút xác nhận. Tham chiếu: CMR_07.
- Nút [Tạo mới] Tất cả trạng thái trên header — không phụ thuộc vào kỳ hạn (báo cáo không định kỳ). **Không tham chiếu CMR_04.**
- Mỗi NĐT chỉ thấy bản ghi do mình tạo. Không có cơ chế chia sẻ bản ghi giữa các NĐT.
- Không giới hạn số lượng báo cáo I.19 mỗi NĐT có thể tạo (báo cáo không định kỳ — ad-hoc).
- Không có trường chọn Dự án, không có cột/filter Tên dự án trên màn hình danh sách (khác UC185-190, UC191-196).

---

## UC197-202.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Tạo mới báo cáo về việc cho tổ chức kinh tế ở nước ngoài vay vốn
- Chức năng cho phép Nhà đầu tư nhập liệu và lập báo cáo theo biểu mẫu I.19. Thông tin NĐT được tự động điền từ profile hệ thống (Tên, Email, SĐT) và từ API ICR (thông tin giấy tờ pháp lý). Tham chiếu: CF_01.

Phân quyền: Nhà đầu tư (Cá nhân / Tổ chức) đã đăng nhập.

**Điều kiện tiên quyết (Preconditions):**
- NĐT đã đăng nhập thành công vào hệ thống.
- Hệ thống API ICR khả dụng (nếu không khả dụng → fallback theo CMR_12: hiển thị Toast T05, các field ICR chuyển sang Enabled cho nhập tay).
- Profile NĐT đã có thông tin cơ bản (Tên, Email, SĐT).

**Kết quả (Postconditions):**
- Lưu nháp: Bản ghi được lưu vào DB với trạng thái "Lưu nháp", hiển thị Toast T01, quay về Danh sách.
- Nộp báo cáo: Bản ghi chuyển trạng thái sang "Chờ duyệt", hiển thị Toast T02, quay về Danh sách.
- Hủy: Không lưu dữ liệu, quay về Danh sách.

Truy cập chức năng: Màn danh sách báo cáo (UC197-202.1) → Nhấn nút [Tạo mới]

Chức năng đáp ứng usecase số: 197, 198

---

### 2. Mô tả giao diện

**Giao diện tạo mới**

Giao diện: Màn hình tạo mới theo biểu mẫu I.19.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **THÔNG TIN NHÀ ĐẦU TƯ** | | | | | | Auto-fill từ profile và API ICR. |
| 1 | Tên nhà đầu tư | Textbox | Từ profile | x | x | Auto-fill từ profile hệ thống. Cho phép chỉnh sửa. Max 255 ký tự (block ký tự khi đạt giới hạn). Nếu để trống: lỗi "Vui lòng nhập Tên nhà đầu tư". Tham chiếu: CMR_06. Placeholder: "Nhập Tên nhà đầu tư". |
| 2 | Giấy CNĐKDN / CCCD số | Textbox | Từ API ICR | x | x | Auto-fill từ API ICR. Cho phép chỉnh sửa. Max 20 ký tự (block ký tự khi đạt giới hạn). Validate: không rỗng. Trạng thái ban đầu theo CMR_12. Tham chiếu: CMR_06, CMR_12. Placeholder: "Nhập Giấy CNĐKDN / CCCD số". |
| 3 | Ngày cấp CCCD / CNĐKDN | Datepicker | Từ API ICR | x | x | Auto-fill từ API ICR. Cho phép chỉnh sửa. Định dạng hiển thị: dd/MM/yyyy. Validate: ≤ ngày hôm nay, ≥ 01/01/1900. Lỗi inline: "Ngày cấp không hợp lệ". Trạng thái ban đầu theo CMR_12. Tham chiếu: CMR_12. |
| 4 | Địa chỉ | Textarea | Từ API ICR | x | x | Auto-fill từ API ICR. Cho phép chỉnh sửa. Validate: không rỗng. Trạng thái ban đầu theo CMR_12. Tham chiếu: CMR_06, CMR_12. Placeholder: "Nhập Địa chỉ". |
| 5 | Mã số thuế | Textbox | Từ API ICR | x | x | Auto-fill từ API ICR. Cho phép chỉnh sửa. Validate: đúng định dạng 10 hoặc 13 chữ số. Lỗi inline: "Mã số thuế phải là 10 hoặc 13 chữ số". Trạng thái ban đầu theo CMR_12. Tham chiếu: CMR_06, CMR_12. Placeholder: "Nhập Mã số thuế". |
| 6 | Đại diện theo pháp luật | Textbox | Từ API ICR | x | x* | Auto-fill từ API ICR. Cho phép chỉnh sửa. Bắt buộc nếu Đối tượng = Tổ chức (DN). Optional nếu = Cá nhân. Trạng thái ban đầu theo CMR_12. Tham chiếu: CMR_06, CMR_12. Placeholder: "Nhập Đại diện theo pháp luật". |
| 7 | Chức vụ | Textbox | Từ API ICR | x | x* | Auto-fill từ API ICR. Cho phép chỉnh sửa. Bắt buộc nếu trường Đại diện theo pháp luật (mục 6) đã có giá trị. Optional nếu mục 6 để trống. Trạng thái ban đầu theo CMR_12. Tham chiếu: CMR_06, CMR_12. Placeholder: "Nhập Chức vụ". |
| 8 | Email | Textbox | Từ profile | x | x | Auto-fill từ profile hệ thống. Cho phép chỉnh sửa. Validate: đúng định dạng email (có @ và domain hợp lệ). Tham chiếu: CMR_06. Placeholder: "Nhập Email". |
| 9 | Điện thoại | Textbox | Từ profile | x | x | Auto-fill từ profile hệ thống. Cho phép chỉnh sửa. Validate: số điện thoại hợp lệ (10–11 chữ số, không ký tự đặc biệt ngoài dấu +). Tham chiếu: CMR_06. Placeholder: "Nhập Điện thoại". |
| **THÔNG TIN KHOẢN CHO VAY** | | | | | | Toàn bộ nhập tay thủ công. |
| 10 | Tên TCKT tại nước ngoài vay vốn | Textbox | Null | x | x | Nhập tay. Max 300 ký tự. Hiển thị lỗi "Vui lòng nhập Tên TCKT tại nước ngoài vay vốn" nếu để trống. Tham chiếu: CMR_06. Placeholder: "Nhập Tên TCKT tại nước ngoài vay vốn". |
| 11 | Tổng số tiền cho vay (USD) | Number | Null | x | x | Nhập tay. Validate: > 0; 5 chữ số thập phân; max 15 chữ số phần nguyên. Block ký tự `-` khi nhập. Lỗi inline: "Vui lòng nhập Tổng số tiền cho vay (USD)" nếu để trống; "Giá trị phải lớn hơn 0" nếu ≤ 0. Tham chiếu: CMR_05, CMR_06. |
| 12 | Mục đích | Textarea | Null | x | x | Nhập tay. Max 3000 ký tự. Placeholder: "Nhập Mục đích (Nêu rõ mục đích sử dụng vốn vay)". Hiển thị lỗi "Vui lòng nhập Mục đích" nếu để trống. Tham chiếu: CMR_06. |
| 13 | Điều kiện cho vay | Textarea | Null | x | x | Nhập tay. Max 3000 ký tự. Placeholder: "Nhập Điều kiện cho vay (Lãi suất, thời hạn, điều kiện giải ngân...)". Hiển thị lỗi "Vui lòng nhập Điều kiện cho vay" nếu để trống. Tham chiếu: CMR_06. |
| 14 | Kế hoạch giải ngân | Textarea | Null | x | x | Nhập tay. Max 3000 ký tự. Placeholder: "Nhập Kế hoạch giải ngân (Tiến độ giải ngân theo từng đợt, mốc thời gian)". Hiển thị lỗi "Vui lòng nhập Kế hoạch giải ngân" nếu để trống. Tham chiếu: CMR_06. |
| 15 | Kế hoạch thu hồi nợ | Textarea | Null | x | x | Nhập tay. Max 3000 ký tự. Placeholder: "Nhập Kế hoạch thu hồi nợ (Lịch hoàn trả gốc và lãi)". Hiển thị lỗi "Vui lòng nhập Kế hoạch thu hồi nợ" nếu để trống. Tham chiếu: CMR_06. |
| 16 | Phương án cân đối nguồn ngoại tệ + đánh giá khả năng tài chính bên cho vay | Textarea | Null | x | x | Nhập tay. Max 3000 ký tự. Đánh giá năng lực tài chính của NĐT (bên cho vay) và phương án cân đối nguồn ngoại tệ để thực hiện khoản cho vay. Hiển thị lỗi "Vui lòng nhập Phương án cân đối nguồn ngoại tệ + đánh giá khả năng tài chính bên cho vay" nếu để trống. Tham chiếu: CMR_06. Placeholder: "Nhập Phương án cân đối nguồn ngoại tệ + đánh giá khả năng tài chính bên cho vay". |
| 17 | Đánh giá khả năng tài chính của bên vay | Textarea | Null | x | x | Nhập tay. Max 3000 ký tự. Đánh giá năng lực tài chính của TCKT nước ngoài (bên vay). Hiển thị lỗi "Vui lòng nhập Đánh giá khả năng tài chính của bên vay" nếu để trống. Tham chiếu: CMR_06. Placeholder: "Nhập Đánh giá khả năng tài chính của bên vay". |
| 18 | Mức độ rủi ro và biện pháp phòng ngừa | Textarea | Null | x | x | Nhập tay. Max 3000 ký tự. Hiển thị lỗi "Vui lòng nhập Mức độ rủi ro và biện pháp phòng ngừa" nếu để trống. Tham chiếu: CMR_06. Placeholder: "Nhập Mức độ rủi ro và biện pháp phòng ngừa". |
| 19 | Biện pháp bảo đảm tài sản và xử lý TS bảo đảm | Textarea | Null | x | | Optional. Max 3000 ký tự. Placeholder: "Nhập Biện pháp bảo đảm tài sản và xử lý TS bảo đảm (Điền nếu có tài sản bảo đảm)". Tham chiếu: CMR_06. |
| 20 | Các nội dung liên quan khác | Textarea | Null | x | | Optional. Max 3000 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập Các nội dung liên quan khác". |
| **CÁC NÚT HÀNH ĐỘNG** | | | | | | |
| 21 | Lưu nháp | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]"). |
| 22 | Xem trước | Button | | | | Mở popup PDF Preview từ bên trong màn hình Tạo mới. Tham chiếu: CF_07.1. |
| 23 | Nộp báo cáo | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |
| 24 | Hủy | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]"). |


**CÁC BUTTON**

| #  | Tên           | Kiểu   | Điều kiện hiển thị | Phân quyền       | Mô tả                                                                                |
| -- | -------------- | ------- | ----------------------- | -------------------- | ------------------------------------------------------------------------------------- |
| B1 | Hủy           | Button | Luôn                   | Người tạo         | Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]").                                     |
| B2 | Xem trước | Button | Luôn                   | Người tạo         | Mở popup PDF Preview báo cáo (không rời màn Lập). Tham chiếu: CF_07.1.        |
| B3 | Lưu nháp     | Button | Luôn                   | Người tạo         | Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]").                                |
| B4 | Nộp báo cáo | Button | Lưu nháp, Yêu cầu CS | Người tạo         | Validate toàn bộ trường bắt buộc trước khi nộp. Tham chiếu: CF_01.         |
---



### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu: CF_01 (Lập báo cáo), CMR_18, CF_04 (Xuất báo cáo), CF_05 (In), CF_07.1 (nút [Xem trước] — PDF Preview Popup từ bên trong màn hình).

**Xử lý đặc thù biểu mẫu I.19:**

- **Khởi tạo màn hình:** Form mở ra, các trường Thông tin NĐT được điền tự động ngay khi màn hình load (không cần chọn dự án):
  - Tên NĐT, Email, SĐT (mục 1, 8, 9): điền từ profile hệ thống → **Enabled**, cho phép chỉnh sửa.
  - CCCD/CNĐKDN số, Ngày cấp, Địa chỉ, MST, Đại diện PL, Chức vụ (mục 2–7): gọi **API ICR** → trạng thái theo CMR_12 (Disabled nếu API trả dữ liệu; Enabled nếu API trả null/rỗng).
  - Toàn bộ trường Thông tin khoản cho vay (mục 10–20): trống, Enabled cho nhập tay.

- **Conditional Required — Đại diện theo pháp luật (mục 6):**
  - Nếu Đối tượng đăng nhập = **Tổ chức (DN)** (nhận biết từ profile): trường Required, hiển thị dấu * đỏ. Nếu để trống khi Nộp → lỗi inline "Vui lòng nhập [tên trường]".
  - Nếu Đối tượng = **Cá nhân**: trường Optional, không hiển thị dấu *.

- **Conditional Required — Chức vụ (mục 7):**
  - Required khi trường Đại diện theo pháp luật (mục 6) **có giá trị**. Hệ thống tự động chuyển trạng thái Required khi mục 6 được nhập.
  - Optional khi mục 6 để trống.

- **Validate Tổng số tiền cho vay (mục 11):** > 0; 5 chữ số thập phân. Tham chiếu: CMR_05.

- **Validate Mã số thuế (mục 5):** Đúng định dạng 10 chữ số (cá nhân/hộ kinh doanh) hoặc 13 chữ số (chi nhánh/đơn vị trực thuộc). Lỗi inline nếu sai định dạng.

- **Validate Email (mục 8):** Bắt buộc có ký tự @ và domain hợp lệ (VD: example@domain.com). Lỗi inline nếu sai định dạng.

- **Validate Điện thoại (mục 9):** 10–11 chữ số, cho phép dấu + ở đầu (prefix quốc tế). Lỗi inline: "Số điện thoại không hợp lệ" nếu sai định dạng.

- **Hành vi vượt max length:** Tất cả trường Textbox/Textarea áp dụng hard limit — block ký tự ngay khi đạt giới hạn max length, không cho phép nhập thêm.

- **Hành vi field ICR trong màn hình Chỉnh sửa (CF_03):** Khi mở màn hình Chỉnh sửa, các field ICR giữ nguyên trạng thái Disabled/Enabled như lúc tạo ban đầu. NĐT KHÔNG thể unlock field đang Disabled để override. Nếu cần thay đổi thông tin pháp lý → NĐT phải cập nhật qua hệ thống ICR trước.

- **Nộp từ Danh sách (CF_09):** Khi NĐT nhấn nút [Nộp] từ cột Hành động trên Danh sách, nếu validate FAIL → hệ thống redirect sang màn hình Chỉnh sửa và hiển thị lỗi inline tại các trường không hợp lệ. Tham chiếu: CF_09.

- **Xuất báo cáo:** Kết xuất file **.docx**. Tham chiếu: CF_04.

---

## UC197-202.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ — Xem chi tiết, Chỉnh sửa, Nộp, Xem vòng đời, In, Xuất báo cáo, Xóa
- Chức năng cho phép người dùng thực hiện các tác vụ bổ trợ trên bản ghi của mình theo trạng thái. Mỗi NĐT chỉ thao tác trên bản ghi do mình tạo.

Phân quyền: NĐT đăng nhập (chỉ bản ghi của mình). Áp dụng CMR_03 chuẩn. Không áp dụng CMR_01/CMR_02.

Truy cập chức năng: Màn danh sách báo cáo (UC197-202.1) → Cột Hành động → Chọn tác vụ

Chức năng đáp ứng usecase số: 199, 200, 201, 202

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
| 1 | Nộp | Button | Lưu nháp & Yêu cầu chỉnh sửa | NĐT sở hữu bản ghi | Tham chiếu: CF_09. Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |
| 2 | Chỉnh sửa | Button | Lưu nháp & Yêu cầu chỉnh sửa | NĐT sở hữu bản ghi | Tham chiếu: CF_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | NĐT sở hữu bản ghi | Điều hướng đến màn hình Xem toàn trang (full-page). Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | NĐT sở hữu bản ghi | Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | NĐT sở hữu bản ghi | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | NĐT sở hữu bản ghi | Kết xuất file .docx. Tham chiếu: CF_04. |
| 7 | Xóa | Button | Chỉ Lưu nháp **VÀ** chưa từng được nộp | NĐT sở hữu bản ghi | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết (màn hình View full-page): Tham chiếu: CF_07.
  - Nút [Xem trước] trong màn hình View → Mở popup PDF Preview. Tham chiếu: CF_07.1.
  - Nút [Chỉnh sửa] → Điều hướng sang CF_03. **Ẩn hoàn toàn** nếu không đủ điều kiện trạng thái.
  - Nút [Hủy] → Quay về Danh sách (không cần xác nhận).
- Chỉnh sửa báo cáo: Tham chiếu: CF_03.
- Nộp báo cáo: Tham chiếu: CF_01.
- Xem vòng đời: Tham chiếu: CF_06.
- In báo cáo: Tham chiếu: CF_05.
- Xuất báo cáo: Kết xuất file **.docx**. Tham chiếu: CF_04.
- Xóa báo cáo: Tham chiếu: CF_08.

---

---

## 4. Tiêu chí nghiệm thu (Acceptance Criteria)

**AC1: Xem danh sách báo cáo — Phân quyền**
- **Given** NĐT đăng nhập thành công.
- **When** Truy cập danh sách báo cáo Mẫu I.19.
- **Then** Chỉ hiển thị các báo cáo do NĐT đó tự lập. Danh sách hiển thị phẳng, sắp xếp theo Ngày cập nhật giảm dần. Nút "Tạo mới" luôn hiển thị trên header. Không có cột/filter Tên dự án.

**AC2: Lập báo cáo — Autofill dữ liệu**
- **Given** NĐT nhấn nút [Tạo mới].
- **When** Màn hình tạo mới mở ra.
- **Then** Tên, Email, SĐT tự động điền từ Profile (Enabled, cho phép sửa). Giấy tờ pháp lý gọi API ICR: nếu ICR trả dữ liệu → field Disabled; nếu ICR trả null/rỗng → field Enabled; nếu ICR timeout → Toast T05 + field Enabled.

**AC3: Lập báo cáo — Conditional Required**
- **Given** NĐT đang ở form Tạo mới.
- **When** Đối tượng đăng nhập = Tổ chức (DN).
- **Then** Trường "Đại diện theo pháp luật" hiển thị dấu * bắt buộc. Nếu trường này có giá trị → trường "Chức vụ" cũng bắt buộc.
- **When** Đối tượng đăng nhập = Cá nhân.
- **Then** Trường "Đại diện theo pháp luật" không bắt buộc, không hiển thị dấu *.

**AC4: Validate form — Các trường bắt buộc**
- **Given** NĐT nhấn [Nộp báo cáo] hoặc [Lưu nháp].
- **When** Có trường bắt buộc để trống.
- **Then** hiển thị lỗi inline "Vui lòng nhập [tên trường]" tại trường tương ứng. Không cho phép nộp/lưu.

**AC5: Validate form — Định dạng đặc biệt**
- **Given** NĐT nhập dữ liệu vào form.
- **When** MST sai định dạng → lỗi "Mã số thuế phải là 10 hoặc 13 chữ số".
- **When** Email sai định dạng → lỗi "Email không hợp lệ".
- **When** SĐT sai định dạng → lỗi "Số điện thoại không hợp lệ".
- **When** Tổng số tiền cho vay ≤ 0 → lỗi "Giá trị phải lớn hơn 0".
- **When** Ngày cấp > ngày hôm nay hoặc < 01/01/1900 → lỗi "Ngày cấp không hợp lệ".

**AC6: Lưu nháp thành công**
- **Given** NĐT đã nhập ít nhất 1 trường dữ liệu.
- **When** Nhấn nút [Lưu nháp].
- **Then** Bản ghi lưu vào DB, trạng thái = "Lưu nháp", hiển thị Toast T01, quay về Danh sách.

**AC7: Nộp báo cáo thành công**
- **Given** NĐT đã điền đầy đủ các trường bắt buộc và hợp lệ.
- **When** Nhấn nút [Nộp báo cáo].
- **Then** Hiển thị popup xác nhận P01. Sau khi đồng ý → bản ghi chuyển trạng thái "Chờ duyệt", hiển thị Toast T02, quay về Danh sách.

**AC8: Xóa bản ghi**
- **Given** Bản ghi ở trạng thái "Lưu nháp" VÀ chưa từng được nộp.
- **When** NĐT nhấn nút [Xóa].
- **Then** Hiển thị popup xác nhận. Sau khi đồng ý → bản ghi bị xóa khỏi danh sách, không thể khôi phục. Tham chiếu: CF_08.

**AC9: Nộp từ Danh sách — Validate FAIL**
- **Given** Bản ghi ở trạng thái "Lưu nháp" hoặc "Yêu cầu chỉnh sửa", có trường bắt buộc chưa điền.
- **When** NĐT nhấn nút [Nộp] từ cột Hành động trên Danh sách.
- **Then** Hệ thống redirect sang màn hình Chỉnh sửa, hiển thị lỗi inline tại các trường không hợp lệ. Tham chiếu: CF_09.

---

## 5. Yêu cầu phi chức năng (Non-functional Requirements)

| # | Hạng mục | Yêu cầu | Ghi chú |
| --- | --- | --- | --- |
| NFR-01 | Hiệu năng API ICR | Thời gian phản hồi ≤ 5 giây. Nếu quá timeout → hiển thị Toast T05, field chuyển Enabled. | Tham chiếu: CMR_12 |
| NFR-02 | Debounce Search | Ô tìm kiếm Mã báo cáo áp dụng debounce 300ms trước khi gọi API tìm kiếm. | Tham chiếu: CMR_07 |
| NFR-03 | Scroll performance | Danh sách phải scroll mượt khi có > 50 bản ghi. Lazy load nếu cần. | CS_02 |
| NFR-04 | Concurrent access | Mỗi NĐT chỉ thao tác trên bản ghi của mình — không có xung đột concurrent giữa các NĐT. | N/A |

---

## 6. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-07 | 1.0 → 1.1 | Bảng thuộc tính — Phạm vi dữ liệu đầu vào | (Không có) | Không có phạm vi | Bổ sung metadata phân loại phạm vi báo cáo |
| 2026-05-07 | 1.0 → 1.1 | Định dạng bảng Markdown | Dòng phân cách không khớp số cột | Sửa dòng phân cách khớp đúng số cột tiêu đề | Chuẩn hóa định dạng Markdown |
| 2026-05-11 | +1 | Tên cột | `Ngày cập nhật / Nộp` | `Ngày cập nhật` | Đồng bộ tên cột theo CS_02 (INS-03) |
| 2026-05-11 | +1 | Điều kiện hiển thị nút | `Luôn hiển thị` | `Tất cả trạng thái` | Chuẩn hóa điều kiện (INS-07) |
| 2026-05-12 | 1.1 → 1.2 | Field 16 — Tên trường | `đánh giá khả năng tài chính bên đi vay` | `đánh giá khả năng tài chính bên cho vay` | Sửa ngữ nghĩa: field 16 là đánh giá bên cho vay (NĐT), field 17 là bên vay (TCKT nước ngoài) |
| 2026-05-12 | 1.1 → 1.2 | Danh sách — Phân trang | `Phân trang theo bản ghi. Tham chiếu: CMR_10` | `Scroll dọc khi >10 bản ghi (theo CS_02)` | Đồng bộ với CS_02 (báo cáo không định kỳ dùng scroll, không phân trang) |
| 2026-05-12 | 1.1 → 1.2 | Placeholder Search bar | `"Nhập dữ liệu"` | `"Tìm kiếm theo Mã báo cáo"` | Đồng bộ với CS_01 |
| 2026-05-12 | 1.1 → 1.2 | Empty state text | `"Không tìm thấy kết quả"` | `"Không tìm thấy dữ liệu phù hợp"` kèm hình minh họa | Đồng bộ với CS_02 |
| 2026-05-12 | 1.1 → 1.2 | Object Attributes | Thiếu max length, format, error text | Bổ sung đầy đủ max length, format dd/MM/yyyy, error message cụ thể | Giải quyết gap audit Q5–Q8, Q12 |
| 2026-05-12 | 1.1 → 1.2 | Preconditions & Postconditions | (Không có) | Bổ sung đầy đủ | Giải quyết gap audit Section 4 |
| 2026-05-12 | 1.1 → 1.2 | Acceptance Criteria | (Không có) | Bổ sung 9 AC (Given/When/Then) | Giải quyết gap audit Section 9 |
| 2026-05-12 | 1.1 → 1.2 | Non-functional Requirements | (Không có) | Bổ sung NFR-01 đến NFR-04 | Giải quyết gap audit Section 10 |
| 2026-05-12 | 1.1 → 1.2 | Functional Logic | Thiếu mô tả CF_09, ICR Edit mode, giới hạn số báo cáo | Bổ sung đầy đủ | Giải quyết gap audit Q9–Q11 |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (1 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them , CMR_18 vao tham chieu CF_01 tren man hinh lap bao cao | Tuan thu CMR_18 Tab Navigation (STD-07) |
| 2026-05-17 | CMR v2.0 | STD-02 Required messages (10 truong) | Truong bat buoc | Vui long nhap/chon [ten truong] | Dong bo CMR_05/06/07 v2.0 |
| 2026-05-17 | CMR v2.0 | STD-02 Required message trong AC/logic | Truong bat buoc | Vui long nhap/chon [ten truong] | Dong bo CMR v2.0 |
| 2026-05-17 | CMR v2.0 | STD-02 Required message (cleanup) | Truong bat buoc | Vui long nhap [ten truong] | Dong bo CMR v2.0 |
| 2026-05-17 | CMR v2.0 | STD-04b Search placeholder fix (1) | Tim kiem theo... | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 STD-04b |
| 2026-05-17 | CMR v2.0 | STD-04a Placeholder text/numeric (13 truong) | Nhap du lieu | Nhap [ten truong cu the] | CMR_06 STD-04a |
| 2026-05-17 | CMR v2.0 | STD-04a Custom Placeholder | 5 truong khong chuan | Dong bo Nhap [ten truong] (Goi y) | CMR_06 |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-18 | 1.2 → 1.3 | Bảng thuộc tính — Loại quy trình | (Không có) | Quy trình 2 bước, CMCĐT_BCTK_03 | Bổ sung metadata loại quy trình |
| 2026-05-22 | 1.3 → 1.4 | Field 1 Tên nhà đầu tư — Max length | Max 500 ký tự | Max 255 ký tự | Align CMR: CMR_06 (A06) — Textbox max 255 |
| 2026-05-22 | 1.3 → 1.4 | Fields 12-15, 17-18 (Textarea Required) — Max length | Max 500 ký tự | Max 3000 ký tự | Align CMR: CMR_06 (A06) — Textarea max 3000 |
| 2026-05-22 | 1.3 → 1.4 | Fields 19-20 (Textarea Optional) — Max length | Max 500 ký tự | Max 3000 ký tự | Align CMR: CMR_06 (A06) — Textarea max 3000 |
| 2026-05-22 | 1.3 → 1.4 | Field 16 Phương án cân đối — Max length | Max 1000 ký tự | Max 3000 ký tự | Align CMR: CMR_06 (A06) — Textarea max 3000 |
| 2026-05-22 | 1.3 → 1.4 | Field 11 Tổng số tiền cho vay — Decimal precision | 2 chữ số thập phân | 5 chữ số thập phân | Align CMR: CMR_05 (C05b) — BA confirmed 15+5 |
