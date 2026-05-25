# UC173-178: Thông báo kéo dài thời hạn chuyển lợi nhuận của dự án đầu tư ra nước ngoài về Việt Nam — Mẫu I.11

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | anh.luu |
| **Phân hệ** | Quản lý đầu tư ra nước ngoài |
| **Mẫu biểu** | Mẫu I.11 |
| **Loại báo cáo** | Không định kỳ (Ad-hoc) |
| **Hình thức nộp** | Báo cáo đơn lẻ |
| **Phạm vi dữ liệu đầu vào** | Có (chọn dự án) |
| **Cơ quan nhận** | Bộ Tài chính |
| **Đối tượng lập** | Nhà đầu tư (NĐT) |
| **Giao diện** | User site |
| **Ngày tạo** | 2026-04-25 |
| **Phiên bản** | 1.3 |
| **Quy tắc sinh mã báo cáo** | ODI_I11_[ID] |
| **Loại quy trình** | Quy trình 2 bước, CMCĐT_BCTK_03 |

> **Lưu ý kiến trúc:** Báo cáo **không định kỳ** — danh sách phẳng, không nhóm theo kỳ hạn. Nút [Tạo mới] đặt trực tiếp trên header màn hình Danh sách. Phân quyền theo CMR_02 (ĐTRNN): tất cả NĐT có full quyền thao tác trên bản ghi đã tạo; mọi thao tác ghi vào Lifecycle Log.

---

## UC173-178.1: Xem Danh Sách Thông Báo

### 1. Mô tả chức năng

- Tên chức năng: Xem danh sách thông báo kéo dài thời hạn chuyển lợi nhuận ĐTRNN (Mẫu I.11)
- Chức năng cho phép Nhà đầu tư (NĐT) xem danh sách các thông báo đã lập, lọc theo Dự án / Năm / Trạng thái.

Phân quyền: Nhà đầu tư (NĐT). Tham chiếu: CMR_02.

Truy cập chức năng: Phân hệ Báo cáo → Quản lý ĐTRNN → Thông báo kéo dài thời hạn chuyển lợi nhuận (Mẫu I.11)

Chức năng đáp ứng usecase số: 173, 174, 175, 176, 177, 178

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện: **Non-periodic** — Danh sách phẳng, phân trang theo bản ghi. Không nhóm theo kỳ hạn.

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | | |
| 1 | Dự án | Multiple-selection Dropdown | Null | x | | Lọc theo tên/mã dự án. Kết quả hiển thị ngay. Tham chiếu: CMR_07., CMR_16 |
| 2 | Năm | Yearpicker | Năm hiện tại | x | | Lọc theo năm của Ngày cập nhật bản ghi gần nhất. Kết quả hiển thị ngay. Tham chiếu: CMR_07. |
| 3 | Trạng thái báo cáo | Multiple-selection Dropdown | Null | x | | Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07., CMR_16 |
| 4 | Mã báo cáo | Search bar | Null | x | | Tìm theo mã báo cáo. Hiển thị ngay khi nhập. Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| **Khung Danh sách Báo cáo** | | | | | | |
| 6 | Mã báo cáo | Label | Null | | | Tham chiếu: CMR_09. |
| 7 | Tên dự án | Label | Null | | | Tên dự án liên kết; "Khác" nếu chọn option thủ công. |
| 8 | Ngày cập nhật | Label | Null | | | Định dạng: dd/MM/yyyy HH:mm. |
| 9 | Trạng thái | Label | Null | | | Tham chiếu: CMR_03. |
| 10 | Hành động | Button group | Null | | | Chi tiết: UC173-178.3. |
| **Header màn hình** | | | | | | |
| 11 | Tạo mới | Button | Null | | | Hiển thị trực tiếp trên header. Báo cáo không định kỳ — không có kỳ hạn, không phụ thuộc CMR_04. Tham chiếu: CF_01, CMR_18, CMR_17. |
| 12 | Nhập từ file | Button | Null | | | Hiển thị trực tiếp trên header. Báo cáo không định kỳ — không có kỳ hạn, không phụ thuộc CMR_04. Tham chiếu: CF_01, CMR_18, CMR_17. |

