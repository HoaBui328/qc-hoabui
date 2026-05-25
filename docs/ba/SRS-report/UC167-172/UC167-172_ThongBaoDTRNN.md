# UC167-172: Thông báo thực hiện hoạt động đầu tư ở nước ngoài (Biểu I.10)

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | anh.luu |
| **Phân hệ** | Quản lý đầu tư ra nước ngoài |
| **Mẫu biểu** | I.10 |
| **Loại báo cáo** | Định kỳ (6 tháng + năm) |
| **Hình thức nộp** | Báo cáo đơn lẻ (BC gắn: NO) |
| **Phạm vi dữ liệu đầu vào** | Có (chọn dự án) |
| **Cơ quan nhận** | Bộ Tài chính |
| **Giao diện** | User site |
| **Đối tượng lập** | Nhà đầu tư (ĐTRNN) |
| **Ngày tạo** | 2026-04-28 |
| **Phiên bản** | 1.4 |
| **Quy tắc sinh mã báo cáo** | ODI_I10_[ID] |
| **Loại quy trình** | Quy trình 2 bước, CMCĐT_BCTK_03 |

> **Lưu ý kiến trúc:**
> - **3 kỳ hạn/năm:** Kỳ 1 (H1 Jan–Jun, deadline 20/07), Kỳ 2 (H2 Jul–Dec, deadline 20/01 năm sau), Năm (deadline 15/02 năm sau). Màn hình danh sách nhóm theo 3 kỳ này trong mỗi năm.
> - **Concurrency:** 1 bản ghi duy nhất mỗi kỳ/dự án. NĐT đầu tiên tạo bản ghi → NĐT khác cùng dự án thấy bản ghi + Tooltip, [Lập báo cáo] ẩn. Sau khi bản ghi tồn tại, tất cả NĐT trong dự án có quyền ngang nhau trên bản ghi đó. Tham chiếu: CMR_02.
> - **Radio flow đầu form:** User chọn loại dự án → ảnh hưởng trường header hiển thị (GCNĐKĐTRNN vs VB ĐKGDNH).
> - **Dự án "Khác":** Khi chọn → tất cả header fields chuyển sang nhập tay thủ công.
> - **Đính kèm:** 1 khu vực upload chung, Required khi Nộp (không Required khi Lưu nháp).

---

## UC167-172.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo thông báo thực hiện hoạt động đầu tư ở nước ngoài (Biểu I.10)
- Chức năng cho phép Nhà đầu tư truy cập màn hình chính để theo dõi danh sách các thông báo theo 3 kỳ hạn/năm, nhóm theo từng Kỳ hạn báo cáo. Áp dụng luồng nghiệp vụ Case B (ĐTRNN). Tham chiếu: CMR_02.

Phân quyền: Nhà đầu tư (ĐTRNN) thuộc dự án đang hoạt động tại nước ngoài. Tham chiếu: CMR_03.

Truy cập chức năng: Phân hệ Báo cáo → Quản lý đầu tư ra nước ngoài → Thông báo thực hiện hoạt động đầu tư ở nước ngoài (Biểu I.10)

