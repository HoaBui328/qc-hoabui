# UC245-250: Tình hình thành lập mới, điều chỉnh diện tích và thu hồi KCN trong kỳ báo cáo (Biểu 2102)

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | hoai.ho |
| **Phân hệ** | KKT/KCN |
| **Mẫu biểu** | Biểu số: 2102.H.QLKKT |
| **Loại báo cáo** | Định kỳ (Quý/Năm) |
| **Hình thức nộp** | Báo cáo đơn lẻ |
| **Cơ quan nhận** | Cục Đầu tư nước ngoài |
| **Giao diện** | Admin site |
| **Đối tượng lập** | Ban Quản lý các khu công nghiệp, kinh tế |
| **Ngày tạo** | 2026-04-27 |
| **Phiên bản** | 1.1 |
| **Phạm vi dữ liệu đầu vào** | Không có phạm vi |
| **Quy tắc sinh mã báo cáo** | EZ_2102HQLKKT_[ID] |

> **Lưu ý kiến trúc:** Báo cáo **định kỳ quý/năm** trên Admin site — danh sách nhóm theo Năm (CS_01, collapsible). Nút [Lập báo cáo] và [Nhập từ file] chỉ hiển thị khi kỳ **Trong thời hạn**, ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo (Tham chiếu: CMR_04).
> Đặc thù: Giao diện tạo báo cáo chia thành 4 Dropdown Sections (Accordions). Mỗi Section chứa một **Bảng động** để người dùng nhập liệu (thêm/xóa KCN). Quy tắc bắt buộc tổng thể: phải có **tối thiểu 1 KCN** được khai báo trên toàn bộ báo cáo khi Nộp.

---

## UC245-250.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

- Tên chức năng: Xem danh sách báo cáo tình hình thành lập mới, điều chỉnh diện tích và thu hồi KCN (Biểu 2102)
- Chức năng cho phép Cán bộ Ban Quản lý xem danh sách các báo cáo định kỳ. Danh sách được nhóm theo Năm (collapsible). Tham chiếu: CS_01.

Phân quyền: Cán bộ Ban Quản lý các khu công nghiệp, kinh tế. Mỗi tài khoản chỉ quản lý và nhìn thấy các bản ghi do mình tạo (Tham chiếu: CMR_03).

Truy cập chức năng: Phân hệ Báo cáo KKT/KCN → Tình hình thành lập, điều chỉnh, thu hồi KCN (Biểu 2102)

Chức năng đáp ứng usecase số: 245, 246, 247, 248, 249, 250

---

### 2. Mô tả giao diện

**Giao diện danh sách:** Periodic-single, nhóm theo Năm. Tham chiếu: CS_01.

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | | |
| 1 | Năm | Yearpicker | Năm hiện tại | x | | Người dùng chọn một hoặc nhiều giá trị năm. Lọc theo năm báo cáo. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_07. |
| 2 | Trạng thái kỳ hạn | Multiple-selection Dropdown | Null | x | | Người dùng chọn một hoặc nhiều giá trị: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_04, CMR_07., CMR_16 |
| 3 | Trạng thái báo cáo | Multiple-selection Dropdown | Null | x | | Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07., CMR_16 |
| 4 | Mã báo cáo | Search bar | Null | x | | Live Search theo mã. Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| **Khung Kỳ hạn (Collapsible)** | | | | | | |
| 5 | Năm báo cáo | Label (collapsible) | Mặc định collapse | | | VD: "Năm 2026". Tham chiếu: CMR_08. |
| 6 | Trạng thái kỳ hạn | Label | Null | | | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| 7 | Lập báo cáo | Button | Null | | | Chỉ hiển thị khi kỳ **Trong thời hạn**. Tham chiếu: CF_01, CMR_18, CMR_04. |
| 8 | Nhập từ file | Button | Null | | | Chỉ hiển thị khi kỳ **Trong thời hạn**. Tham chiếu: CF_02, CMR_04. |
| **Bảng Danh sách Báo cáo** | | | | | | |
| 9 | Mã báo cáo | Label | Null | | | EZ_2102HQLKKT_[ID]. Tham chiếu: CMR_09. |
| 10 | Ngày cập nhật | Label | Null | | | Định dạng: dd/MM/yyyy HH:mm. |
| 11 | Trạng thái | Label | Null | | | Tham chiếu: CMR_03. |
| 12 | Hành động | Button group | Null | | | Chi tiết: UC245-250.3. |

