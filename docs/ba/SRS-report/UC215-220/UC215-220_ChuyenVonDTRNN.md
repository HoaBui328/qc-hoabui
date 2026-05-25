# UC215-220: Báo cáo về tình hình chuyển vốn đầu tư ra nước ngoài (Mẫu II.6)

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | anh.luu |
| **Phân hệ** | Quản lý đầu tư ra nước ngoài |
| **Mẫu biểu** | II.6 |
| **Loại báo cáo** | Định kỳ (Năm) |
| **Hình thức nộp** | Báo cáo đơn lẻ |
| **Phạm vi dữ liệu đầu vào** | Không có phạm vi |
| **Cơ quan nhận** | Bộ Tài chính (Cục Đầu tư nước ngoài) |
| **Giao diện** | Admin site |
| **Đối tượng lập** | Ngân hàng Nhà nước Việt Nam |
| **Ngày tạo** | 2026-04-27 |
| **Phiên bản** | 1.4 |
| **Quy tắc sinh mã báo cáo** | ODI_II6_[ID] |
| **Loại quy trình** | Quy trình 3 bước, CMCĐT_BCTK_09 |

> **Lưu ý kiến trúc:** Báo cáo **định kỳ năm** trên **Admin site** — danh sách nhóm theo Năm (CS_01, collapsible). Nút [Lập báo cáo] chỉ hiển thị khi kỳ **Trong thời hạn**, ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo (CMR_04). **Nút [Nhập từ file] không áp dụng cho Mẫu II.6** (báo cáo này do NHNN tự lập, không có nguồn dữ liệu ngoài để nhập từ file). Không có trường chọn Dự án. Phân quyền: Người tạo (CMR_03). Không áp dụng CMR_01/CMR_02. Đặc thù: có **Phần Dẫn** auto-generate (inline text Disabled) phía trên mỗi bảng, cập nhật real-time theo dữ liệu bảng.

> **Quy trình duyệt báo cáo:** Mẫu II.6 áp dụng quy trình **2 bước**: Lưu nháp → Nộp → **Đã tiếp nhận** (không qua bước Chờ duyệt). Sau khi Nộp thành công, trạng thái chuyển trực tiếp sang "Đã tiếp nhận", khóa quyền Chỉnh sửa và Xóa.

---

## UC215-220.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

- Tên chức năng: Xem danh sách báo cáo tình hình chuyển vốn ĐTRNN (Mẫu II.6)
- Chức năng cho phép Cán bộ NHNN xem danh sách các báo cáo định kỳ năm. Danh sách nhóm theo Năm (collapsible). Tham chiếu: CS_01.

Phân quyền: Cán bộ Ngân hàng Nhà nước Việt Nam (Admin site). Mỗi tài khoản chỉ thấy bản ghi do mình tạo.

Truy cập chức năng: Phân hệ Báo cáo → Quản lý ĐTRNN → Báo cáo chuyển vốn ĐTRNN (Mẫu II.6)

Chức năng đáp ứng usecase số: 215, 216, 217, 218, 219, 220

---

### 2. Mô tả giao diện