Chức năng đáp ứng usecase số: 167, 168, 169, 170, 171, 172

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện: **Periodic-single** — Báo cáo có kỳ hạn, gửi lẻ từng báo cáo. 3 kỳ/năm. Nhóm theo kỳ hạn (CS_01 collapsible).

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | | |
| 1 | Năm | Yearpicker | Năm hiện tại | x | | Lọc và nhóm danh sách theo năm chọn. Tham chiếu: CMR_07. |
| 2 | Trạng thái kỳ hạn | Multiple-selection Dropdown | Null | x | | Người dùng chọn một hoặc nhiều giá trị: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_04, CMR_07., CMR_16 |
| 3 | Trạng thái báo cáo | Multiple-selection Dropdown | Null | x | | Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07., CMR_16 |
| 4 | Dự án | Multiple-selection Dropdown | Null | x | | Danh sách dự án ĐTRNN của NĐT. Tham chiếu: CMR_07., CMR_16 |
| 5 | Mã báo cáo | Search bar | Null | x | | Live search theo mã báo cáo. Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| **Khung Danh sách kỳ hạn (Collapsible — 3 kỳ/năm)** | | | | | | |
| 6 | Kỳ hạn báo cáo | Label | Null | | | VD: "Kỳ 1/2026", "Kỳ 2/2026", "Năm 2026". Tham chiếu: CMR_08. |
| 7 | Trạng thái kỳ hạn | Label | Null | | | Chưa tới hạn / Trong thời hạn / Qua kỳ. Tham chiếu: CMR_04. |
| 8 | Lập báo cáo | Button | Null | | | Chỉ hiển thị khi **Trong thời hạn** VÀ chưa có bản ghi trong kỳ này. Tham chiếu: CF_01, CMR_18, CMR_02, CMR_04. |
| 9 | Nhập từ file | Button | Null | | | Chỉ hiển thị khi **Trong thời hạn** VÀ chưa có bản ghi. Tham chiếu: CF_02 Case 1 (có Phạm vi = Dự án), CMR_02, CMR_04. |
| **Khung Danh sách Báo cáo (trong mỗi kỳ)** | | | | | | |
| 10 | Mã báo cáo | Label | Null | | | ODI_I10_[ID]. Tham chiếu: CMR_09. |
| 11 | Tên dự án | Label | Null | | | Tên đầy đủ dự án đầu tư ra nước ngoài. |
| 12 | Ngày thông báo | Label | Null | | | Ngày user nhập tại Field 15 trong form (Hoạt động đầu tư bắt đầu từ). Định dạng: MM/yyyy. |
| 13 | Ngày cập nhật | Label | Null | | | Ngày giờ thao tác gần nhất. Định dạng: dd/MM/yyyy HH:mm. |
| 14 | Trạng thái | Label | Null | | | Trạng thái bản ghi. Tham chiếu: CMR_03. Trường hợp "Đã được lập bởi NĐT khác": hiển thị Tooltip *"Báo cáo kỳ này đã được lập bởi [Tên NĐT]. Bạn không thể tạo thêm báo cáo cho cùng dự án trong kỳ này"* Tham chiếu: CMR_02. |
| 15 | Hành động | Button group | Null | | | Chi tiết: UC167-172.3. |

---

### 3. Mô tả các xử lý của chức năng

- Hệ thống tự động nhóm danh sách theo 3 kỳ hạn/năm: Kỳ 1 (H1), Kỳ 2 (H2), Năm. Sắp xếp giảm dần (kỳ mới nhất lên đầu). Tham chiếu: CMR_10.
- Tất cả bộ lọc và search hiển thị kết quả ngay lập tức sau tương tác. Không tìm thấy → text "Không tìm thấy kết quả".
- Xử lý Concurrency (CMR_02): Khi NĐT A đã tạo bản ghi (kể cả Lưu nháp) → hệ thống **ẩn** [Lập báo cáo] và [Nhập từ file] cho NĐT B cùng dự án. Bản ghi của A hiển thị với Tooltip.

**Validation trạng thái kỳ hạn (realtime):**

Hệ thống xác định trạng thái từng kỳ dựa trên ngày hiện tại (today) so với deadline nộp báo cáo:

| Kỳ hạn | Khoảng dữ liệu | Deadline nộp | Chưa tới hạn | Trong thời hạn | Qua kỳ |
| --- | --- | --- | --- | --- | --- |
| Kỳ 1 (H1) | 01/01 – 30/06 năm N | 20/07 năm N | today < 01/07/N | 01/07/N ≤ today ≤ 20/07/N | today > 20/07/N |
| Kỳ 2 (H2) | 01/07 – 31/12 năm N | 20/01 năm N+1 | today < 01/01/(N+1) | 01/01/(N+1) ≤ today ≤ 20/01/(N+1) | today > 20/01/(N+1) |
| Năm | 01/01 – 31/12 năm N | 15/02 năm N+1 | today < 01/01/(N+1) | 01/01/(N+1) ≤ today ≤ 15/02/(N+1) | today > 15/02/(N+1) |

