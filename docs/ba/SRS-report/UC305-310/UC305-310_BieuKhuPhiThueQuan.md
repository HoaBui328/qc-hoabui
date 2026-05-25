# UC305-310: Tình hình hoạt động của các khu phi thuế quan, khu thương mại tự do, khu bảo thuế lũy kế đến kỳ báo cáo

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | Yen.trinh |
| **Phân hệ** | Báo cáo KKT/KCN |
| **Mẫu biểu** | 2112.H.QLKKT [MBFS] |
| Phân hệ Báo cáo | KCN, KKT |
| **Loại báo cáo** | Định kỳ (Quý / Năm) |
| **Phạm vi báo cáo** | Không có phạm vi |
| **Hình thức nộp** | Báo cáo đơn lẻ (Single report form) |
| **File xuất** | .docx |
| **Cơ quan nhận** | Cục Đầu tư nước ngoài |
| **Giao diện** | Admin site |
| **Đối tượng lập** | Ban Quản lý các khu công nghiệp, kinh tế |
| **Ngày tạo** | 2026-04-22 |
| **Phiên bản** | 1.7 |
| **Quy tắc sinh mã báo cáo** | EZ_2112HQLKKT_[ID] |
| **Loại quy trình** | Quy trình > 2 bước, CMCĐT_BCTK_04 |

---

## UC305-310.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách Biểu tình hình hoạt động các khu phi thuế quan, khu thương mại tự do, khu bảo thuế (Biểu số 2112.H.QLKKT)
- Chức năng cho phép Cán bộ chuyên môn Ban Quản lý khu truy cập màn hình chính để theo dõi danh sách báo cáo định kỳ Quý/Năm. Danh sách hiển thị theo cấu trúc kỳ hạn (collapsible), mỗi kỳ chứa các báo cáo đã gửi.

**Precondition:** Người dùng đã đăng nhập thành công và được phân quyền "Cán bộ chuyên môn Ban Quản lý các khu công nghiệp, kinh tế".

Phân quyền: Cán bộ chuyên môn Ban Quản lý các khu công nghiệp, kinh tế.

Truy cập chức năng: Phân hệ Báo cáo → Báo cáo KKT/KCN → Biểu 2112.H.QLKKT

Chức năng đáp ứng usecase số: 305, 306

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện:

**Periodic-single**: Giao diện mẫu cho loại Báo cáo đơn lẻ có kỳ hạn (Quý/Năm). Kỳ hạn mặc định collapse, khi click → expand danh sách báo cáo đã gửi.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | | |
| 1 | Năm | Yearpicker | Null | x | | Lọc danh sách theo năm. Kết quả hiển thị ngay khi chọn. Tham chiếu: CMR_05. |
| 2 | Trạng thái báo cáo | Multiple-selection Dropdown | Null | x | | Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07., CMR_16 |
| 3 | Mã báo cáo | Search bar | Null | x | | Search theo mã báo cáo. Nếu không tìm thấy: text "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| 4 | Trạng thái kỳ | Multiple-selection Dropdown | Null | x | | Lọc theo trạng thái:Chưa tới hạn/ Trong thời hạn/ Qua kỳ báo cáo. Tham chiếu: CMR_04. Tham chiếu: CMR_16. |
| **Khung Kỳ hạn báo cáo (Collapsible Section)** | | | | | | |
| 5 | Kỳ báo cáo | Label (collapsible) | Collapse | | | Tên kỳ (VD: "Quý I/2026", "Năm 2026"). Click → expand bảng BC. Tham chiếu: CMR_08. |
| 6 | Trạng thái kỳ | Label | | | | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| 7 | Lập báo cáo | Button | | | | Chỉ hiển thị và enable khi kỳ ở trạng thái Trong thời hạn. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CF_01, CMR_04. |
| 8 | Nhập từ file | Button | | | | Chỉ hiển thị và enable khi kỳ ở trạng thái Trong thời hạn. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| **Bảng danh sách báo cáo (trong mỗi kỳ)** | | | | | | |
| 9 | Mã báo cáo | Label | | | | Mã hệ thống sinh tự động. Tham chiếu: CMR_09. |
| 10 | Ngày cập nhật | Label | | | | Định dạng: dd/MM/yyyy HH:mm. Tham chiếu: CMR_05. |
| 11 | Trạng thái báo cáo | Label | | | | Tham chiếu: CMR_03. |
| 12 | Hành động | Button group | | | | Chi tiết: UC305-310.3. |