---

### 3. Mô tả các xử lý của chức năng

- Danh sách hiển thị phẳng, sắp xếp mặc định theo Ngày cập nhật giảm dần. Tham chiếu: CMR_10.
- Tất cả bộ lọc hiển thị kết quả ngay lập tức. Tham chiếu: CMR_07.
- Nút [Tạo mới] Tất cả trạng thái trên header (báo cáo không định kỳ, không phụ thuộc kỳ hạn).

---


## UC173-178.2: Lập Báo Cáo Thông Báo

### 1. Mô tả chức năng

- Tên chức năng: Tạo mới thông báo kéo dài thời hạn chuyển lợi nhuận ĐTRNN (Mẫu I.11)
- Chức năng cho phép NĐT lập thông báo theo biểu mẫu I.11. Bao gồm bảng lợi nhuận 3 dòng cố định, 2 cột tiền tệ (Ngoại tệ đầu tư + USD). Tham chiếu: CF_01, CMR_18, CMR_17.

Phân quyền: Nhà đầu tư (NĐT). Tham chiếu: CMR_02.

Truy cập chức năng: Màn danh sách báo cáo (UC173-178.1) → Nhấn nút [Tạo mới]

Chức năng đáp ứng usecase số: 173, 174

---

### 2. Mô tả giao diện

