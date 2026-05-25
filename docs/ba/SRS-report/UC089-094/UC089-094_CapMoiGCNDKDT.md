# UC089-094: Báo cáo tình hình cấp mới giấy chứng nhận đăng ký đầu tư/giấy tờ có giá trị tương đương cho nhà đầu tư nước ngoài trong lĩnh vực ... Quý ... Năm ... (Mẫu A.IV.5)

| Thuộc tính                          | Giá trị                                                       |
| ------------------------------------- | --------------------------------------------------------------- |
| **BA phụ trách**              | yen.le2                                                         |
| **Phân hệ**                   | Quản lý đầu tư nước ngoài vào Việt Nam                |
| **Mẫu biểu**                  | Mẫu A.IV.5                                                     |
| **Loại báo cáo**             | Định kỳ quý                                                 |
| **Phạm vi báo cáo**          | Không có phạm vi                                             |
| **Hình thức nộp**            | Báo cáo đơn lẻ (Single report form)                        |
| **Cơ quan nhận**              | Bộ Tài chính (Cục Đầu tư nước ngoài)                  |
| **Đối tượng lập**          | Bộ Tư pháp / Bộ Công thương / Ngân hàng Nhà nước VN |
| **Giao diện**                  | Admin site                                                      |
| **Ngày tạo**                  | 2026-04-23                                                      |
| **Phiên bản**                 | 1.7                                                             |
| **Đơn vị tiền**             | USD                                                             |
| **Quy tắc sinh mã báo cáo** | FDI_AIV5_[ID]                                                   |
| **Loại quy trình**           | Quy trình 3 bước, CMCĐT_BCTK_09                                |

> **Lưu ý:** Báo cáo được lập **riêng biệt bởi từng Bộ** (Bộ Tư pháp / Bộ Công thương / Ngân hàng Nhà nước VN). Mỗi Bộ gửi 1 bản độc lập theo lĩnh vực quản lý của mình. Phạm vi dữ liệu hiển thị theo CMR_02.

---

## UC089-094.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo tình hình cấp mới GCNĐKĐT/giấy tờ tương đương cho NĐT nước ngoài (Mẫu A.IV.5)
- Chức năng cho phép Bộ Tư pháp / Bộ Công thương / Ngân hàng Nhà nước VN truy cập danh sách báo cáo định kỳ quý, được nhóm theo từng Kỳ hạn báo cáo. Mỗi Bộ chỉ thấy báo cáo do Bộ mình lập. Mục tiêu: Hỗ trợ nộp báo cáo trực tuyến, thuận tiện kiểm duyệt, lưu trữ dữ liệu và theo dõi lịch sử.
- Out of scope: Không cho phép nộp báo cáo trễ hạn. Việc duyệt báo cáo được thực hiện ở một UC riêng biệt.

Phân quyền: Bộ Tư pháp / Bộ Công thương / Ngân hàng Nhà nước VN.

Truy cập chức năng: Phân hệ Báo cáo → Quản lý ĐTNN vào VN → Báo cáo cấp mới GCNĐKĐT theo lĩnh vực (Mẫu A.IV.5)

Chức năng đáp ứng usecase số: 89, 90, 91, 92, 93, 94

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện: **Periodic-single** — Giao diện mẫu cho báo cáo có kỳ hạn và gửi lẻ từng báo cáo.

Mô tả giao diện:

| #                                                     | Tên trường          | Kiểu trường              | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả                                                                                                                                                                                                                          |
| ----------------------------------------------------- | ---------------------- | --------------------------- | --------------------- | ------------ | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Khung Điều kiện Lọc & Tìm kiếm**        |                        |                             |                       |              |            |                                                                                                                                                                                                                                  |
| 1                                                     | Năm                   | Yearpicker                  | Năm hiện tại       | x            |            | Người dùng nhấp để chọn năm. Hệ thống lọc và nhóm danh sách theo năm. Kết quả hiển thị ngay, không cần nhấn thêm nút. Tham chiếu: CMR_07.                                                               |
| 2                                                     | Quý                   | Multiple-selection Dropdown | Tất cả                | x            |            | Lọc theo quý. Người dùng chọn một hoặc nhiều giá trị: Tất cả / Quý 1 / Quý 2 / Quý 3 / Quý 4. Kết quả hiển thị ngay sau khi chọn. Logic filter: AND khi chọn nhiều giá trị đồng thời với các bộ lọc khác. Tham chiếu: CMR_07., CMR_16                                                                |
| 3                                                     | Trạng thái kỳ       | Multiple-selection Dropdown | Tất cả                | x            |            | Lọc theo trạng thái kỳ hạn. Chọn một hoặc nhiều giá trị: Tất cả / Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Kết quả hiển thị ngay. Logic filter: AND khi chọn nhiều giá trị đồng thời với các bộ lọc khác. Tham chiếu: CMR_04, CMR_07., CMR_16                                              |
| 4                                                     | Trạng thái báo cáo | Multiple-selection Dropdown | Tất cả                | x            |            | Người dùng chọn một hoặc nhiều giá trị: Tất cả / Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Logic filter: AND khi chọn nhiều giá trị đồng thời với các bộ lọc khác. Tham chiếu: CMR_03, CMR_07., CMR_16                                 |
| 5                                                     | Mã báo cáo          | Search bar                  | Null                  | x            |            | Nhập liệu tự do để tìm theo mã báo cáo. Kết quả hiển thị ngay khi nhập. Nếu không tìm thấy: hiển thị "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo".             |
| **Khung Danh sách Kỳ hạn**                   |                        |                             |                       |              |            |                                                                                                                                                                                                                                  |
| 6                                                     | Kỳ hạn báo cáo     | Label                       | Null                  |              |            | Hiển thị tên kỳ hạn (VD: "Quý 1 Năm 2026"). Mặc định collapse; người dùng click để expand. Tham chiếu: CMR_08.                                                                                                   |
| 7                                                     | Trạng thái kỳ       | Label                       | Null                  |              |            | Trạng thái kỳ hạn: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04.                                                                                                                              |
| 8                                                     | Lập báo cáo         | Button                      | Null                  |              |            | Hiển thị trong header của mỗi kỳ. Chỉ hiển thị khi Trong thời hạn. Ẩn khi Chưa tới hạn hoặc đã Qua kỳ báo cáo. Tham chiếu: CF_01.                                                                           |
| 9                                                     | Nhập từ file                 | Button                      | Null                  |              |            | Hiển thị trong header của mỗi kỳ. Chỉ hiển thị khi Trong thời hạn. Khi nhấn hiển thị popup có link tải template mẫu và nút chọn file tải lên (Format:**.xlsx only**, max 10MB. Không hỗ trợ .csv). |
| **Khung Danh sách Báo cáo** (trong mỗi kỳ) |                        |                             |                       |              |            |                                                                                                                                                                                                                                  |
| 9.1                                                   | Empty State            | Label                       | Null                  |              |            | Nếu danh sách báo cáo trống, hiển thị hình ảnh minh họa kèm text: "Chưa có báo cáo nào".                                                                                                                         |
| 10                                                    | Mã báo cáo          | Label                       | Null                  |              |            | Hiển thị mã báo cáo do hệ thống sinh. Tham chiếu: CMR_09.                                                                                                                                                                |
| 12                                                    | Ngày cập nhật  | Label                       | Null                  |              |            | Định dạng: dd/MM/yyyy HH:mm.                                                                                                                                                                                                  |
| 13                                                    | Trạng thái báo cáo | Label                       | Null                  |              |            | Tham chiếu: CMR_03.                                                                                                                                                                                                             |
| 14                                                    | Hành động           | Button group                | Null                  |              |            | Chi tiết tham chiếu: UC089-094.3. Không hiển thị tooltip khi hover.                                                                                                                                                         |

---

### 3. Mô tả các xử lý của chức năng

- Hệ thống tự động nhóm danh sách theo Kỳ hạn báo cáo (theo quý), mặc định collapse. Người dùng click để expand từng kỳ.
- Sắp xếp kỳ hạn giảm dần (kỳ mới nhất lên đầu). Báo cáo trong mỗi kỳ sắp xếp mới → cũ.
- Các nút [Lập báo cáo] và [Nhập từ file] bị ẩn với kỳ chưa bắt đầu (Chưa tới hạn) và kỳ đã qua (Qua kỳ báo cáo). Tham chiếu: CF_01.
- Mỗi Bộ chỉ thấy báo cáo của Bộ mình.
- Tất cả bộ lọc hiển thị kết quả ngay lập tức, không cần nhấn thêm nút.
- Phân trang. Tham chiếu: CMR_10.

---

## UC089-094.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Lập mới Báo cáo cấp mới GCNĐKĐT theo lĩnh vực (Mẫu A.IV.5)
- Chức năng cho phép từng Bộ lập báo cáo gồm Header auto-fill theo tổ chức đăng nhập và Bảng dynamic table 19 cột. Khi nhập Mã số dự án (C2), hệ thống có thể gọi API CSDL chuyên ngành để auto-fill các cột còn lại của dòng.

Phân quyền: Bộ Tư pháp / Bộ Công thương / Ngân hàng Nhà nước VN.