- Nút [Lập báo cáo] và [Nhập từ file] chỉ hiển thị khi trạng thái kỳ hạn = **Trong thời hạn** VÀ chưa có bản ghi trong kỳ đó. Tham chiếu: CMR_02, CMR_04.
- Lưu ý: Khi kỳ hạn chuyển sang "Qua kỳ", chỉ ẩn nút [Lập báo cáo] và [Nhập từ file]. Các bản ghi hiện hữu (Lưu nháp / Yêu cầu chỉnh sửa) vẫn có thể Chỉnh sửa, Nộp, Xóa bình thường theo CMR_03.
- Collapse kỳ hạn Tất cả trạng thái đủ 3 kỳ/năm bất kể có báo cáo hay không, đóng vai trò dashboard trạng thái cho NĐT.

---


## UC167-172.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Tạo mới thông báo thực hiện hoạt động đầu tư ở nước ngoài (Biểu I.10)
- Chức năng cho phép Nhà đầu tư khai báo thông tin thông báo theo biểu mẫu I.10. Form có Radio "Loại dự án" đầu trang ảnh hưởng đến trường header hiển thị. Tham chiếu: CF_01, CMR_18, CMR_17.

Phân quyền: Nhà đầu tư (ĐTRNN). Kỳ hạn phải **Trong thời hạn**. Tham chiếu: CMR_04.