**Giao diện tạo mới**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **PHẦN PHẠM VI BÁO CÁO** | | | | | | |
| 1 | Chọn dự án | Dropdown | Null | x | x | Danh sách dự án ĐTRNN của NĐT đăng nhập. Bao gồm option **"Khác"** (dành cho dự án chưa có GCNĐK). Khi chọn dự án: auto-fill Header (mục 2–4). Tham chiếu: CMR_12. |
| 2 | Đơn vị tiếp nhận | Dropdown | Null | x | x | Danh mục cơ quan trong hệ thống (VD: UBND, NHNN, BTC...). Enabled. Không phụ thuộc vào chọn dự án. |
| **PHẦN HEADER** | | | | | | Disable khi chọn dự án từ danh sách. Enabled khi chọn option "Khác". |
| 3 | Mã GCNĐKĐTRNN / Số VB ĐKGDNH | Text/Label | Auto-fill | | x | Disabled khi chọn dự án. Enabled và Required khi chọn "Khác". Tham chiếu: CMR_12. |
| 4 | Ngày cấp / điều chỉnh gần nhất | Date/Label | Auto-fill | | x | Disabled khi chọn dự án. Enabled và Required khi chọn "Khác". Tham chiếu: CMR_12. |
| 5 | Tên NĐT | Text/Label | Auto-fill | | x | Disabled khi chọn dự án. Enabled và Required khi chọn "Khác". Tham chiếu: CMR_12. |
| **PHẦN NỘI DUNG** | | | | | | |
| 6 | Năm tài chính | Text | Null | x | x | Format: DD/MM/YYYY – DD/MM/YYYY. Validate: ngày kết thúc > ngày bắt đầu. Placeholder: "Nhập Năm tài chính (VD: 01/01/2025 – 31/12/2025)". Tham chiếu: CMR_06. |
| 7 | Ngày có quyết định chia lợi nhuận | Date Picker | Null | x | x | Required. Validate: nằm trong khoảng ngày của trường Năm tài chính (mục 6). Tham chiếu: CMR_05. |
| **BẢNG LỢI NHUẬN — 3 dòng cố định** | | | | | | 2 cột số liệu: Ngoại tệ đầu tư + USD. |
| **Cột: Ngoại tệ đầu tư** | | | | | | Nhập tay, đơn vị theo loại ngoại tệ của dự án. |
| 8 | Dòng 1 — LN sau thuế được chia của NĐT VN (Ngoại tệ) | Number | Null | x | x | Decimal >= 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số. Tham chiếu: CMR_05. |
| 9 | Dòng 2 — LN đã chuyển về nước (Ngoại tệ) | Number | Null | x | x | Decimal >= 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số. Validate: <= Dòng 1 (Ngoại tệ). Tham chiếu: CMR_05. |
| 10 | Dòng 3 — LN còn lại (Ngoại tệ) | Calculated | Auto | | | = Dòng 1 – Dòng 2 (Ngoại tệ). Disabled, nền xám. Cập nhật real-time. |
| **Cột: USD** | | | | | | Nhập tay thủ công (không có auto-quy đổi tỷ giá). |
| 11 | Dòng 1 — LN sau thuế được chia của NĐT VN (USD) | Number | Null | x | x | Decimal >= 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số. Tham chiếu: CMR_05. |
| 12 | Dòng 2 — LN đã chuyển về nước (USD) | Number | Null | x | x | Decimal >= 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số. Validate: <= Dòng 1 (USD). Tham chiếu: CMR_05. |
| 13 | Dòng 3 — LN còn lại (USD) | Calculated | Auto | | | = Dòng 1 – Dòng 2 (USD). Disabled, nền xám. Cập nhật real-time. |
| **TRƯỜNG BỔ SUNG** | | | | | | |
| 14 | Số tiền đề nghị kéo dài (VND) | Number | Null | x | x | Decimal > 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số. Validate: <= Dòng 3 (Ngoại tệ) quy đổi VND. Tooltip: "Không vượt quá lợi nhuận còn lại chưa chuyển về". Tham chiếu: CMR_05, CMR_11. |
| 15 | Số tiền đề nghị kéo dài (USD) | Number | Null | x | x | Decimal > 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số. Validate: <= Dòng 3 (USD). Tooltip: "Không vượt quá lợi nhuận còn lại chưa chuyển về". Tham chiếu: CMR_05, CMR_11. |
| 16 | Hạn chuyển tiền mới | Date Picker | Null | x | x | Required. Validate: > Ngày nộp thông báo (ngày hiện tại). Tooltip: "Theo quy định tại khoản 3 Điều 34 Nghị định 103/2026/NĐ-CP". Tham chiếu: CMR_05, CMR_11. |
| 17 | Lý do kéo dài | Textarea | Null | x | x | Required. Max 3000 ký tự. Placeholder: "Nhập lý do kéo dài thời hạn chuyển lợi nhuận". Validation error: "Lý do kéo dài không được vượt quá 3000 ký tự". Tham chiếu: CMR_06. |
| **PHẦN ĐÍNH KÈM** | | | | | | Gộp chung: file đính kèm thông báo + báo cáo gắn kèm. |
| 18 | File đính kèm | File upload | Null | x | x | Required. Định dạng: PDF, JPG, PNG. Giới hạn: 10MB/file. Cho phép upload nhiều file. Bao gồm: (1) Tài liệu chứng minh lý do kéo dài; (2) Báo cáo tài chính / Báo cáo quyết toán thuế / VB pháp lý tương đương; (3) Quyết định về việc chia lợi nhuận của dự án tại nước ngoài. Mỗi file upload phải có icon Xóa [✕] để loại bỏ và chọn lại. |
| **CÁC NÚT HÀNH ĐỘNG** | | | | | | |
| 19 | Lưu nháp | Button | | | | Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Lưu nháp]"). |
| 20 | Nộp báo cáo | Button | | | | Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Nộp báo cáo]"). |
| 21 | Hủy | Button | | | | Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Hủy]"). |


**CÁC BUTTON**