Truy cập chức năng: Màn danh sách báo cáo (UC089-094.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 89, 90

---

### 2. Mô tả giao diện

**PHẦN HEADER**

| # | Tên trường        | Kiểu trường  | Giá trị mặc định                   | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                                                                                                                  |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Tên Bộ/Ngành      | Label           | Auto-fill từ tổ chức của user login |              |            | Disabled. Ví dụ: "NGÂN HÀNG NHÀ NƯỚC VIỆT NAM". Tham chiếu: CMR_12.                                                                                                                                                                                                                                                                                                                      |
| 2 | Lĩnh vực báo cáo | Text (Editable) | Auto-suggest theo Bộ                   | x            | x          | Hệ thống gợi ý default theo tổ chức: Bộ Công thương → "DẦU KHÍ"; Bộ Tư pháp → "CÔNG TY LUẬT"; Ngân hàng Nhà nước VN → "NGÂN HÀNG NƯỚC NGOÀI". Người dùng được phép thay đổi giá trị. Giá trị này điền vào biến "TRONG LĨNH VỰC ......" trong tiêu đề báo cáo và cột Lĩnh vực trên màn hình danh sách. Tham chiếu: CMR_06. |
| 3 | Quý báo cáo       | Dropdown        | Quý hiện tại                         |             | x          | Hiển thị quý báo cáo đã chọn từ màn danh sách. **Disabled** — không cho sửa. Tham chiếu: CMR_05.                                                                                                                                                                                                                                                                                                       |
| 4 | Năm báo cáo       | Yearpicker | Năm hiện tại                         |             | x          | Hiển thị năm báo cáo đã chọn từ màn danh sách. **Disabled** — không cho sửa. Tham chiếu: CMR_05.                                                                                                                                                                                                                                                                                                                |

**BẢNG DANH SÁCH DỰ ÁN (Dynamic Table — 19 cột — max 500 dòng)**

Người dùng tự Thêm/Xóa dòng. Khi nhập C2 và blur, hệ thống gọi API auto-fill dữ liệu — tất cả cột vẫn **Editable** để user hiệu chỉnh. Mỗi dòng = 1 dự án/DN được cấp giấy chứng nhận.

| #                     | Tên cột                                                     | Kiểu trường                 | Được sửa                      | Bắt buộc | Mô tả/Ghi chú                                                                                                                                                                                                                                                                                     |
| --------------------- | ------------------------------------------------------------- | ------------------------------ | --------------------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| C1                    | TT                                                            | Label (Auto-increment)         |                                   |            | Hệ thống tự tăng từ 1. Read-only.                                                                                                                                                                                                                                                               |
| C2                    | Mã số dự án/Số GCNĐT/Số Giấy tờ có giá trị tương đương | Text                           | x | x          | Validate: Bắt buộc. Unique trong báo cáo. Text free (không validate format ký tự). Tối đa 255 ký tự. Khi nhập giá trị và blur khỏi ô: hệ thống gọi API CSDL chuyên ngành (nếu có tích hợp) → auto-fill C3→C19 của dòng đó từ bản ghi gần nhất. Placeholder: "Nhập mã số dự án". Error required: "Vui lòng nhập Mã số dự án". Tham chiếu: CMR_05. |
| C3                    | Ngày cấp                                                    | Date Picker                    | x                                 | x          | Validate: Bắt buộc. Ngày cấp ≤ ngày hiện tại. Tham chiếu: CMR_05, CMR_08.                                                                                                                                                                                                                   |
| C4                    | Tên dự án / doanh nghiệp                                  | Text                           | x                                 | x          | Bắt buộc. Tối đa 255 ký tự. Placeholder: "Nhập tên dự án/doanh nghiệp". Error required: "Vui lòng nhập Tên dự án/doanh nghiệp". Tham chiếu: CMR_06.                                                                                                                                                                                                                                                                     |
| C5                    | Vốn đầu tư đăng ký (USD)                               | Decimal                        | x                                 | x          | Validate: ≥ 0. **Decimal precision: tối đa 5 chữ số thập phân.** Ràng buộc: C5 ≥ C8 (Vốn góp Tổng) — validate **chỉ khi Nộp** (Lưu nháp không validate). Tham chiếu: CMR_05, CMR_08.                                                                 |
| C6                    | Vốn góp (USD) - Bên Việt Nam                              | Decimal                        | x                                 | x          | Validate: ≥ 0. **Decimal precision: tối đa 5 chữ số thập phân.** Tham chiếu: CMR_08.                                                                                                                                                                                              |
| C7                    | Vốn góp (USD) - Bên nước ngoài                          | Decimal                        | x                                 | x          | Validate: ≥ 0. **Decimal precision: tối đa 5 chữ số thập phân.** Tham chiếu: CMR_08.                                                                                                                                                                                              |
| C8                    | Vốn góp (USD) - Tổng                                       | Calculated (Disabled)          |                                   |            | Read-only. Auto = C6 + C7. **Decimal precision: tối đa 5 chữ số thập phân.** Cập nhật ngay khi C6 hoặc C7 thay đổi. Tham chiếu: CMR_12.                                                                                                                                                      |
| C9                    | Ngành cấp 1 (theo mục tiêu chính của dự án)             | Dropdown (VSIC cấp 1)         | x                                 | x          | Chọn từ danh mục ngành cấp 1 theo QĐ 36/2025/QĐ-TTg.**:** Nếu API tích hợp: hệ thống tự động ánh xạ tên ngành từ giấy phép chuyên ngành → Mã ngành cấp 1 QĐ 36/2025. Tham chiếu: CMR_05.                                                                         |
| C10                   | Mục tiêu                                                    | Textarea                       | x                                 | x          | Nhập mô tả chi tiết mục tiêu hoạt động của dự án. Tối đa 3000 ký tự. Error maxlength: "[Tên trường] không được vượt quá 3000 ký tự". Nếu API tích hợp, tự động điền thông tin từ cơ sở dữ liệu giấy chứng nhận được cấp. Placeholder: "Nhập mục tiêu". Error required: "Vui lòng nhập Mục tiêu". Tham chiếu: CMR_06.                                                                                                           |
| C11                   | Thời hạn thực hiện dự án                                | Text                           | x                                 | x          | Bắt buộc. Tối đa 255 ký tự. Theo thông tin trên giấy phép (VD: 50 năm, 70 năm). Placeholder: "Nhập thời hạn thực hiện dự án". Error required: "Vui lòng nhập Thời hạn thực hiện dự án". Tham chiếu: CMR_06.                                                                                                                                                                                                           |
| C12                   | Địa chỉ trụ sở DN / địa điểm dự án                 | Text                           | x                                 | x          | Bắt buộc. Tối đa 255 ký tự. Placeholder: "Nhập địa chỉ". Error required: "Vui lòng nhập Địa chỉ trụ sở DN/địa điểm dự án". Tham chiếu: CMR_06.                                                                                                                                                                                                                                                                     |
| C13                   | Nhà đầu tư nước ngoài - Tên                                     | Text                           | x                                 | x          | Bắt buộc. Tối đa 255 ký tự. Placeholder: "Nhập tên nhà đầu tư nước ngoài". Error required: "Vui lòng nhập Tên nhà đầu tư nước ngoài". Tham chiếu: CMR_06.                                                                                                                                                                                                                                                                     |
| C14                   | Nhà đầu tư nước ngoài - Địa chỉ                               | Text                           | x                                 | x          | Bắt buộc. Tối đa 255 ký tự. Placeholder: "Nhập địa chỉ NĐT nước ngoài". Error required: "Vui lòng nhập Địa chỉ nhà đầu tư nước ngoài". Tham chiếu: CMR_06.                                                                                                                                                                                                                                                                     |
| C15                   | Nhà đầu tư nước ngoài - Nước đăng ký                        | Dropdown (Danh mục Quốc gia) | x                                 | x          | Bắt buộc. Chọn từ danh mục quốc gia chuẩn quốc tế. Tham chiếu: CMR_05.                                                                                                                                                                                                                     |
| C16                   | Nhà đầu tư Việt Nam - Tên                                         | Text                           | x                                 |            | Không bắt buộc. Tối đa 255 ký tự. Bỏ trống nếu dự án 100% vốn nước ngoài. Placeholder: "Nhập tên NĐT Việt Nam". Tham chiếu: CMR_06.                                                                                                                                                                                                             |
| C17                   | Nhà đầu tư Việt Nam - Địa chỉ                                   | Text                           | x                                 |            | Không bắt buộc. Tối đa 255 ký tự. Placeholder: "Nhập địa chỉ NĐT Việt Nam". Tham chiếu: CMR_06.                                                                                                                                                                                                                                                              |
| C18                   | Ưu đãi đầu tư (nếu có)                                | Textarea                       | x                                 |            | Không bắt buộc. Tối đa 3000 ký tự. Error maxlength: "[Tên trường] không được vượt quá 3000 ký tự". Nếu API tích hợp, tự động điền thông tin từ cơ sở dữ liệu giấy chứng nhận được cấp. Placeholder: "Nhập ưu đãi đầu tư". Tham chiếu: CMR_06.                                                                                                                                                    |
| C19                   | Ghi chú                                                      | Text                           | x                                 |            | Không bắt buộc. Tối đa 255 ký tự. Placeholder: "Nhập ghi chú". Tham chiếu: CMR_06.                                                                                                                                                                                                                                                              |
| **TỔNG CỘNG** |                                                               |                                |                                   |            |                                                                                                                                                                                                                                                                                                      |
| T                     | Tổng cộng                                                   | Calculated (Disabled)          |                                   |            | Dòng cuối bảng. Hệ thống tự SUM dọc các cột vốn: C5, C6, C7, C8. **Decimal precision: tối đa 5 chữ số thập phân.** Cập nhật realtime. Read-only.                                                                                                                                       | Tham chiếu: CMR_06.                                                                                                                                                                                                                                                              |
| T                     | Tổng cộng                                                   | Calculated (Disabled)          |                                   |            | Dòng cuối bảng. Hệ thống tự SUM dọc các cột vốn: C5, C6, C7, C8. **Decimal precision: tối đa 5 chữ số thập phân.** Cập nhật realtime. Read-only.                                                                                                                                       |

**FOOTER**

| #  | Tên trường     | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú                                                                     |
| --- | --- | --- | --- | --- | --- | --- |
| F1 | Địa danh        | Label          | Auto-fill             |              |            | Disabled. Tên Tỉnh/Thành phố theo cơ quan của user login. Tham chiếu: CMR_12. |
| F2 | Ngày/tháng/năm | Date           | Auto-fill             |              |            | Disabled. Thời gian thực tại thời điểm lập báo cáo. Tham chiếu: CMR_12.    |

**CÁC BUTTON**

| #  | Tên           | Kiểu                           | Mô tả                                                                                                                                                                                                   |
| -- | -------------- | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| --- | --- | --- | --- |
| B1 | Hủy           | Button                          | Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]").                                                                                                                                                          |
| B2 | Xem trước | Button | Mở popup PDF Preview báo cáo (không rời màn Lập). Tham chiếu: CF_07.1.                                                                                                                              |
| B3 | Lưu nháp     | Button                          | Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]").                                                                                                                                                    |
| B4 | Nộp báo cáo | Button                          | Validate toàn bộ trường bắt buộc.**Empty table rule:** Không cho phép nộp nếu 0 dòng → Toast T15 *"Vui lòng nhập ít nhất 1 dòng dữ liệu"*. Tham chiếu: CF_01.                         |
| —  | Xóa dòng     | Icon Button (mỗi dòng) | Hiển thị trên tất cả dòng. Xóa trực tiếp không cần popup xác nhận. STT re-index liên tục. Tham chiếu: CF_08, CMR_15. |