Truy cập chức năng: Màn danh sách báo cáo (UC167-172.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 167, 168

---

### 2. Mô tả giao diện

**Giao diện thêm mới**

Giao diện: Màn hình tạo mới theo biểu mẫu I.10.

**BR01 (Định dạng số):** Dấu `.` phân tách hàng nghìn; dấu `,` phân tách thập phân.

**BR02 (Radio flow — Loại dự án):**
- **[Có GCNĐKĐTRNN]** → Hiển thị Fields 5, 6. Ẩn Field 7.
- **[Không thuộc diện cấp GCNĐKĐTRNN — chỉ có VB ĐKGDNH]** → Hiển thị Field 7. Ẩn Fields 5, 6.

**BR03 (Dự án "Khác"):** Khi chọn "Khác" tại Field 1 → các Fields header (4, 5, 6) chuyển sang nhập tay thủ công (không auto-fill từ IRC/API). Các fields Phần II (Field 7 trở đi) giữ nguyên kiểu trường.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| **PHẦN I — THÔNG TIN CHUNG (Header)** | | | | | | |
| 1 | Dự án | Single-choice Dropdown | Null | x | x | Danh sách dự án ĐTRNN của NĐT. Có option **"Khác"** (áp dụng BR03). Tham chiếu: CMR_07. |
| 2 | Đơn vị tiếp nhận | Dropdown | Null | x | x | Danh mục đơn vị tiếp nhận trong hệ thống (UBND, NHNN, BTC, ...). Tham chiếu: CMR_07. |
| 3 | Loại dự án | Radio | Có GCNĐKĐTRNN | x | x | **[Có GCNĐKĐTRNN]** / **[Không thuộc diện cấp GCNĐKĐTRNN — chỉ có VB ĐKGDNH]**. Quyết định trường nào hiển thị (BR02). Tham chiếu: CMR_06. |
| **— Hiển thị khi Field 3 = [Có GCNĐKĐTRNN] (BR02)** | | | | | | |
| 4 | Mã số GCNĐKĐTRNN | Textbox | Auto-fill từ IRC | x | x* | Auto-fill nếu dự án liên kết IRC; nhập tay nếu "Khác" (BR03). Max 255 ký tự. Tham chiếu: CMR_06, CMR_12. Placeholder: "Nhập Mã số GCNĐKĐTRNN". |
| 5 | Ngày cấp GCNĐKĐTRNN | Datepicker | Auto-fill từ IRC | x | x* | Auto-fill nếu IRC; nhập tay nếu "Khác". Validate: ≤ ngày hôm nay. Định dạng: dd/MM/yyyy. Tham chiếu: CMR_06, CMR_12. |
| **— Hiển thị khi Field 3 = [Không thuộc diện] (BR02)** | | | | | | |
| 6 | Số VB xác nhận ĐKGDNH | Textbox | Null | x | x* | Nhập tay. Max 255 ký tự. Required khi Field 3 = [Không thuộc diện]. Tham chiếu: CMR_06. Placeholder: "Nhập Số VB xác nhận ĐKGDNH". |
| **PHẦN II — NỘI DUNG THÔNG BÁO** | | | | | | |
| 7 | Tên quốc gia / vùng lãnh thổ tiếp nhận đầu tư | Dropdown | Null | x | x | Danh mục quốc gia chuẩn của hệ thống. Tham chiếu: CMR_07. |
| 8 | Hình thức chấp thuận đầu tư | Dropdown | Null | x | x | VB chấp thuận của nước tiếp nhận / Chứng nhận sở hữu cổ phần / VB ghi nhận thành viên-cổ đông / Hình thức khác. Tham chiếu: CMR_07. |
| 9 | Số văn bản chấp thuận | Textbox | Null | x | x | Max 255 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập Số văn bản chấp thuận". |
| 10 | Ngày cấp VB chấp thuận | Datepicker | Null | x | x | Định dạng: dd/MM/yyyy. Validate: ≤ ngày hôm nay. Tham chiếu: CMR_06. |
| 11 | Cơ quan cấp | Textbox | Null | x | x | Max 255 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập Cơ quan cấp". |
| 12 | Địa chỉ trụ sở tại nước ngoài | Textarea | Null | x | x | Placeholder: *"Ghi chi tiết: số nhà, đường, thành phố, quốc gia"*. Max 3000 ký tự. Tham chiếu: CMR_06. |
| 13 | Số tài khoản vốn ĐTRNN | Textbox | Null | x | x | Max 255 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập Số tài khoản vốn ĐTRNN". |
| 14 | Tên tổ chức tín dụng mở tài khoản | Textbox | Null | x | x | Max 255 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập Tên tổ chức tín dụng mở tài khoản". |
| 15 | Hoạt động đầu tư bắt đầu từ | MonthYearPicker | Null | x | x | Định dạng: MM/yyyy. Validate: tháng ∈ [1–12]; năm ≤ năm hiện tại + 1. Tham chiếu: CMR_06. |
| **PHẦN III — ĐÍNH KÈM** | | | | | | |
| 16 | Tài liệu đính kèm | File Upload | Null | x | x* | 1 khu vực chung cho cả 3 loại tài liệu: (a) Bản sao GCNĐKĐTRNN / VB xác nhận ĐKGDNH; (b) VB chấp thuận đầu tư / VB sở hữu cổ phần; (c) Tài liệu liên quan khác (nếu có). Định dạng: PDF, JPG, PNG. Max 10MB/file. **Required khi Nộp** (không Required khi Lưu nháp). Tham chiếu: CMR_06. |
| **Các Button** | | | | | | |
| 17 | Hủy | Button | | | | Luôn Enabled. Tham chiếu: CF_01, CMR_18, CMR_17. |
| 18 | Xem trước | Button | | | | Luôn Enabled. Popup PDF Preview. Tham chiếu: CF_07.1. |
| 19 | Lưu nháp | Button | | | | Luôn Enabled. Tham chiếu: CF_01, CMR_18, CMR_17. Sau khi lưu: NĐT khác cùng dự án thấy bản ghi + Tooltip. Tham chiếu: CMR_02. |
| 20 | Nộp báo cáo | Button | | | | Luôn Enabled. Validate: Required fields đầy đủ + ít nhất 1 file đính kèm. Tham chiếu: CF_01, CMR_18, CMR_17. |

---

### 3. Mô tả các xử lý của chức năng

**Chọn Dự án:**
- Hệ thống cung cấp dropdown danh sách dự án ĐTRNN của NĐT đang đăng nhập, kèm option **"Khác"**.
- Ngay khi chọn dự án (không phải "Khác"): Auto-fill Fields 4, 5 từ IRC nếu dự án có liên kết. Trạng thái field theo CMR_12.
- Khi chọn "Khác" (BR03): Tất cả header fields (4, 5, 6) chuyển sang Textbox nhập tay. Không auto-fill.

**Radio "Loại dự án" (BR02):**
- Mặc định: [Có GCNĐKĐTRNN]. Hiển thị Fields 4, 5. Ẩn Field 6.
- Khi chuyển sang [Không thuộc diện]: Ẩn Fields 4, 5. Hiển thị Field 6. Xóa dữ liệu đã nhập ở Fields bị ẩn.

**Upload file (Field 16):**
- Cho phép upload nhiều file một lúc.
- Validate khi Nộp: ≥ 1 file đính kèm. Nếu 0 file → lỗi *"Vui lòng đính kèm ít nhất 1 tài liệu trước khi nộp báo cáo"*.
- Lưu nháp: Không validate file (cho phép lưu mà không có file).

**Validate khi Nộp:** Tất cả Required fields đầy đủ + ít nhất 1 file đính kèm. Tham chiếu: CMR_06.

**Quy trình nộp:** Báo cáo I.10 theo quy trình **2 bước** (Nộp → Tiếp nhận). Khi NĐT nộp thành công, trạng thái chuyển sang **"Đã tiếp nhận"** (CMR_03).

**Validate kỳ hạn khi lập báo cáo:**
- Khi mở form: Hệ thống kiểm tra realtime today date so với deadline kỳ hạn tương ứng (theo bảng Validation trạng thái kỳ hạn tại UC167-172.1). Nếu kỳ hạn không còn "Trong thời hạn" (đã chuyển sang "Qua kỳ") → chặn mở form, hiển thị thông báo: *"Kỳ hạn báo cáo đã hết hạn nộp. Vui lòng liên hệ quản trị viên nếu cần hỗ trợ."*
- Khi Nộp báo cáo: Hệ thống validate lại kỳ hạn một lần nữa trước khi submit. Nếu kỳ hạn đã hết hạn trong lúc user đang nhập liệu → hiển thị thông báo: *"Kỳ hạn báo cáo đã hết hạn nộp. Báo cáo không thể nộp."* Hệ thống vẫn cho phép [Lưu nháp] trong trường hợp này.

**Concurrency:** Sau khi Lưu nháp, NĐT còn lại trong cùng dự án + kỳ thấy bản ghi kèm Tooltip. Tham chiếu: CMR_02.

---

## UC167-172.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ — Xem chi tiết, Chỉnh sửa, Nộp, Xem vòng đời, In, Xuất báo cáo, Xóa
- Chức năng cho phép Nhà đầu tư thực hiện các tác vụ tương ứng với trạng thái bản ghi. Tham chiếu: CMR_03.

Phân quyền: Kiểm soát theo trạng thái bản ghi. Tất cả NĐT trong dự án có quyền ngang nhau (Xem, Chỉnh sửa, Nộp, Xóa, In, Xuất báo cáo) khi bản ghi thỏa điều kiện trạng thái. Tham chiếu: CMR_02, CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC167-172.1) → Cột Hành động