**Giao diện danh sách:** Periodic-single, nhóm theo Năm. Tham chiếu: CS_01.

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | | |
| 1 | Năm | Yearpicker | Năm hiện tại | x | | Lọc theo năm báo cáo. Tham chiếu: CMR_07. |
| 2 | Trạng thái kỳ hạn | Multiple-selection Dropdown | Null | x | | Người dùng chọn một hoặc nhiều giá trị: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_04, CMR_07., CMR_16 |
| 3 | Trạng thái báo cáo | Multiple-selection Dropdown | Null | x | | Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07., CMR_16 |
| 4 | Mã báo cáo | Search bar | Null | x | | Live Search. Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| **Khung Kỳ hạn (Collapsible)** | | | | | | |
| 5 | Năm báo cáo | Label (collapsible) | Mặc định collapse | | | Tên kỳ hiển thị theo format: "Năm [YYYY]" (VD: "Năm 2026"). Click → expand. Hệ thống tự sinh kỳ hạn theo năm dương lịch. Thời hạn mỗi kỳ: từ 01/01 đến 31/03 năm kế tiếp (VD: kỳ "Năm 2025" có hạn nộp đến 31/03/2026). Tham chiếu: CMR_08. |
| 6 | Trạng thái kỳ hạn | Label | Null | | | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| 7 | Lập báo cáo | Button | Null | | | Chỉ hiển thị khi kỳ ở trạng thái **Trong thời hạn**. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CF_01, CMR_18, CMR_04. |
| ~~8~~ | ~~Nhập từ file~~ | ~~Button~~ | — | | | **Không áp dụng cho Mẫu II.6.** Nút Nhập từ file không hiển thị trên giao diện. |
| **Bảng Danh sách Báo cáo** | | | | | | |
| 9 | Mã báo cáo | Label | Null | | | ODI_II6_[ID]. Tham chiếu: CMR_09. |
| 10 | Ngày cập nhật | Label | Null | | | Định dạng: dd/MM/yyyy HH:mm. |
| 11 | Trạng thái | Label | Null | | | Tham chiếu: CMR_03. |
| 12 | Hành động | Button group | Null | | | Chi tiết: UC215-220.3. |

---

### 3. Mô tả các xử lý của chức năng

- Danh sách nhóm theo Năm (collapse mặc định), sắp xếp năm mới nhất lên trên. Tham chiếu: CS_01, CMR_10.
- Nút [Lập báo cáo] chỉ hiển thị khi kỳ **Trong thời hạn**. Tham chiếu: CMR_04. Nút [Nhập từ file] **không áp dụng** cho Mẫu II.6.
- Tất cả bộ lọc hiển thị kết quả ngay lập tức. Tham chiếu: CMR_07.
- **Debounce:** Tìm kiếm Mã báo cáo áp dụng Debounce 300ms trước khi gọi API. Tham chiếu: CS_01.

**Empty States:**
| Trường hợp | Text hiển thị |
| --- | --- |
| Kỳ "Chưa tới hạn" chưa có báo cáo | "Chưa có báo cáo nào trong kỳ này" |
| Kỳ "Trong thời hạn" chưa có báo cáo | "Chưa có báo cáo nào. Nhấn [Lập báo cáo] để bắt đầu." |
| Kỳ "Qua kỳ báo cáo" chưa có báo cáo | "Không có báo cáo nào trong kỳ này" |
| Filter/Search không có kết quả | "Không tìm thấy kết quả phù hợp" |

---

## UC215-220.2: Lập Báo Cáo

### 1. Mô tả chức năng

- Tên chức năng: Tạo mới báo cáo tình hình chuyển vốn ĐTRNN (Mẫu II.6)
- Chức năng cho phép Cán bộ NHNN lập báo cáo theo biểu mẫu II.6. Bao gồm HEADER, 2 Phần Dẫn auto-generate và 2 bảng động. Tham chiếu: CF_01, CMR_18.

Phân quyền: Cán bộ NHNN (Admin site). Kỳ hạn phải ở trạng thái **Trong thời hạn**. Tham chiếu: CMR_04.