---

## UC245-250.2: Lập Báo Cáo

### 1. Mô tả chức năng

- Tên chức năng: Tạo mới Báo cáo tình hình thành lập mới, điều chỉnh diện tích và thu hồi KCN (Biểu 2102)
- Chức năng cho phép Cán bộ BQL nhập liệu các KCN có biến động trong kỳ. Màn hình chia thành 4 Dropdown Sections, mỗi section chứa một bảng động để khai báo.

Phân quyền: Cán bộ BQL các khu công nghiệp, kinh tế (Admin site). Kỳ hạn phải ở trạng thái **Trong thời hạn**. Tham chiếu: CMR_04.

Truy cập chức năng: Màn danh sách báo cáo (UC245-250.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 245, 246

---

### 2. Mô tả giao diện

**Giao diện nhập liệu:** Báo cáo chia làm 4 Dropdown Section (Accordion). Người dùng click để mở rộng (expand) từng phần. Mỗi phần là một **Bảng động (Add/Remove Row)**.

**Business Rules chung:**
- **BR01 (Định dạng số):** Dấu `,` phân tách hàng nghìn; dấu `.` phân tách thập phân. Dấu `/` và `-` dùng cho số hiệu văn bản. (Tham chiếu: CMR_05, CMR_06).
- **BR02 (Bắt buộc nhập):** Tất cả các cột trong bảng đều là Required. Khi ấn nút CTA (Lưu/Nộp), nếu user để trống → Hiển thị inline error màu đỏ bên dưới trường: *"Vui lòng nhập [tên trường]"*. Tự động biến mất khi người dùng nhập giá trị hợp lệ. Tham chiếu: CMR_06. Tổng thể toàn báo cáo phải có **tối thiểu 1 KCN** (nghĩa là ít nhất 1 trong 4 bảng phải có ≥ 1 dòng dữ liệu hợp lệ).

| Nhóm trường (Dùng chung) | Kiểu trường | Mô tả & Validation |
| --- | --- | --- |
| 1. Tên KCN | Single choice Dropdown | Danh sách KCN có trong hệ thống. Cho phép search & chọn. |
| 2. Vị trí khu | Dropdown | Các options: KCN nằm ngoài KKT / KCN nằm trong KKT ven biển / KCN nằm trong KKT cửa khẩu. Cho phép search & chọn. |
| 3. Địa điểm | Textbox | Nhập chuỗi. Max 255 ký tự. |
| 4. Nhà đầu tư xây dựng... | Textbox | Nhập chuỗi. Max 255 ký tự. |
| 5. Quốc tịch nhà đầu tư | Single choice Dropdown | Danh sách quốc tịch hợp pháp. Cho phép search & chọn. |

#### SECTION I. Các KCN mới được phê duyệt chủ trương đầu tư/thành lập
Gồm Bảng động 1. Các cột bao gồm nhóm trường dùng chung (1-5) và các trường Thành lập mới (6-11).

| Các trường đặc thù | Kiểu trường | Validation & Logic |
| --- | --- | --- |
| 6. QĐ chấp thuận CTĐT | Textbox | Nhập số hiệu QĐ. Max 255 ký tự. **Validate:** Kiểm tra với dữ liệu hệ thống, nếu không trùng khớp → hiển thị inline error *"Quyết định chấp thuận chủ trương đầu tư không tồn tại trong hệ thống"*. **Chặn lưu/nộp.** Tham chiếu: CMR_06. |
| 7. GCN đăng ký đầu tư | Textbox | Nhập số hiệu GCN. Max 255 ký tự. **Validate:** Kiểm tra với hệ thống, nếu không trùng khớp → hiển thị inline error *"[Tên field] không tồn tại trong hệ thống"*. **Chặn lưu/nộp.** Tham chiếu: CMR_06. |
| 8. Quy mô diện tích thành lập | Number | Áp dụng BR01. Label: "ha". |
| 9. Quy mô diện tích đất CN, DV | Number | Áp dụng BR01. Label: "ha". |
| 10. Thời hạn cho thuê đất | Number | Áp dụng BR01. Label: "năm". |
| 11. Vốn đầu tư xây dựng... | (Group Header) | Group này merge ô phía trên, tách làm 2 cột nhỏ phía dưới: |
| 11.1. Vốn ĐT nước ngoài | Number | Áp dụng BR01. Label: "tr.USD". |
| 11.2. Vốn ĐT trong nước | Number | Áp dụng BR01. Label: "tỷ VNĐ". |

#### SECTION II, III, IV
- Section II: Các KCN điều chỉnh tăng diện tích
- Section III: Các KCN điều chỉnh giảm diện tích
- Section IV: Các KCN thu hồi toàn bộ diện tích...

Mỗi section là 1 Bảng động. Các cột bao gồm nhóm trường dùng chung (1-5) và các trường Điều chỉnh/Thu hồi (12-15).

| Các trường đặc thù | Kiểu trường | Validation & Logic |
| --- | --- | --- |
| 12. GCN trước khi ĐC/TH | Textbox | Nhập số hiệu. Max 255 ký tự. **Validate:** Kiểm tra hệ thống, nếu không trùng khớp → hiển thị inline error *"[Tên field] không tồn tại trong hệ thống"*. **Chặn lưu/nộp.** Tham chiếu: CMR_06. |
| 13. Quy mô trước khi ĐC/TH | Number | Áp dụng BR01. Label: "ha". |
| 14. GCN sau điều chỉnh/TH | Textbox | Nhập số hiệu. Max 255 ký tự. **Validate:** Kiểm tra hệ thống, nếu không trùng khớp → hiển thị inline error *"[Tên field] không tồn tại trong hệ thống"*. **Chặn lưu/nộp.** Tham chiếu: CMR_06. |
| 15. Quy mô sau điều chỉnh/TH | Number | Áp dụng BR01. Label: "ha". |

**Các Nút Hành Động:**
- **[Lưu nháp]**: Tham chiếu CF_01.
- **[Xem trước]**: Popup PDF Preview. Tham chiếu CF_07.1.
- **[Nộp báo cáo]**: Tham chiếu CF_01.
- **[Hủy]**: Tham chiếu CF_01.

---

### 3. Mô tả các xử lý của chức năng

**Xử lý Bảng động trong Section:**
- Tại mỗi Section, người dùng nhấn `[+ Thêm dòng]` (hoặc Thêm KCN) để thêm 1 dòng mới vào bảng tương ứng.
- Có thể thêm nhiều KCN vào cùng 1 Section. 
- Có nút `[Xóa]` ở cuối mỗi dòng.
- Các Section có thể rỗng (không có dòng nào) NẾU như trong kỳ không phát sinh KCN loại đó.
- **Validate bắt buộc toàn báo cáo:** Tổng số dòng dữ liệu trên cả 4 Section phải ≥ 1. Nếu toàn bộ 4 Section đều rỗng khi nhấn [Nộp báo cáo], hệ thống chặn lại và báo lỗi *"Vui lòng khai báo ít nhất 1 KCN trong kỳ báo cáo"*.

**Xử lý Validate GCN / Quyết định (Trường 6, 7, 12, 14):**
- Đây là các trường Textbox cho phép nhập tay.
- Khi người dùng nhập liệu, hệ thống tự động kiểm tra (validate ngầm — blur event) với cơ sở dữ liệu số hiệu Quyết định/GCN đang tồn tại.
- Nếu chuỗi nhập vào KHÔNG MATCH (không tồn tại trong hệ thống), hệ thống hiển thị inline error màu đỏ bên dưới ô nhập theo cấu trúc: `[Tên field] + " không tồn tại trong hệ thống"`. **Chặn lưu nháp và nộp báo cáo** cho đến khi lỗi được giải quyết. Tham chiếu: CMR_06.

---

## UC245-250.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

- Tên chức năng: Các tác vụ bổ trợ — Xem chi tiết, Chỉnh sửa, Nộp, Xem vòng đời, In, Xuất báo cáo, Xóa
- Phân quyền: Cán bộ BQL (Người tạo). Quản lý theo quyền tác giả, các tài khoản khác cùng BQL không thấy bản ghi này. Tham chiếu: CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC245-250.1) → Cột Hành động