---

### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu: CF_01 (Lập báo cáo), CMR_18, CF_04 (Xuất báo cáo Excel), CF_05 (In).

**Xử lý đặc thù biểu mẫu A.IV.5:**

- **Phân quyền theo Bộ:** Hệ thống xác định Bộ của user login để auto-fill Tên Bộ/Ngành và gợi ý Lĩnh vực mặc định. Mỗi Bộ chỉ xem và thao tác báo cáo của Bộ mình. Tham chiếu: CMR_12.
- **Lĩnh vực báo cáo:** Field Editable. Gợi ý default theo Bộ, người dùng được phép ghi đè. Giá trị được lưu vào báo cáo và hiển thị trong cột Lĩnh vực trên danh sách. Tham chiếu: CMR_06.
- **Auto-fill qua API:** Khi user nhập C2 và rời khỏi ô (blur), hệ thống gọi API CSDL chuyên ngành tương ứng để lấy bản ghi gần nhất và auto-fill C3→C19. Tất cả cột vẫn **Editable** — người dùng được phép hiệu chỉnh dữ liệu API nếu cần. Người dùng chịu trách nhiệm cuối cùng về nội dung báo cáo.
- **Lỗi API (Timeout/Mất kết nối):** Hiển thị Toast T05. Tham chiếu: CMR_12. Enable toàn bộ C3→C19 cho nhập thủ công.
- **Auto-map Ngành C9:** Nếu có API tích hợp, hệ thống tự ánh xạ tên ngành từ giấy phép chuyên ngành sang Mã ngành cấp 1 theo QĐ 36/2025/QĐ-TTg.
- **Auto-calculate C8:** C8 = C6 + C7, cập nhật realtime. Disabled.
- **Validate C5 ≥ C8:** **Chỉ khi Nộp** (Lưu nháp KHÔNG validate). Kiểm tra C5 ≥ C8. Nếu vi phạm → hiển thị lỗi inline tại C5: *"Vốn đầu tư đăng ký (C5) không được nhỏ hơn Tổng vốn góp (C8)"*. Tham chiếu: CMR_05.
- **Validate Unique C2:** Không cho phép trùng giá trị C2 trong cùng 1 báo cáo. Tham chiếu: CMR_05.
- **Dòng Tổng cộng:** SUM dọc C5, C6, C7, C8 toàn bộ dòng dữ liệu. **Decimal: tối đa 5 chữ số thập phân.** Cập nhật realtime. Disabled. Dòng Tổng luôn ở cuối bảng, không tham gia sort.
- **Sort:** Các cột có giá trị ngày hoặc số (C3, C5, C6, C7, C8) có icon sort trên header. Click icon → toggle: Ascending ↑ / Descending ↓. **Mặc định sort theo C3 (Ngày cấp): xa nhất → gần nhất (descending).** Dòng mới thêm vào cuối bảng, user tự sort lại nếu muốn. Sort persist khi Lưu nháp → mở lại giữ nguyên thứ tự. Khi API auto-fill, hệ thống auto-sort theo default sort trước khi render.
- **Concurrent edit:** Áp dụng Last Write Wins — khi 2 user cùng Bộ cùng lưu/nộp cùng lúc, thao tác sau ghi đè thao tác trước. Cả 2 thao tác đều được ghi vào Lifecycle Log (Actor, Action, Timestamp). Tham chiếu: CMR_02, CF_06.
- **Footer:** F1 (Địa danh) và F2 (Ngày/tháng/năm) auto-fill và Disabled khi khởi tạo báo cáo. Tham chiếu: CMR_12.
- **Xuất báo cáo:** Kết xuất file **Excel**. Tham chiếu: CF_04.
- Chỉnh sửa: Tham chiếu: CF_03.