Truy cập chức năng: Màn danh sách báo cáo (UC215-220.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 215, 216

---

### 2. Mô tả giao diện

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **HEADER** | | | | | | |
| 1 | Đơn vị lập | Label | "Ngân hàng Nhà nước Việt Nam" | | | Hardcode. Disabled. |
| 2 | Số văn bản | Textbox | Null | x | x | Nhập tay. Max 50 ký tự. Lỗi "Vui lòng nhập Số văn bản" nếu trống. Tham chiếu: CMR_06. Placeholder: "Nhập Số văn bản". |
| 3 | Năm báo cáo | Yearpicker | Năm hiện tại | x | x | Mặc định = năm hiện tại. Cho phép chỉnh sửa. Validate: số nguyên 4 chữ số, ≥ 1990 và ≤ năm hiện tại. Lỗi inline: nếu < 1990 hoặc > năm hiện tại → "Năm báo cáo không hợp lệ". Tham chiếu: CMR_05, CMR_06. |
| **PHẦN DẪN BẢNG 1** | | | | | | Inline text Disabled phía trên Bảng 1. Cập nhật real-time theo dữ liệu Bảng 1. |
| 4 | Năm báo cáo (Phần Dẫn 1) | Label | Từ Header mục 3 | | | Auto-fill từ trường Năm báo cáo (mục 3). Disabled. Cập nhật real-time khi mục 3 thay đổi. |
| 5 | Số lượng dự án chuyển vốn ra | Label | 0 | | | Calculated = số dòng dữ liệu hiện có trong Bảng 1. Disabled. Cập nhật real-time. |
| 6 | Tổng vốn đã chuyển ra (USD) | Label | 0.00 | | | Calculated = tổng cột Vốn chuyển ra NN (USD) của Bảng 1. Disabled. Cập nhật real-time. |
| **BẢNG 1 – TÌNH HÌNH CHUYỂN VỐN TỪ VN RA NƯỚC NGOÀI** | | | | | | Bảng động. Min 1 dòng. Cho phép bảng rỗng khi Nộp. |
| **Quy tắc Add/Remove Row Bảng 1:** | | | | | | Tham chiếu: CMR_15. |
| 7 | STT | Number | Auto-increment | | | Tự động tăng. Disabled. |
| 8 | Tên NĐT | Textbox | Null | x | x | Nhập tay. Validate: không rỗng. Max 255 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập Tên NĐT". |
| 9 | Mã số DN / CCCD | Textbox | Null | x | x | Nhập tay. Validate: không rỗng. Max 50 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập Mã số DN / CCCD". |
| 10 | Mã số GCNĐT / VB ĐKGDNH | Textbox | Null | x | x | Nhập tay. Validate: không rỗng. Max 100 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập Mã số GCNĐT / VB ĐKGDNH". |
| 11 | Địa chỉ trụ sở | Textbox | Null | x | x | Nhập tay. Validate: không rỗng. Max 255 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập Địa chỉ trụ sở". |
| 12 | Mục tiêu HĐ của dự án | Textbox | Null | x | x | Nhập tay. Validate: không rỗng. Max 255 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập Mục tiêu HĐ của dự án". |
| 13 | Vốn chuyển ra NN (USD) | Number | Null | x | x | Validate: > 0 (giá trị 0.00 bị từ chối, lỗi V03); phần nguyên tối đa 15 chữ số, phần thập phân tối đa 5 chữ số; max value: 999,999,999,999.99. Hệ thống tự động format hiển thị dấu phẩy ngàn khi blur. Tham chiếu: CMR_05, CMR_06. |
| 14 | Quốc gia / vùng lãnh thổ | Dropdown (Searchable) | Null | x | x | Nguồn dữ liệu: API danh mục quốc gia chuẩn. Áp dụng CMR_12: Dropdown Disabled khi đang gọi API; nếu API fail → hiển thị Toast T05 và Dropdown chuyển sang Enabled cho phép nhập tay. Hỗ trợ tìm kiếm trong dropdown (Searchable). Tham chiếu: CMR_07, CMR_12. |
| **Dòng Tổng Bảng 1** | | | | | | |
| 15 | Tổng Vốn chuyển ra NN (USD) | Calculated | Auto | | | = Tổng cột mục 13. Disabled, nền xám. Cập nhật real-time. |
| **PHẦN DẪN BẢNG 2** | | | | | | Inline text Disabled phía trên Bảng 2. Cập nhật real-time theo dữ liệu Bảng 2. |
| 16 | Năm báo cáo (Phần Dẫn 2) | Label | Từ Header mục 3 | | | Auto-fill từ trường Năm báo cáo (mục 3). Disabled. Cập nhật real-time khi mục 3 thay đổi. |
| 17 | Số lượng dự án chuyển tiền về | Label | 0 | | | Calculated = số dòng dữ liệu hiện có trong Bảng 2. Disabled. Cập nhật real-time. |
| 18 | Tổng tiền chuyển về VN (USD) | Label | 0.00 | | | Calculated = tổng cột Tiền chuyển về VN (USD) của Bảng 2. Disabled. Cập nhật real-time. |
| **BẢNG 2 – TÌNH HÌNH CHUYỂN TIỀN TỪ NƯỚC NGOÀI VỀ VN** | | | | | | Bảng động. Min 1 dòng. Cho phép bảng rỗng khi Nộp. |
| **Quy tắc Add/Remove Row Bảng 2:** | | | | | | Tham chiếu: CMR_15. Áp dụng độc lập với Bảng 1. |
| 19 | STT | Number | Auto-increment | | | Tự động tăng. Disabled. |
| 20 | Tên NĐT | Textbox | Null | x | x | Nhập tay. Validate: không rỗng. Max 255 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập Tên NĐT". |
| 21 | Mã số DN / CCCD | Textbox | Null | x | x | Nhập tay. Validate: không rỗng. Max 50 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập Mã số DN / CCCD". |
| 22 | Mã số GCNĐT / VB ĐKGDNH | Textbox | Null | x | x | Nhập tay. Validate: không rỗng. Max 100 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập Mã số GCNĐT / VB ĐKGDNH". |
| 23 | Địa chỉ trụ sở | Textbox | Null | x | x | Nhập tay. Validate: không rỗng. Max 255 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập Địa chỉ trụ sở". |
| 24 | Mục tiêu HĐ | Textbox | Null | x | x | Nhập tay. Validate: không rỗng. Max 255 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập Mục tiêu HĐ". |
| 25 | Tiền chuyển về VN (USD) | Number | Null | x | x | Validate: > 0 (giá trị 0.00 bị từ chối, lỗi V03); phần nguyên tối đa 15 chữ số, phần thập phân tối đa 5 chữ số; max value: 999,999,999,999.99. Hệ thống tự động format hiển thị dấu phẩy ngàn khi blur. Tham chiếu: CMR_05, CMR_06. |
| 26 | Quốc gia / vùng lãnh thổ | Dropdown (Searchable) | Null | x | x | Nguồn dữ liệu: API danh mục quốc gia chuẩn. Áp dụng CMR_12: Dropdown Disabled khi đang gọi API; nếu API fail → hiển thị Toast T05 và Dropdown chuyển sang Enabled cho phép nhập tay. Hỗ trợ tìm kiếm trong dropdown (Searchable). Tham chiếu: CMR_07, CMR_12. |
| **Dòng Tổng Bảng 2** | | | | | | |
| 27 | Tổng Tiền chuyển về VN (USD) | Calculated | Auto | | | = Tổng cột mục 25. Disabled, nền xám. Cập nhật real-time. |
| **MỤC 3 – ĐỀ XUẤT KIẾN NGHỊ** | | | | | | |
| 28 | Đề xuất, kiến nghị | Textarea | Null | x | | Optional. Max 3000 ký tự. Tham chiếu: CMR_06. Placeholder: "Nhập Đề xuất, kiến nghị". |
| **CÁC NÚT HÀNH ĐỘNG** | | | | | | |
| 29 | Hủy | Button | | | | Nếu form dirty: hiển thị popup P02 (Dữ liệu chưa được lưu). Nếu form không dirty: quay lại Danh sách. Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Hủy]"). |
| 30 | Xem trước | Button | | | | Mở **Popup PDF Preview** (không chuyển trang). Đây là chức năng xem trước nội dung báo cáo dạng PDF ngay trên form Lập. Tham chiếu: CF_07.1. **Lưu ý:** Khác với nút [Xem chi tiết] trên Danh sách (CF_07 — full-page view Disabled). |
| 31 | Lưu nháp | Button | | | | Lưu bản ghi với trạng thái "Lưu nháp". Sau khi lưu thành công → hiển thị Toast T01/T03 → **quay lại màn hình Danh sách**. Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Lưu nháp]"). |
| 32 | Nộp báo cáo | Button | | | | Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Nộp báo cáo]"). |