Chức năng đáp ứng usecase số: 247, 248, 249, 250

---

### 2. Mô tả giao diện

**Màn hình Xem chi tiết:** Tham chiếu: CF_07. 
Hiển thị layout giống màn hình tạo mới (4 Dropdown Sections) nhưng tất cả nội dung chỉ đọc (Disabled).

**Action Mapping:**

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Lưu nháp & Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_09. Tham chiếu: CF_01, CMR_18. |
| 2 | Chỉnh sửa | Button | Lưu nháp & Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Người tạo | Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Người tạo | Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | Người tạo | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Người tạo | Kết xuất **.docx**. Đảm bảo layout các bảng được xuất thành các bảng riêng biệt theo từng section. Tham chiếu: CF_04. |
| 7 | Xóa | Button | Lưu nháp **VÀ** chưa từng nộp | Người tạo | Tham chiếu: CF_08. |


**CÁC BUTTON**

| #  | Tên           | Kiểu   | Điều kiện hiển thị | Phân quyền       | Mô tả                                                                                |
| -- | -------------- | ------- | ----------------------- | -------------------- | ------------------------------------------------------------------------------------- |
| B1 | Hủy           | Button | Luôn                   | Người tạo         | Luôn Enabled. Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Hủy]").                                     |
| B2 | Xem trước | Button | Luôn                   | Người tạo         | Luôn Enabled. Mở popup PDF Preview báo cáo (không rời màn Lập). Tham chiếu: CF_07.1.        |
| B3 | Lưu nháp     | Button | Luôn                   | Người tạo         | Luôn Enabled. Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Lưu nháp]").                                |
| B4 | Nộp báo cáo | Button | Lưu nháp, Yêu cầu CS | Người tạo         | Luôn Enabled. Validate toàn bộ trường bắt buộc trước khi nộp. Tham chiếu: CF_01, CMR_18.         |
---