---

### 3. Mô tả các xử lý của chức năng

- Yêu cầu về hiển thị danh sách:
  - Sort: từ mới → cũ (giảm dần theo ngày cập nhật).
  - Phân trang kỳ hạn. Tham chiếu: CMR_10.

- Thao tác lọc & tìm kiếm:
  - Tất cả bộ lọc hiển thị kết quả ngay lập tức, không cần nút xác nhận.
  - Không có kết quả: text "Không tìm thấy kết quả".

---


## UC305-310.2: Lập Báo Cáo (Dạng Bảng — 2 Nhóm Hàng)

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Lập Biểu tình hình hoạt động các khu phi thuế quan, khu TMTD, khu bảo thuế (2112.H.QLKKT)
- Chức năng cho phép Cán bộ chuyên môn nhập liệu báo cáo dạng bảng. Bảng gồm 28 cột thông tin và 2 nhóm hàng (section) theo trạng thái khu:
  - Nhóm I: Khu đã cấp QĐ chủ trương/GCNĐKĐT và đang vận hành
  - Nhóm II: Khu đã cấp QĐ chủ trương/GCNĐKĐT và đang xây dựng cơ bản
- Cuối bảng có Tổng chung (auto-sum tất cả). Tham chiếu: CF_01.

**Precondition:** Dữ liệu Master Data về danh sách các khu (phi thuế quan, TMTD, bảo thuế) phải có sẵn trên hệ thống. Tài khoản có quyền lập báo cáo.

**Postcondition:** Khi Lưu nháp, báo cáo có trạng thái "Lưu nháp". Khi Nộp, bản ghi được lưu vào DB với trạng thái "Chờ duyệt", đồng thời trigger quy trình workflow tiếp theo.

Phân quyền: Cán bộ chuyên môn Ban Quản lý các khu công nghiệp, kinh tế.