---

### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu: CF_01, CMR_18, CF_04 (Xuất báo cáo .docx), CF_05 (In), CF_07.1 (PDF Preview).

**Xử lý đặc thù biểu mẫu II.6:**

- **Khởi tạo màn hình:**
  - Đơn vị lập (mục 1): hardcode "Ngân hàng Nhà nước Việt Nam".
  - Năm báo cáo (mục 3): mặc định = năm hiện tại, Enabled cho chỉnh sửa.
  - Phần Dẫn Bảng 1 (mục 4–6) và Phần Dẫn Bảng 2 (mục 16–18): khởi tạo với giá trị 0/0.00, Disabled.
  - Bảng 1 và Bảng 2: mỗi bảng khởi tạo 1 dòng trống.

- **Phần Dẫn — Cập nhật real-time:**
  - **Năm báo cáo (mục 4, 16):** Tự động cập nhật ngay khi người dùng thay đổi giá trị tại mục 3.
  - **Số lượng dự án (mục 5, 17):** = số dòng có **ít nhất 1 trường được nhập** (bất kỳ trường nào có giá trị khác rỗng thì dòng đó được tính). Cập nhật real-time khi thêm/xóa dòng hoặc nhập/xóa dữ liệu.
  - **Tổng vốn/tiền (mục 6, 18):** = sum của cột số tiền trong bảng tương ứng (chỉ tính các ô có giá trị hợp lệ > 0). Cập nhật real-time theo từng keystroke.
  - **Template text Phần Dẫn 1:** *"Trong năm [Năm báo cáo], có [Số lượng dự án] dự án đã chuyển vốn đầu tư ra nước ngoài với tổng số vốn đã chuyển là [Tổng vốn] USD."*
  - **Template text Phần Dẫn 2:** *"Trong năm [Năm báo cáo], có [Số lượng dự án] dự án đã chuyển tiền từ nước ngoài về Việt Nam với tổng số tiền đã chuyển là [Tổng tiền] USD."*