Chức năng đáp ứng usecase số: 169, 170, 171, 172

---

### 2. Mô tả giao diện

**Màn hình Xem chi tiết (Full-Page View Screen)**

Tham chiếu: CF_07.

- Giao diện Read-only theo biểu mẫu I.10. Hiển thị đúng Radio "Loại dự án" đã chọn, trường tương ứng, và danh sách tài liệu đính kèm (tên file + link download).
- Nút **[Chỉnh sửa]**: Hiển thị khi Lưu nháp hoặc Yêu cầu chỉnh sửa. Tất cả NĐT trong dự án (CMR_02). Tham chiếu: CF_07, CMR_03.
- Nút **[Xem trước]**: Popup PDF Preview. Tham chiếu: CF_07.1.
- Nút **[Hủy]**: Quay về Danh sách. Không cần popup xác nhận.

**Popup Xem vòng đời (Audit Trail)**

Tham chiếu: CF_06.

**Các Button theo Action Mapping:**

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Lưu nháp & Yêu cầu chỉnh sửa | Tất cả NĐT trong dự án (CMR_02) | Tham chiếu: CF_09. Tham chiếu: CF_01, CMR_18, CMR_17. |
| 2 | Chỉnh sửa | Button | Lưu nháp & Yêu cầu chỉnh sửa | Tất cả NĐT trong dự án (CMR_02) | Tham chiếu: CF_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Tất cả NĐT trong dự án (CMR_02) | Tham chiếu: CF_07. Read-only theo biểu I.10. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Tất cả NĐT trong dự án (CMR_02) | Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | Tất cả NĐT trong dự án (CMR_02) | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Tất cả NĐT trong dự án (CMR_02) | Kết xuất **.docx**. Tham chiếu: CF_04. |
| 7 | Xóa | Button | Lưu nháp **VÀ** chưa từng nộp | Tất cả NĐT trong dự án (CMR_02) | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết (CF_07): Màn hình Read-only hiển thị biểu I.10 bao gồm Radio "Loại dự án", header fields tương ứng, Nội dung thông báo, và danh sách tài liệu đính kèm.
- Chỉnh sửa: Tham chiếu: CF_03.
- Nộp từ Màn hình danh sách: Tham chiếu: CF_09. Validate lại toàn bộ Required fields + ít nhất 1 file đính kèm.
- Xuất báo cáo (.docx): Tham chiếu: CF_04.
- In: Tham chiếu: CF_05.
- Xóa: Tham chiếu: CF_08.