#### 3.4 Tiêu chí nghiệm thu (Acceptance Criteria)

- **AC1:** Dữ liệu Nhập từ file: Người dùng mở popup Nhập từ file, tải lên file đúng template (**.xlsx only**) và dung lượng ≤ 10MB → hệ thống xử lý thành công.
- **AC2:** Auto-fill API: Người dùng nhập Mã dự án (C2) hợp lệ, blur khỏi ô nhập liệu → hệ thống tự động gọi API điền dữ liệu vào C3→C19. Tất cả cột vẫn Editable — user được phép hiệu chỉnh.
- **AC3:** Lỗi kết nối API: Người dùng nhập Mã dự án (C2) nhưng hệ thống mất kết nối mạng, blur khỏi ô → hệ thống hiển thị thông báo "Không thể kết nối. Vui lòng kiểm tra mạng và thử lại.", đồng thời cho phép nhập thủ công C3→C19.
- **AC4:** Validate logic: Người dùng nhập Tổng vốn góp (C8) lớn hơn Vốn ĐT đăng ký (C5), nhấn **Nộp** (không áp dụng khi Lưu nháp) → hệ thống chặn hành động và hiển thị lỗi inline dưới cột C5: "Vốn đầu tư đăng ký (C5) không được nhỏ hơn Tổng vốn góp (C8)".
- **AC5:** Nút Nộp: Bản ghi ở trạng thái Lưu nháp hoặc Yêu cầu chỉnh sửa, các trường bắt buộc đã được điền đủ → nút Nộp báo cáo chuyển sang trạng thái Active.
- **AC6:** API partial fill: API chỉ trả một phần fields → fill các trường có data, các trường thiếu để trống cho user nhập manual.
- **AC7:** API fail: API timeout/mất kết nối → Toast T05 (Tham chiếu: CMR_12) + enable toàn bộ C3→C19 cho nhập manual.
- **AC8:** Sort: Mặc định sort theo C3 (Ngày cấp) descending. User click icon sort trên header C3/C5/C6/C7/C8 để toggle Ascending/Descending. Dòng Tổng luôn ở cuối. Sort persist khi Lưu nháp.
- **AC9:** Max rows: Bảng đã có 500 dòng, user nhấn [Thêm dòng] → Toast T16 *"Vượt quá số dòng tối đa cho phép (500)"*.
- **AC10:** Empty table: Bảng có 0 dòng, user nhấn [Nộp] → Toast T15 *"Vui lòng nhập ít nhất 1 dòng dữ liệu"* và chặn nộp.
- **AC11:** Concurrent edit: 2 user cùng mở chỉnh sửa, cả 2 cùng lưu/nộp → thao tác sau ghi đè thao tác trước. Cả 2 thao tác được ghi vào Lifecycle Log (Actor, Action, Timestamp). Tham chiếu: CMR_02, CF_06.