- **Validate Năm báo cáo (mục 3):** Số nguyên 4 chữ số, ≥ 1990 và ≤ năm hiện tại. Lỗi inline: "Năm báo cáo không hợp lệ" nếu vi phạm. Tham chiếu: CMR_05.

- **Add/Remove Row (áp dụng riêng từng bảng):** Tham chiếu: CMR_15. STT tự tăng, tự cập nhật lại sau khi xóa.

- **Validate khi Nộp:**
  - Bảng 1 và Bảng 2 **được phép rỗng** (không phát sinh nghiệp vụ). Không bắt buộc ≥ 1 dòng.
  - Nếu bảng có dữ liệu (dòng có ít nhất 1 trường được nhập): tất cả trường Required trên từng dòng đó phải có giá trị.
  - Số văn bản (mục 2) bắt buộc có giá trị khi Nộp.
  - **Validate multi-row:** Khi có lỗi trên nhiều dòng, hệ thống highlight **tất cả dòng lỗi đồng thời** (inline error trên từng trường sai), scroll tự động đến **dòng lỗi đầu tiên**. Validate Bảng 1 và Bảng 2 được thực hiện **song song** (hiển thị lỗi cả 2 bảng cùng lúc).

- **Validate khi Lưu nháp:**
  - Nếu toàn bộ form rỗng (không có bất kỳ trường nào được nhập): hiển thị Toast T07 ("Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp"). Form không lưu.
  - Nếu có ít nhất 1 trường được nhập: lưu thành công, không validate required.

- **Xuất báo cáo:** Kết xuất file **.docx**. Tham chiếu: CF_04. Tên file theo format: `[Mã báo cáo]_[Kỳ báo cáo]_[Mã đơn vị].docx`. Ví dụ: `ODI_II6_001_nam-2026_NHNN.docx`. Trong đó: Mã đơn vị = "NHNN" (Ngân hàng Nhà nước), Kỳ báo cáo = "nam-[YYYY]".

- **Hành vi redirect sau Lưu nháp:** Sau khi lưu thành công → hiển thị Toast T01 (tạo mới) hoặc T03 (chỉnh sửa) → quay lại màn hình Danh sách (UC215-220.1). Tham chiếu: CF_01, CMR_18.

---

## UC215-220.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