Truy cập chức năng: Màn danh sách báo cáo (UC305-310.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 305, 306

---

### 2. Mô tả giao diện

**Giao diện thêm mới — Dạng bảng 2 nhóm hàng**

Giao diện: Màn hình nhập liệu dạng lưới (grid), 28 cột, chia 2 nhóm hàng (section header), dòng Tổng chung cuối bảng.

**Cấu trúc bảng (Row Layout):**

```
┌─────────────────────────────────────────────────────────────────┐
│ I. Khu phi thuế quan, khu TMTD, khu bảo thuế và các khu chức   │
│    năng ... đã cấp QĐ/GCNĐKĐT và ĐANG VẬN HÀNH                │
│ ├── [Row 1] [Row 2] ... [+ Thêm dòng]                          │
├─────────────────────────────────────────────────────────────────┤
│ II. Khu phi thuế quan, khu TMTD, khu bảo thuế và các khu chức  │
│     năng ... đã cấp QĐ/GCNĐKĐT và ĐANG XÂY DỰNG CƠ BẢN       │
│ ├── [Row 1] [Row 2] ... [+ Thêm dòng]                          │
├─────────────────────────────────────────────────────────────────┤
│ *** TỔNG SỐ *** (auto-sum nhóm I + II)                          │
└─────────────────────────────────────────────────────────────────┘
```

**Quy tắc Add/Remove Row (áp dụng cho mỗi nhóm):** Tham chiếu: CMR_15.

**Mô tả giao diện — 28 cột:**

| Col# | Tên cột | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | STT | Number | Null | x | x | Tham chiếu: CMR_05. |
| 2 | Tên khu | Dropdown | Null | x | x | Dropdown hiển thị danh sách khu phi thuế quan/TMTD/bảo thuế từ Master Data, đã pre-filter theo nhóm: Nhóm I chỉ hiển thị khu "Đang vận hành", Nhóm II chỉ hiển thị khu "Đang xây dựng". Tham chiếu: CMR_07.<br>- Khi user chọn 1 giá trị thì hệ thống thực hiện check:<br>+ Nếu khu đã được chọn ở dòng trước đó: Không cho user chọn và hiển thị lỗi "Khu đã được chọn trước đó. Vui lòng kiểm tra lại"<br>+ Nếu khu chưa được chọn thì đóng dropdown, hiển thị giá trị chọn và thực hiện auto fill dữ liệu cho các cột 3->11, 16->19, 24->28 |
| 3 | Văn bản thành lập hoặc tương đương | Textarea | Null | | x | Auto-fill theo Tên khu (Col#2). Nếu API có dữ liệu: Disabled. Nếu API rỗng: Enabled cho phép người dùng nhập tay. Tham chiếu CMR_12 và CMR_06. |
| 4 | Văn bản phê duyệt quy hoạch xây dựng | Textarea | Null | | x | Auto-fill theo Tên khu (Col#2). Nếu API có dữ liệu: Disabled. Nếu API rỗng: Enabled cho phép người dùng nhập tay. Tham chiếu CMR_12 và CMR_06. |
| **Quy mô diện tích (ha)** | | | | | | |
| 5 | Đất thành lập | Number | Null | | x | Auto-fill theo Tên khu (Col#2). Disabled. Tham chiếu: CMR_05, CMR_12. |
| 6 | Đất công nghiệp - dịch vụ | Number | Null | | x | Auto-fill theo Tên khu. Disabled. Tham chiếu: CMR_05, CMR_12. |
| 7 | Đất CN-DV đã cho thuê | Number | Null | | x | Auto-fill theo Tên khu. Disabled. Tham chiếu: CMR_05, CMR_12. |
| **Dự án ĐTNN (vốn nước ngoài)** | | | | | | |
| 8 | Tổng số dự án còn hiệu lực | Number | Null | | x | Auto-fill từ IRC (aggregate theo khu). Disabled. Tham chiếu: CMR_05, CMR_12. |
| 9 | Tổng vốn đầu tư đăng ký (tr.USD) | Number | Null | | x | Auto-fill từ IRC. Disabled. Tham chiếu: CMR_05, CMR_12. |
| 10 | Số dự án đang SXKD | Number | Null | | x | Auto-fill từ IRC. Disabled. Tham chiếu: CMR_05, CMR_12. |
| 11 | Tổng vốn đầu tư thực hiện (tr.USD) | Number | Null | | x | Auto-fill từ IRC. Disabled. Tham chiếu: CMR_05, CMR_12. |
| 12 | Doanh thu (tr.USD) | Number (Cho phép số thập phân tối đa 2 chữ số) | Null | x | x | Người dùng nhập. Validate: >= 0. Chấp nhận số nguyên và số thập phân. Tham chiếu: CMR_05. |
| 13 | Giá trị xuất khẩu (tr.USD) | Number (Cho phép số thập phân tối đa 2 chữ số) | Null | x | x | Người dùng nhập. Validate: >= 0. Chấp nhận số nguyên và số thập phân. Tham chiếu: CMR_05. |
| 14 | Giá trị nhập khẩu (tr.USD) | Number (Cho phép số thập phân tối đa 2 chữ số) | Null | x | x | Người dùng nhập. Validate: >= 0. Chấp nhận số nguyên và số thập phân. Tham chiếu: CMR_05. |
| 15 | Nộp ngân sách (tỷ VNĐ) | Number (Cho phép số thập phân tối đa 2 chữ số) | Null | x | x | Người dùng nhập. Validate: >= 0. Chấp nhận số nguyên và số thập phân. Tham chiếu: CMR_05. |
| **Dự án ĐTTN (vốn trong nước)** | | | | | | |
| 16 | Tổng số dự án còn hiệu lực | Number | Null | | x | Auto-fill từ IRC (aggregate). Disabled. Tham chiếu: CMR_05, CMR_12. |
| 17 | Tổng vốn đầu tư đăng ký (tỷ VNĐ) | Number | Null | | x | Auto-fill từ IRC. Disabled. Tham chiếu: CMR_05, CMR_12. |
| 18 | Số dự án đang SXKD | Number | Null | | x | Auto-fill từ IRC. Disabled. Tham chiếu: CMR_05, CMR_12. |
| 19 | Tổng vốn đầu tư thực hiện (tỷ VNĐ) | Number | Null | | x | Auto-fill từ IRC. Disabled. Tham chiếu: CMR_05, CMR_12. |
| 20 | Doanh thu (tỷ VNĐ) | Number (Cho phép số thập phân tối đa 2 chữ số) | Null | x | x | Người dùng nhập. Validate: >= 0. Chấp nhận số nguyên và số thập phân. Tham chiếu: CMR_05. |
| 21 | Giá trị xuất khẩu (tr.USD) | Number (Cho phép số thập phân tối đa 2 chữ số) | Null | x | x | Người dùng nhập. Validate: >= 0. Chấp nhận số nguyên và số thập phân. Tham chiếu: CMR_05. |
| 22 | Giá trị nhập khẩu (tr.USD) | Number (Cho phép số thập phân tối đa 2 chữ số) | Null | x | x | Người dùng nhập. Validate: >= 0. Chấp nhận số nguyên và số thập phân. Tham chiếu: CMR_05. |
| 23 | Nộp ngân sách (tỷ VNĐ) | Number (Cho phép số thập phân tối đa 2 chữ số) | Null | x | x | Người dùng nhập. Validate: >= 0. Chấp nhận số nguyên và số thập phân. Tham chiếu: CMR_05. |
| **Công trình xử lý nước thải tập trung** | | | | | | |
| 24 | Tình trạng: (Chưa xây dựng/Đang xây dựng/Đang hoạt động) | Single choice Dropdown | Null | | x | Auto fill theo tên khu ở cột 2. Tham chiếu: CMR_07. |
| 25 | Công suất thiết kế (m3/ngày đêm) | Number | Null | | x | Auto fill theo tên khu ở cột 2. Người dùng nhập. Tham chiếu: CMR_05. |
| 26 | Công suất hoạt động (m3/ngày đêm) | Number | Null | | x | Auto fill theo tên khu ở cột 2. Người dùng nhập. Tham chiếu: CMR_05. |
| **Lao động** | | | | | | |
| 27 | Trong nước (người) | Number | Null | | x | Auto fill theo tên khu. Tham chiếu: CMR_05. |
| 28 | Nước ngoài (người) | Number | Null | | x | Auto fill theo tên khu. Tham chiếu: CMR_05. |
| 29 | Thêm dòng cho Khu đang vận hành | button | | | | Luôn enable, khi click vào hệ thống sẽ thêm 1 dòng cuối mục 1 Khu phi thuế quan, khu thương mại tự do, khu bảo thuế và các khu chức năng theo quy hoạch chung xây dựng đã cấp Quyết định chủ trương đầu tư/GCNĐKĐT và đang vận hành |
| 30 | Thêm dòng cho Khu đang xây dựng cơ bản | button | | | | Luôn enable, khi click vào hệ thống sẽ thêm 1 dòng mới vào cuối mục 2 Khu phi thuế quan, khu thương mại tự do, khu bảo thuế và các khu chức năng theo quy hoạch chung xây dựng đã cấp Quyết định chủ trương đầu tư/GCNĐKĐT và đang xây dựng cơ bản, trước dòng Tổng |

**Dòng Tổng (Summary Rows):**

| Dòng | Cột tham gia | Ghi chú |
| --- | --- | --- |
| Tổng số | Col#5 – Col#28 | Disabled. Real-time. |

> Lưu ý: Col#1 (STT), Col#2 (Tên khu), Col#3-#4 (Văn bản — Text), Col#24 (Tình trạng — Single choice Dropdown) không tham gia dòng Tổng.

**Các Button:**

| # | Tên | Ghi chú |
| --- | --- | --- |
| 31 | Hủy | Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]"). |
| 32 | Xem trước | Popup Doc Preview. Tham chiếu: CF_07.1. |
| 33 | Lưu nháp | Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]"). |
| 34 | Nộp báo cáo | Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |

---

### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu: CF_01 (Lập báo cáo), CF_04 (Xuất báo cáo), CF_05 (In), CF_07 (nút [Xem trước]).

**Xử lý đặc thù biểu mẫu 2112.H.QLKKT:**

- Khởi tạo màn hình: Form mở ra với 2 nhóm hàng, mỗi nhóm có 1 dòng trống. Dropdown Tên khu (Col#2) Enabled. Tất cả cột auto-fill Disabled cho đến khi chọn Tên khu. Tham chiếu: CMR_12.
- Dropdown Tên khu (Col#2) — Pre-filter theo nhóm:
  - Nhóm I: Dropdown chỉ hiển thị các khu có trạng thái "Đang vận hành" trong Master Data.
  - Nhóm II: Dropdown chỉ hiển thị các khu có trạng thái "Đang xây dựng cơ bản" trong Master Data.
  - Hệ thống sẽ lấy trạng thái của khu từ Master Data tại đúng thời điểm lập/mở form báo cáo (real-time) và filter danh sách tên khu theo status Đang vận hành/ Đang xây dựng cơ bản. Khi user mở dropdown Tên khu ở section nào thì sẽ chỉ nhìn thấy các khu thuộc section đó.
  - Chọn Tên khu → hệ thống gọi API và auto-fill:
    - Col#3-4: Văn bản thành lập/Quy hoạch (từ Master Data KKT). Disabled.
    - Col#5-7: Diện tích (từ Master Data KKT). Disabled.
    - Col#8-11: Dự án ĐTNN — aggregate từ IRC. Disabled.
    - Col#16-19: Dự án ĐTTN — aggregate từ IRC. Disabled.
  - Tham chiếu: CMR_07, CMR_12.
- Dòng Tổng: 1 dòng tổng số. Auto-sum real-time cho toàn bộ các dòng (Col#5 đến Col#28 là Number, trừ Col#24 — Single choice Dropdown). Disabled.
- Add/Remove Row: Tham chiếu: CMR_15. Mỗi nhóm có nút [+ Thêm dòng] riêng.

---


## UC305-310.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ — Nộp, Chỉnh sửa, Xem chi tiết, Xem vòng đời, In, Xuất báo cáo, Xóa
- Quyền truy cập kiểm soát theo CMR_03.

**Precondition:** Đã có ít nhất 1 bản ghi báo cáo được lập trên hệ thống.

Phân quyền: Cán bộ chuyên môn Ban Quản lý khu (người tạo). Tham chiếu: CMR_03.

Truy cập: Màn danh sách báo cáo (UC305-310.1) → Cột Hành động

Chức năng đáp ứng usecase số: 307, 308, 309, 310

---

### 2. Mô tả giao diện

**Màn hình Xem chi tiết (Full-Page View Screen)**

Tham chiếu: CF_07.

- Giao diện: Form đọc (toàn bộ Disabled), layout giống Chỉnh sửa. Hiển thị bảng 2 nhóm + 1 dòng Tổng.
- Nút [Chỉnh sửa]: Hiển thị khi Lưu nháp hoặc YCCSR. Tham chiếu: CF_07, CMR_03.
- Nút [Xem trước]: Popup Doc Preview. Tham chiếu: CF_07.1.
- Nút [Hủy]: Quay về Danh sách. Không cần popup xác nhận.

**Popup Xem vòng đời:** Tham chiếu: CF_06.

**Action Mapping:**

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Lưu nháp, Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_09. Tham chiếu: CF_01, CMR_03. |
| 2 | Chỉnh sửa | Button | Lưu nháp, Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_03, CMR_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Người tạo | Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Người tạo | Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | Người tạo | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Người tạo | .docx. Tham chiếu: CF_04. |
| 7 | Xóa | Button | Lưu nháp VÀ chưa từng nộp | Người tạo | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Nộp: Tham chiếu: CF_09. Tham chiếu: CF_01. Cho phép nộp từ Lưu nháp và YCCSR (CMR_03).
- Chỉnh sửa: Tham chiếu: CF_03.
- Xem chi tiết: Tham chiếu: CF_07. Nút [Chỉnh sửa] ẩn nếu không đủ điều kiện (CMR_03).
- Xem vòng đời: Tham chiếu: CF_06.
- In: Tham chiếu: CF_05.
- Xuất báo cáo: .docx. Tham chiếu: CF_04.
- Xóa: Tham chiếu: CF_08.

---



---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-07 | 1.0 → 1.1 | Cập nhật theo Audit | (Nhiều mục) | (Đã cập nhật theo Implementation Plan) | Audit Readiness: Bổ sung Pre/Post-conditions, logic Master Data, định dạng thập phân, fallback API và fix tham chiếu CMR |
| 2026-05-08 | 1.1 → 1.2 | Quy tắc Add/Remove Row | Inline rule chi tiết | Tham chiếu: CMR_15 | Chuẩn hóa quy tắc thêm/xóa hàng |
| 2026-05-11 | +1 | Tên cột | `Ngày cập nhật / Nộp` | `Ngày cập nhật` | Đồng bộ tên cột theo CS_02 (INS-03) |
| 2026-05-11 | 1.1 → 1.2 | Cập nhật logic nút Lập báo cáo/Nhập từ file & Bổ sung 2 nút Thêm dòng | Như cũ | Đã cập nhật theo yêu cầu | Theo yêu cầu cập nhật UC305-310 |
| 2026-05-11 | 1.2 → 1.3 | Cập nhật Postcondition của UC305-310.2 | Trạng thái "Đã tiếp nhận" hoặc "Chờ duyệt" | Trạng thái "Chờ duyệt" | Xóa trạng thái Đã tiếp nhận khi nộp báo cáo |
| 2026-05-17 | 1.3 → 1.4 | Cập nhật cấu trúc bảng & logic Tên khu (UC305-310.2) | Có dòng Tổng nhóm, cột Scope; Tên khu chưa chặn trùng | Bỏ dòng Tổng nhóm, bỏ cột Scope; thêm check trùng Tên khu & auto-fill | Cập nhật theo Implementation Plan |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (1 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | STD-01 Them CMR_16 vao filter dropdown rows (1 dong) | Chua co CMR_16 | Them tham chieu CMR_16 | Filter phai co Tat ca default |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-18 | 1.4 → 1.5 | Bảng thuộc tính | (Không có) | Bổ sung Loại quy trình: Quy trình > 2 bước, CMCĐT_BCTK_04 | Phân loại luồng quy trình theo yêu cầu |
| 2026-05-21 | 1.5 → 1.6 | Cập nhật theo Wireframe | Kỳ báo cáo (Lọc), Trạng thái, các cột diện tích, Tình trạng XLNT, Công suất, Tổng chung | Năm, Trạng thái báo cáo, bỏ đơn vị (ha), Tình trạng: (Chưa xây dựng/Đang xây dựng/Đang hoạt động) kiểu Single choice Dropdown, bổ sung đơn vị m3/ngày đêm, Tổng số | Đồng bộ hóa với thiết kế Wireframe theo phản hồi chi tiết của người dùng |
| 2026-05-23 | 1.6 → 1.7 | Cập nhật UC305-310.2: Auto fill fields & Decimal rule & Kiểu trường Col#3,4 | Col#3-11,16-19,24-28: Giá trị mặc định = Từ Master Data/IRC, Được sửa = x (Col#24-28), không có placeholder. Col#12-15,20-23: "Chấp nhận số nguyên và số thập phân lấy tối đa 2 chữ số phần thập phân". Col#3,4: Kiểu trường = Text | Col#3-11,16-19,24-28: Giá trị mặc định = Null, Được sửa = trống, Ghi chú thêm "Không hiển thị placeholder". Col#12-15,20-23: "Chấp nhận số nguyên và số thập phân". Col#3,4: Kiểu trường = Textarea | Cập nhật theo yêu cầu BA |