---

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-05 | 1.0 → 1.1 | UC167-172.1 Mục 3 — Validation trạng thái kỳ hạn | (Không có) | Bổ sung bảng rule xác định trạng thái kỳ hạn (Chưa tới hạn / Trong thời hạn / Qua kỳ) dựa trên realtime today date vs deadline từng kỳ | Explicit hóa logic validate date cho nút [Lập báo cáo] |
| 2026-05-05 | 1.0 → 1.1 | UC167-172.2 Mục 3 — Validate kỳ hạn khi lập báo cáo | (Không có) | Bổ sung validate kỳ hạn khi mở form và khi Nộp; cho phép Lưu nháp nếu hết hạn giữa chừng | Xử lý edge case hết hạn trong lúc user nhập liệu |
| 2026-05-06 | 1.1 → 1.2 | Header — Lưu ý kiến trúc (Concurrency) | "Concurrency (Đa NĐT: NO): 1 dự án chỉ có 1 NĐT submit" | "Concurrency: 1 bản ghi duy nhất mỗi kỳ/dự án. Sau khi bản ghi tồn tại, tất cả NĐT ngang quyền (CMR_02)." | Đồng bộ CMR_02 và pattern UC161-166 v1.1 |
| 2026-05-06 | 1.1 → 1.2 | UC167-172.3 — Phân quyền | "Nhà đầu tư (ĐTRNN) — Người tạo" | "Tất cả NĐT trong dự án có quyền ngang nhau (CMR_02, CMR_03)" | Đồng bộ CMR_02 |
| 2026-05-06 | 1.1 → 1.2 | UC167-172.3 — Action Mapping cột Phân quyền | Tất cả 7 action: "Người tạo" | Tất cả 7 action: "Tất cả NĐT trong dự án (CMR_02)" | Đồng bộ CMR_02 |
| 2026-05-06 | 1.1 → 1.2 | UC167-172.1 Field 12 — Ngày thông báo | "Ngày user nhập tại Field 17 trong form" | "Ngày user nhập tại Field 15 trong form (Hoạt động đầu tư bắt đầu từ)" | Sửa lỗi tham chiếu sai field number |
| 2026-05-06 | 1.1 → 1.2 | UC167-172.2 — BR03 (Dự án "Khác") | "Fields header (4, 5, 6, 7) chuyển sang nhập tay" | "Fields header (4, 5, 6) chuyển sang nhập tay. Các fields Phần II giữ nguyên kiểu trường." | Field 7 (Quốc gia) thuộc Phần II, không bị ảnh hưởng bởi BR03 |
| 2026-05-06 | 1.1 → 1.2 | UC167-172.1 Field 9 — Nhập từ file | "Tham chiếu: CF_02, CMR_02, CMR_04" | "Tham chiếu: CF_02 Case 1 (có Phạm vi = Dự án), CMR_02, CMR_04" | Explicit hóa Nhập từ file Case theo pattern UC ĐTRNN |
| 2026-05-06 | 1.1 → 1.2 | UC167-172.2 Mục 3 — Quy trình nộp | (Không có) | Bổ sung: "Báo cáo I.10 theo quy trình 2 bước (Nộp → Tiếp nhận). Trạng thái → Đã tiếp nhận (CMR_03)." | Đồng bộ pattern UC161-166 (cùng phân hệ ĐTRNN, cùng nộp BTC) |
| 2026-05-06 | 1.1 → 1.2 | UC167-172.1 Mục 3 — Edge case kỳ hết hạn | (Không có) | Bổ sung: "Khi kỳ hạn Qua kỳ, bản ghi hiện hữu (Lưu nháp/YCCS) vẫn Sửa/Nộp/Xóa được theo CMR_03." | Explicit hóa logic CMR_04 chỉ chặn tạo mới, không chặn bản ghi hiện hữu |
| 2026-05-07 | 1.2 → 1.3 | Bảng thuộc tính — Phạm vi dữ liệu đầu vào | (Không có) | Có (chọn dự án) | Bổ sung metadata phân loại phạm vi báo cáo |
| 2026-05-07 | 1.2 → 1.3 | Định dạng bảng Markdown | Dòng phân cách không khớp số cột | Sửa dòng phân cách khớp đúng số cột tiêu đề | Chuẩn hóa định dạng Markdown |
| 2026-05-11 | +1 | Tên cột | `Ngày cập nhật / Nộp` | `Ngày cập nhật` | Đồng bộ tên cột theo CS_02 (INS-03) |
| 2026-05-11 | +1 | Điều kiện hiển thị nút | `Luôn hiển thị` | `Tất cả trạng thái` | Chuẩn hóa điều kiện (INS-07) |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (3 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_17 (Upload File Dinh kem) | Chua co CMR_17 | Them CMR_17 vao tham chieu CF_01 | UC co phan dinh kem tai lieu (CMR_17) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them CMR_18 vao tham chieu CF_01 | Tuan thu CMR_18 Tab Navigation tren form nhap lieu |
| 2026-05-17 | CMR v2.0 | STD-04a Placeholder text/numeric (6 truong) | Nhap du lieu | Nhap [ten truong cu the] | CMR_06 STD-04a |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-18 | 1.3 → 1.4 | Bảng thuộc tính — Loại quy trình | (Không có) | Quy trình 2 bước, CMCĐT_BCTK_03 | Bổ sung metadata loại quy trình |
| 2026-05-22 | CMR Alignment v5 | Textbox max 200→255 (Fields 11, 14); Textbox max 50→255 (Field 13); Textarea max 500→3000 (Field 12); Buttons "Luôn Enabled"; Trailing `.` removed from tooltip | Đồng bộ CMR_05/06 v2.4 |