- Tên chức năng: Các tác vụ bổ trợ — Xem chi tiết, Chỉnh sửa, Nộp, Xem vòng đời, In, Xuất báo cáo, Xóa
- Phân quyền: Người tạo (CMR_03). Không áp dụng CMR_01/CMR_02.

Truy cập chức năng: Màn danh sách báo cáo (UC215-220.1) → Cột Hành động

Chức năng đáp ứng usecase số: 217, 218, 219, 220

---

### 2. Mô tả giao diện

**Màn hình Xem chi tiết:** Tham chiếu: CF_07. Form đọc toàn bộ Disabled. Hiển thị đầy đủ 2 Phần Dẫn + 2 bảng + dòng Tổng. **Lưu ý:** Đây là chế độ full-page view (khác với nút [Xem trước] trên form Lập — popup PDF preview).

**Action Mapping:**

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Lưu nháp & Yêu cầu chỉnh sửa | Người tạo | Sau khi nộp thành công, trạng thái chuyển sang **"Đã tiếp nhận"**. Tham chiếu: CF_09, CF_01. |
| 2 | Chỉnh sửa | Button | Lưu nháp & Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Người tạo | Full-page view (Disabled toàn bộ). Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Người tạo | Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | Người tạo | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Người tạo | Kết xuất .docx. Tên file: `[Mã BC]_nam-[YYYY]_NHNN.docx`. Tham chiếu: CF_04. |
| 7 | Xóa | Button | Lưu nháp **VÀ** chưa từng nộp | Người tạo | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết: Tham chiếu: CF_07. Phần Dẫn + 2 bảng hiển thị ở chế độ đọc (Disabled toàn bộ).
- Chỉnh sửa: Tham chiếu: CF_03. Phần Dẫn tiếp tục cập nhật real-time khi chỉnh sửa bảng.
- Nộp từ Màn hình danh sách: Tham chiếu: CF_09.
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
| 2026-05-07 | 1.0 → 1.1 | Bảng thuộc tính — Phạm vi dữ liệu đầu vào | (Không có) | Không có phạm vi | Bổ sung metadata phân loại phạm vi báo cáo |
| 2026-05-07 | 1.0 → 1.1 | Định dạng bảng Markdown | Dòng phân cách không khớp số cột | Sửa dòng phân cách khớp đúng số cột tiêu đề | Chuẩn hóa định dạng Markdown |
| 2026-05-08 | 1.1 → 1.2 | Quy tắc Add/Remove Row | Inline rule chi tiết | Tham chiếu: CMR_15 | Chuẩn hóa quy tắc thêm/xóa hàng |
| 2026-05-11 | +1 | Tên cột | `Ngày cập nhật / Nộp` | `Ngày cập nhật` | Đồng bộ tên cột theo CS_02 (INS-03) |
| 2026-05-11 | +1 | Kiểu field Năm báo cáo | `Number` | `Yearpicker` | Đồng nhất kiểu field (INS-04) |
| 2026-05-11 | +1 | Dòng phân cách bảng Markdown | Thiếu cột (1 chỗ) | Đủ số cột theo header | Chuẩn hóa separator (INS-05) |
| 2026-05-12 | 1.1 → 1.2 | Quy trình duyệt | Không rõ 2 bước hay >2 bước | Xác nhận 2 bước: Nộp → Đã tiếp nhận | Giải quyết Q1 audit |
| 2026-05-12 | 1.1 → 1.2 | Nút [Nhập từ file] | Hiển thị khi Trong thời hạn | Không áp dụng cho Mẫu II.6 | Giải quyết Q2 audit |
| 2026-05-12 | 1.1 → 1.2 | Ngưỡng "dòng hợp lệ" | Không rõ | Có ít nhất 1 trường được nhập | Giải quyết Q3 audit |
| 2026-05-12 | 1.1 → 1.2 | Validate multi-row UX | Không mô tả | Highlight tất cả, scroll dòng đầu, song song 2 bảng | Giải quyết Q4 audit |
| 2026-05-12 | 1.1 → 1.2 | CMR_08 inline | Chưa định nghĩa | Format "Năm [YYYY]", tự sinh theo năm, hạn nộp 31/03 năm kế | Giải quyết Q5 audit |
| 2026-05-12 | 1.1 → 1.2 | Dropdown Quốc gia | Không rõ nguồn | API + CMR_12 + Searchable | Giải quyết Q6 audit |
| 2026-05-12 | 1.1 → 1.2 | Năm báo cáo lower bound | Chỉ ≤ năm hiện tại | ≥ 1990 và ≤ năm hiện tại | Giải quyết Q7 audit |
| 2026-05-12 | 1.1 → 1.2 | Trường số tiền | Chỉ ghi > 0 | Bổ sung: 0.00 bị từ chối, max 999B, auto-format dấu phẩy ngàn | Giải quyết Q8 audit |
| 2026-05-12 | 1.1 → 1.2 | Max length fields bảng | Không ghi | Tên NĐT 500, Mã DN 50, Mã GCNĐT 100, Địa chỉ 1000, Mục tiêu 1000 | Giải quyết Q9 audit |
| 2026-05-12 | 1.1 → 1.2 | Redirect sau Lưu nháp | Không rõ | Quay lại Danh sách (CF_01) | Giải quyết Q10 audit |
| 2026-05-12 | 1.1 → 1.2 | Nút [Xem trước] | Naming không nhất quán | Đổi thành [Xem trước] (popup) vs [Xem chi tiết] (full-page) | Giải quyết Q11 audit |
| 2026-05-12 | 1.1 → 1.2 | Tên file Xuất báo cáo | Không mô tả | Format: [Mã BC]_nam-[YYYY]_NHNN.docx | Giải quyết Q12 audit |
| 2026-05-12 | 1.1 → 1.2 | Empty States | Không mô tả | Bổ sung 4 trường hợp empty state text | Giải quyết Q13 audit |
| 2026-05-12 | 1.1 → 1.2 | Template Phần Dẫn | Không mô tả | Bổ sung template câu văn đầy đủ | Giải quyết Q14 audit |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (2 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them CMR_18 vao tham chieu CF_01 | Tuan thu CMR_18 Tab Navigation tren form nhap lieu |
| 2026-05-17 | CMR v2.0 | STD-02 Required messages (1 truong) | Truong bat buoc | Vui long nhap/chon [ten truong] | Dong bo CMR_05/06/07 v2.0 |
| 2026-05-17 | CMR v2.0 | STD-04a Placeholder text/numeric (12 truong) | Nhap du lieu | Nhap [ten truong cu the] | CMR_06 STD-04a |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-18 | 1.2 → 1.3 | Bảng thuộc tính — Loại quy trình | (Không có) | Quy trình 3 bước, CMCĐT_BCTK_09 | Bổ sung metadata loại quy trình |
| 2026-05-22 | 1.3 → 1.4 | Fields 8, 20 Tên NĐT — Max length | Max 500 ký tự | Max 255 ký tự | Align CMR: CMR_06 (A06) — Textbox max 255 |
| 2026-05-22 | 1.3 → 1.4 | Fields 11, 23 Địa chỉ trụ sở — Max length | Max 1000 ký tự | Max 255 ký tự | Align CMR: CMR_06 (A06) — Textbox max 255 |
| 2026-05-22 | 1.3 → 1.4 | Fields 12, 24 Mục tiêu HĐ — Max length | Max 1000 ký tự | Max 255 ký tự | Align CMR: CMR_06 (A06) — Textbox max 255 |
| 2026-05-22 | 1.3 → 1.4 | Field 28 Đề xuất kiến nghị — Max length | Max 1000 ký tự | Max 3000 ký tự | Align CMR: CMR_06 (A06) — Textarea max 3000 |
| 2026-05-22 | 1.3 → 1.4 | Fields 13, 25 Vốn/Tiền chuyển — Decimal precision | tối đa 2 chữ số thập phân | phần nguyên tối đa 15 chữ số, phần thập phân tối đa 5 chữ số | Align CMR: CMR_05 (C05b) — BA confirmed 15+5 |