#### 3.5 Yêu cầu phi chức năng (NFR)

- **Performance:** Thời gian tải danh sách báo cáo (Load list) < 3s. Thời gian xử lý Nhập từ file file Excel < 10s. API timeout: 5s.
- **Security:** Phân quyền truy cập bằng Role-Based Access Control (RBAC). Ghi log hệ thống (audit log) đầy đủ đối với các thao tác nhạy cảm như Xóa, Nộp báo cáo.
- **Concurrency:** Áp dụng Last Write Wins — khi 2 user cùng lưu/nộp cùng lúc, thao tác sau ghi đè thao tác trước. Cả 2 thao tác đều được ghi vào Lifecycle Log (Actor, Action, Timestamp). Tham chiếu: CMR_02, CF_06.

---

## UC089-094.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ – Xem chi tiết, Xem vòng đời, In, Xuất báo cáo, Nộp, Chỉnh sửa
- Cho phép người dùng thực hiện tác vụ tương ứng trạng thái bản ghi.

Phân quyền: Bộ Tư pháp / Bộ Công thương / Ngân hàng Nhà nước VN. Tham chiếu: CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC089-094.1) → Cột Hành động → Chọn tác vụ tương ứng

Chức năng đáp ứng usecase số: 91, 92, 93, 94

---

### 2. Mô tả giao diện

| # | Tên            | Kiểu  | Điều kiện hiển thị                         | Phân quyền           | Mô tả                                                                                                                                                                          |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp            | Button | Chỉ khi Lưu nháp hoặc Yêu cầu chỉnh sửa | Người tạo           | Nút enable khi các trường bắt buộc đã được điền. Tham chiếu: CF_09, CF_01. Sau khi nộp thành công, hiển thị notification trên giao diện web cho Cục ĐTNN. |
| 2 | Chỉnh sửa     | Button | Chỉ khi Lưu nháp hoặc Yêu cầu chỉnh sửa | Người tạo           | Tham chiếu: CF_03.                                                                                                                                                              |
| 3 | Xem chi tiết   | Button | Tất cả trạng thái                                | Tất cả người dùng | Mở bảng ở chế độ read-only. Tham chiếu: CF_07.                                                                                                                            |
| 4 | Xem vòng đời | Button | Tất cả trạng thái                                | Tất cả người dùng | Mở popup Vòng đời. Tham chiếu: CF_06.                                                                                                                                       |
| 5 | In              | Button | Tất cả trạng thái                                | Tất cả người dùng | Tham chiếu: CF_05.                                                                                                                                                              |
| 6 | Xuất báo cáo          | Button | Tất cả trạng thái                                | Tất cả người dùng | Kết xuất file Excel. Tham chiếu: CF_04.                                                                                                                                       |
| 7 | Xóa            | Button | Lưu nháp**VÀ** chưa từng nộp        | Người tạo           | Tham chiếu: CF_08. Xóa có lưu log (soft-delete).                                                                                                                             |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết: Tham chiếu: CF_07.
- Xem vòng đời: Tham chiếu: CF_06.
- In báo cáo: Tham chiếu: CF_05.
- Xuất báo cáo: Kết xuất ra file Excel. Tham chiếu: CF_04.
- Chỉnh sửa: Tham chiếu: CF_03.