| #  | Tên           | Kiểu   | Điều kiện hiển thị | Phân quyền       | Mô tả                                                                                |
| -- | -------------- | ------- | ----------------------- | -------------------- | ------------------------------------------------------------------------------------- |
| B1 | Hủy           | Button | Luôn                   | Người tạo         | Luôn Enabled. Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Hủy]").                                     |
| B2 | Xem trước | Button | Luôn                   | Người tạo         | Luôn Enabled. Mở popup PDF Preview báo cáo (không rời màn Lập). Tham chiếu: CF_07.1.        |
| B3 | Lưu nháp     | Button | Luôn                   | Người tạo         | Luôn Enabled. Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Lưu nháp]").                                |
| B4 | Nộp báo cáo | Button | Lưu nháp, Yêu cầu CS | Người tạo         | Luôn Enabled. Validate toàn bộ trường bắt buộc trước khi nộp. Tham chiếu: CF_01, CMR_18, CMR_17.         |
---



### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu: CF_01, CMR_18, CF_04 (Xuất báo cáo), CF_05 (In).

**Quy trình nộp:** Mẫu I.11 theo quy trình **2 bước** (Nộp → Tiếp nhận). Khi NĐT nộp thành công, trạng thái chuyển sang **"Đã tiếp nhận"** (CMR_03).

**Xử lý đặc thù Mẫu I.11:**

**A. Xử lý chọn Phạm vi báo cáo:**
- Khi chọn dự án từ Dropdown (option thông thường): Hệ thống gọi API lấy thông tin dự án → auto-fill các trường Header (mục 3–5) ở trạng thái Disabled. Tham chiếu: CMR_12.
- Khi chọn option **"Khác"**: Hệ thống chuyển các trường Header (mục 3–5) sang trạng thái **Enabled**, Required — người dùng nhập thủ công.
- Khi thay đổi lựa chọn dự án sau khi đã điền dữ liệu: Hiển thị popup xác nhận "Thay đổi dự án sẽ xóa dữ liệu Header hiện tại. Tiếp tục?" → [Xác nhận] / [Hủy].

**B. Bảng Lợi nhuận — Cross-field Validation:**
- **Dòng 2 <= Dòng 1:** Validate riêng biệt cho từng cột (Ngoại tệ và USD). Nếu vi phạm → lỗi inline màu đỏ: *"LN đã chuyển về nước không được vượt quá LN sau thuế được chia"*.
- **Dòng 3 = Dòng 1 – Dòng 2:** Calculated real-time, không validate. Disabled, nền xám.
- Không có auto-quy đổi tỷ giá: cột USD nhập tay hoàn toàn, độc lập với cột Ngoại tệ.

**C. Validate "Số tiền đề nghị kéo dài":**
- Trường VND (mục 14): > 0.
- Trường USD (mục 15): > 0 và <= Dòng 3 (USD). Nếu vi phạm → lỗi inline: *"Số tiền đề nghị kéo dài không được vượt quá lợi nhuận còn lại chưa chuyển về"*.

**D. Validate "Ngày có quyết định chia LN":**
- Phải nằm trong khoảng ngày Năm tài chính đã khai (mục 6). Nếu vi phạm → lỗi inline.

**E. Phần ĐÍNH KÈM:**
- Người dùng upload nhiều file trong cùng 1 khung. Mỗi file có nhãn gợi ý loại tài liệu (BC tài chính, QĐ chia LN...) nhưng không bắt buộc phân loại từng file.
- Ít nhất 1 file bắt buộc khi Nộp. Tham chiếu: CF_01, CMR_18 (Validate khi Nộp).

**F. Xuất báo cáo:** Kết xuất file **.docx**. Tham chiếu: CF_04.

---


## UC173-178.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

- Tên chức năng: Các tác vụ bổ trợ — Xem chi tiết, Chỉnh sửa, Nộp, Xem vòng đời, In, Xuất báo cáo
- Phân quyền: **CMR_02** — tất cả NĐT đều có quyền Chỉnh sửa, Nộp, Xem; không phân biệt người khởi tạo. Mọi thao tác ghi vào Lifecycle Log.

Truy cập chức năng: Màn danh sách báo cáo (UC173-178.1) → Cột Hành động