### 3. Mô tả các xử lý của chức năng

- Xem chi tiết: Tham chiếu CF_07. Các Accordion có KCN sẽ tự động expand, các Accordion rỗng sẽ collapse.
- Chỉnh sửa: Tham chiếu CF_03. 
- Nộp từ Màn hình danh sách: Tham chiếu CF_09. Áp dụng validate tổng số KCN ≥ 1.
- Xem vòng đời: Tham chiếu CF_06.
- In: Tham chiếu CF_05.
- Xuất báo cáo (.docx): Tham chiếu CF_04. 
- Xóa: Tham chiếu CF_08.


---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-11 | +1 | Tên cột | `Ngày cập nhật / Nộp` | `Ngày cập nhật` | Đồng bộ tên cột theo CS_02 (INS-03) |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (2 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them CMR_18 vao tham chieu CF_01 | Tuan thu CMR_18 Tab Navigation tren form nhap lieu |
| 2026-05-17 | CMR v2.0 | STD-02 Required message trong AC/logic | Truong bat buoc | Vui long nhap/chon [ten truong] | Dong bo CMR v2.0 |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |

---

## BỔ SUNG: TOAST / ERROR / INLINE MESSAGES (Cập nhật 2026-05-22)

> Tham chiếu: CMR_05, CMR_06, CMR_07, CF_01, CF_03, CF_04, CF_07, CF_08, CF_09, list-toast-messages.md

### 1. Toast Messages

| Mã | Trường hợp | Tiêu đề | Nội dung | Loại |
| :--- | :--- | :--- | :--- | :--- |
| T01 | Lập báo cáo + Lưu nháp thành công | Thành công | Đã lập báo cáo thành công | 🟢 Success |
| T02 | Nộp báo cáo thành công | Thành công | Đã nộp báo cáo thành công | 🟢 Success |
| T03 | Chỉnh sửa + Lưu nháp thành công | Thành công | Đã chỉnh sửa báo cáo thành công | 🟢 Success |
| T04 | Xuất báo cáo thành công | Thành công | Đã xuất báo cáo thành công | 🟢 Success |
| T05 | Lỗi hệ thống (API fail, lưu/nộp/xuất fail) | Lỗi hệ thống | Không thể kết nối đến hệ thống. Vui lòng thử lại sau | 🔴 Error |
| T07 | Lưu nháp khi tất cả trường đều trống | Lưu nháp không thành công | Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp | 🔴 Error |
| T08 | Xóa báo cáo thành công | Thành công | Xóa báo cáo thành công | 🟢 Success |

### 2. Inline Validation Messages

| Trường hợp | Message | Vị trí | Tham chiếu |
| :--- | :--- | :--- | :--- |
| Trường số bắt buộc bỏ trống | "Vui lòng nhập [tên trường]" | Bên dưới trường, màu đỏ | CMR_05 |
| Trường text bắt buộc bỏ trống | "Vui lòng nhập [tên trường]" | Bên dưới trường, màu đỏ | CMR_06 |
| Dropdown bắt buộc chưa chọn | "Vui lòng chọn [tên trường]" | Bên dưới trường, màu đỏ | CMR_07 |
| Nhập ký tự không hợp lệ vào trường số | "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm, dấu phẩy và dấu trừ" | Bên dưới trường, màu đỏ | CMR_05, V02 |
| Trường số ≥ 0: nhập dấu trừ | "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy" | Bên dưới trường, màu đỏ | CMR_05, V03 |
| Sai cấu trúc số (nhiều dấu chấm, dấu phẩy sai) | "Sai định dạng số" | Bên dưới trường, màu đỏ | CMR_05, V04 |
| Vượt digit precision (>15 nguyên hoặc >5 thập phân) | "[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân" | Bên dưới trường, màu đỏ | Align_CMR C05b |
| Vượt max length Textarea (3000 ký tự) — Fields 12, 13, 14 | "[Tên trường] không được vượt quá 3000 ký tự!" | Bên dưới trường, màu đỏ | CMR_06 |
| GCN/QĐ không tồn tại trong hệ thống | "[Tên field] không tồn tại trong hệ thống" | Bên dưới trường, màu đỏ | UC-specific |
| Bảng rỗng khi Nộp (tất cả 4 section đều rỗng) | "Vui lòng khai báo ít nhất 1 KCN trong kỳ báo cáo" | Inline error hoặc Toast | V16 |

### 3. Popup Messages

| Mã | Trường hợp | Tiêu đề | Nội dung | Nút |
| :--- | :--- | :--- | :--- | :--- |
| P01 | Xác nhận nộp báo cáo | Bạn có chắc muốn nộp? | Checkbox: "Tôi đã kiểm tra toàn bộ thông tin đã nhập và xác nhận rằng các thông tin đó là chính xác" | [Xác nhận] / [Hủy] / ✕ |
| P02 | Dirty Form Guard | Dữ liệu chưa được lưu | Bạn có chắc chắn muốn rời khỏi trang này không? | [Đồng ý] / [Hủy] |
| P04 | Xác nhận xóa báo cáo | — | Bạn có chắc chắn muốn xóa báo cáo này? | [Đồng ý] / [Hủy] |

### 4. Quy tắc Numeric (Bổ sung theo Align_CMR)

- **Digit precision:** Phần nguyên tối đa **15 chữ số**, phần thập phân tối đa **5 chữ số**. Tổng max length = 21 ký tự.
- **Áp dụng cho:** Tất cả trường Number trong form (Quy mô diện tích, Vốn ĐT, Thời hạn cho thuê đất, v.v.)
- **Error khi vượt:** "[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"

### 5. Textarea max length (Bổ sung theo Align_CMR)

- Fields 12, 13, 14 (textarea): Sửa max từ 1000 → **3000 ký tự**
- Error: "[Tên trường] không được vượt quá 3000 ký tự!"

> **Lưu ý format:** Toàn bộ error/toast/inline message KHÔNG có dấu `.` ở cuối câu.