---

## 4. Lịch sử cập nhật

| Ngày      | Phiên bản | Mục cập nhật        | Before                        | After                                                                                    | Ghi chú                                                       |
| ---------- | ----------- | ---------------------- | ----------------------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| 2026-05-03 | N/A         | Trạng thái báo cáo | Đã nộp                     | Chờ duyệt / Đã tiếp nhận                                                           | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-06 | 1.0 → 1.1  | Mã báo cáo          | FDI_AIV5_[ID]                 | FDI_AIV5_[ID]                                                                            | Chuyển đổi prefix FDI theo CMR_09.                          |
| 2026-05-06 | 1.0 → 1.1  | Objective & Scope      | (Không có)                  | Mô tả chi tiết mục tiêu hỗ trợ nộp trực tuyến và Out of Scope nộp trễ hạn. | Bổ sung theo phản hồi của BA.                              |
| 2026-05-06 | 1.0 → 1.1  | Empty State            | (Không có)                  | Bổ sung dòng 10.1: "Chưa có báo cáo nào".                                         | Cải thiện UI/UX.                                             |
| 2026-05-06 | 1.0 → 1.1  | API Logic & Validation | Mô tả sơ sài.             | Bổ sung logic khóa API (CMR_12), báo lỗi mạng, và validate C5 >= C8.               | Chuẩn hóa logic theo rule hệ thống.                        |
| 2026-05-06 | 1.0 → 1.1  | Post-conditions        | (Không có)                  | Thêm Notification khi Nộp và Audit log khi Xóa.                                      | Bổ sung luồng xử lý hậu kỳ.                              |
| 2026-05-06 | 1.0 → 1.1  | Acceptance Criteria    | (Không có)                  | Thêm 5 AC (AC1 -> AC5).                                                                 | Đảm bảo tính có thể test (Testability).                  |
| 2026-05-07 | 1.1 → 2.0  | Decimal precision      | Không rõ                    | 2 chữ số thập phân, round half up (C5-C8, T)                                         | Chuẩn hóa số liệu USD.                                     |
| 2026-05-07 | 1.1 → 2.0  | Validate C5 ≥ C8      | Khi Lưu/Nộp                 | Chỉ khi Nộp                                                                            | Lưu nháp không validate.                                    |
| 2026-05-07 | 1.1 → 2.0  | Mã dự án C2         | 10 chữ số / [Số/Ký hiệu] | Alphanumeric +`/`, `-`, max 20 ký tự                                               | Format rõ ràng hơn.                                         |
| 2026-05-07 | 1.1 → 2.0  | API row behavior       | Enabled                       | Disabled (không sửa, không xóa)                                                      | Bảo toàn dữ liệu API.                                      |
| 2026-05-07 | 1.1 → 2.0  | Nhập từ file                 | .xls/.xlsx                    | .xlsx only                                                                               | Chuẩn hóa format.                                            |
| 2026-05-07 | 1.1 → 2.0  | Max rows               | Không giới hạn             | 500 dòng                                                                                | Giới hạn hiệu năng.                                        |
| 2026-05-07 | 1.1 → 2.0  | API partial fill       | Không đề cập              | Fill có data + enable thiếu + Toast warning                                            | Xử lý edge case.                                             |
| 2026-05-07 | 1.1 → 2.0  | API fail               | Thông báo chung             | Toast T05 + enable toàn bộ manual                                                      | Fallback rõ ràng.                                            |
| 2026-05-07 | 1.1 → 2.0  | Empty table            | Không đề cập              | Không cho phép nộp 0 dòng                                                            | Validate dữ liệu.                                            |
| 2026-05-07 | 1.1 → 2.0  | Concurrency            | Không đề cập              | Optimistic locking                                                                       | Xử lý concurrent edit.                                       |
| 2026-05-07 | 1.1 → 2.0  | AC bổ sung            | 5 AC                          | 11 AC (AC6-AC11 mới)                                                                    | Bao phủ edge cases.                                           |
| 2026-05-11 | 1.0→1.1 | Quy tắc sinh mã báo cáo | `FDI_A4_5_[ID]` | `FDI_AIV5_[ID]` | Chuẩn hóa prefix và mã theo appendices.md v2.0 (INS-10) |
| 2026-05-11 | +1 | Điều kiện hiển thị nút | `Luôn hiển thị` | `Tất cả trạng thái` | Chuẩn hóa điều kiện (INS-07) |
| 2026-05-11 | +1 | Kiểu field Năm báo cáo | `Number` | `Yearpicker` | Đồng nhất kiểu field (INS-04) |
| 2026-05-11 | +1 | Dòng phân cách bảng Markdown | Thiếu cột (3 chỗ) | Đủ số cột theo header | Chuẩn hóa separator (INS-05) |
| 2026-05-11 | +1 | Dòng phân cách Markdown | Sai số cột | 4 cột đúng | Sửa lỗi Markdown (INS-05) |
| 2026-05-11 | 1.2 → 1.3 | Toast T05 (lỗi API) | Nội dung toast tự viết | Tham chiếu CMR_12 (T05 chuẩn) | QC Feedback — chuẩn hóa toast. |
| 2026-05-11 | 1.2 → 1.3 | AC11 + NFR Concurrency | Optimistic locking — conflict + refresh | Last Write Wins theo CMR_02 — thao tác sau ghi đè, cả 2 ghi Lifecycle Log | QC Feedback — đồng bộ CMR_02, CF_06. |
| 2026-05-14 | 1.3 → 1.4 | Filter Lĩnh vực (danh sách) | Có filter Lĩnh vực (row #4) | Xóa — không cần filter theo lĩnh vực | Client feedback. |
| 2026-05-14 | 1.4 | Lĩnh vực mặc định | Bộ Tư pháp: "HÀNH NGHỀ LUẬT SƯ"; Bộ Công thương: "THƯƠNG MẠI/NHƯỢNG QUYỀN THƯƠNG MẠI"; NHNN: "NGÂN HÀNG" | Bộ Công thương: "DẦU KHÍ"; Bộ Tư pháp: "CÔNG TY LUẬT"; NHNN: "NGÂN HÀNG NƯỚC NGOÀI" | Client feedback — cập nhật tên lĩnh vực. |
| 2026-05-14 | 1.4 | C2 validation | Alphanumeric + `/`, `-`, max 20 ký tự | Text free (không validate format), max 50 ký tự | Client feedback — nới lỏng format. |
| 2026-05-14 | 1.4 | C5, C6, C7, C8, T decimal | 2 chữ số thập phân, round half up | Tối đa 5 chữ số thập phân | Client feedback — tăng precision. |
| 2026-05-14 | 1.4 | C11 | Không có placeholder | Thêm placeholder: "VD: 50 năm (kể từ ngày cấp GCN)" | Client feedback. |
| 2026-05-14 | 1.4 | Dòng API | Disabled (không sửa, không xóa), có tag "API" | Editable (cho sửa, cho xóa), bỏ tag "API" — user chịu trách nhiệm cuối | Client feedback — cho phép hiệu chỉnh dữ liệu API. |
| 2026-05-14 | 1.4 | Sort | Không có | Thêm icon sort cho C3, C5, C6, C7, C8. Mặc định sort C3 descending. Persist khi Lưu nháp | Client feedback — thêm sort. |
| 2026-05-14 | 1.4 | AC | AC8 (dòng API Disabled) | Bỏ AC8, thêm AC8 (Sort behavior) | Đồng bộ với thay đổi API Editable + Sort. |
| 2026-05-14 | 1.4 → 1.5 | Xử lý API partial | Có mục "API auto-fill partial" + Toast warning chi tiết | Xóa — logic đã gộp vào AC6 | QC Review — loại bỏ mô tả thừa. |
| 2026-05-14 | 1.5 | AC | Format Given/When/Then (tiếng Anh) | Viết lại tiếng Việt thuần, bỏ Given/When/Then | QC Review — chuẩn hóa ngôn ngữ AC. |
| 2026-05-14 | 1.5 → 1.6 | Quý + Năm báo cáo (form Lập) | Editable, cho phép chọn/nhập | Disabled — hiển thị quý/năm đã chọn từ màn danh sách | QC Review — kỳ đã xác định từ danh sách, không cần nhập lại. |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (3 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them , CMR_18 vao tham chieu CF_01 tren man hinh lap bao cao | Tuan thu CMR_18 Tab Navigation (STD-07) |
| 2026-05-17 | CMR v2.0 | STD-04a Custom Placeholder | 1 truong khong chuan | Dong bo Nhap [ten truong] (Goi y) | CMR_06 |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-22 | 1.6 → 1.7 | Xóa dòng (popup) | Popup xác nhận "Bạn có chắc muốn xóa dòng này?" [Đồng ý] / [Hủy] | Xóa trực tiếp không cần popup xác nhận | Follow CMR_15 — xóa không cần popup. |
| 2026-05-22 | 1.7 | Filter logic (AND/OR) | Chưa mô tả logic khi chọn nhiều giá trị | Logic filter: AND khi chọn nhiều giá trị đồng thời với các bộ lọc khác | QC Feedback — clarify filter combination. |
| 2026-05-22 | 1.7 | Giá trị mặc định bộ lọc | Null (3 dropdown: Quý, Trạng thái kỳ, Trạng thái báo cáo) | Tất cả + thêm option "Tất cả" vào danh sách giá trị | Tuân thủ CMR_16 — filter dropdown mặc định "Tất cả". |
| 2026-05-22 | 1.7 | Cột Lĩnh vực (danh sách báo cáo) | Có cột Lĩnh vực (dòng #11) | Xóa — không hiển thị trên danh sách | Client feedback — đã yêu cầu bỏ từ trước. |