Chức năng đáp ứng usecase số: 175, 176, 177, 178

---

### 2. Mô tả giao diện

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Lưu nháp & Yêu cầu chỉnh sửa | Tất cả NĐT trong dự án. Tham chiếu: CF_09, CMR_02. | Tham chiếu: CF_09. Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Nộp báo cáo]"). Tham chiếu: CMR_02. |
| 2 | Chỉnh sửa | Button | Lưu nháp & Yêu cầu chỉnh sửa | Tất cả NĐT. Tham chiếu: CF_03, CMR_02. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Tất cả người dùng | Lifecycle Log ghi nhận tất cả NĐT. Tham chiếu: CF_06, CMR_02. |
| 5 | In | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Tất cả người dùng | Kết xuất file .docx. Tham chiếu: CF_04. |
| 7 | Xóa | Button | Lưu nháp **VÀ** chưa từng nộp | Người tạo | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Chỉnh sửa: Tham chiếu: CF_03. **Tất cả NĐT** đều có quyền chỉnh sửa theo CMR_02. Mọi thao tác ghi Lifecycle Log.
- Xem chi tiết: Tham chiếu: CF_07.
- Xem vòng đời: Tham chiếu: CF_06. Timeline ghi nhận đầy đủ Tên NĐT + Timestamp cho mọi thao tác.
- In báo cáo: Tham chiếu: CF_05.
- Xuất báo cáo: Kết xuất file **.docx**. Tham chiếu: CF_04.

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-07 | 1.0 → 1.1 | UC173-178.3 Mục 2 — Nút [Nộp] cột Phân quyền | Người tạo | Tất cả NĐT trong dự án. Tham chiếu: CF_09, CMR_02. | Đồng bộ CMR_02 — tất cả NĐT trong dự án ĐTRNN có quyền ngang nhau. Đồng bộ pattern UC167-172 |
| 2026-05-07 | 1.0 → 1.1 | UC173-178.2 Mục 3 — Quy trình nộp | (Không có) | Bổ sung: Mẫu I.11 theo quy trình 2 bước (Nộp → Tiếp nhận). Trạng thái → "Đã tiếp nhận" (CMR_03). | Đồng bộ pattern UC161-166, UC167-172 (cùng phân hệ ĐTRNN, cùng nộp BTC) |
| 2026-05-07 | 1.1 → 1.2 | Bảng thuộc tính — Phạm vi dữ liệu đầu vào | (Không có) | Có (chọn dự án) | Bổ sung metadata phân loại phạm vi báo cáo |
| 2026-05-07 | 1.1 → 1.2 | Định dạng bảng Markdown | Dòng phân cách không khớp số cột | Sửa dòng phân cách khớp đúng số cột tiêu đề | Chuẩn hóa định dạng Markdown |
| 2026-05-11 | +1 | Điều kiện hiển thị nút | `Luôn hiển thị` | `Tất cả trạng thái` | Chuẩn hóa điều kiện (INS-07) |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (2 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_17 (Upload File Dinh kem) | Chua co CMR_17 | Them CMR_17 vao tham chieu CF_01 | UC co phan dinh kem tai lieu (CMR_17) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them CMR_18 vao tham chieu CF_01 | Tuan thu CMR_18 Tab Navigation tren form nhap lieu |
| 2026-05-17 | CMR v2.0 | STD-04a Custom Placeholder | 2 truong khong chuan | Dong bo Nhap [ten truong] (Goi y) | CMR_06 |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-18 | 1.2 → 1.3 | Bảng thuộc tính — Loại quy trình | (Không có) | Quy trình 2 bước, CMCĐT_BCTK_03 | Bổ sung metadata loại quy trình |
| 2026-05-22 | CMR Alignment v5 | Numeric precision 15+5 (Fields 8, 9, 11, 12, 14, 15); Textarea max 3000 (Field 17); Buttons "Luôn Enabled" | Đồng bộ CMR_05/06 v2.4 |
