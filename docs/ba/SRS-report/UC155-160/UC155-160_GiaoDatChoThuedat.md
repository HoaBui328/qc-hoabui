# UC155-160: Báo cáo tình hình giao đất, cho thuê đất và cho phép chuyển mục đích sử dụng đất đối với tổ chức kinh tế có vốn đầu tư nước ngoài trên địa bàn tỉnh/thành phố

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | anh.luu |
| **Phân hệ** | Quản lý đầu tư nước ngoài vào Việt Nam |
| **Mẫu biểu** | Mẫu A.IV.12 |
| **Loại báo cáo** | Định kỳ năm |
| **Hình thức nộp** | Báo cáo đơn lẻ (Single report form) |
| **Phạm vi dữ liệu đầu vào** | Không có phạm vi |
| **Cơ quan nhận** | Bộ Tài chính (Cục Đầu tư nước ngoài); Bộ Nông nghiệp và Môi trường |
| **Đối tượng lập** | UBND cấp tỉnh |
| **Giao diện** | Admin site |
| **Ngày tạo** | 2026-04-23 |
| **Phiên bản** | 1.3 |
| **Quy tắc sinh mã báo cáo** | FDI_AIV12_[ID] |
| **Loại quy trình** | Quy trình 3 bước, CMCĐT_BCTK_09 |

---

## UC155-160.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo tình hình giao đất, cho thuê đất và cho phép chuyển mục đích sử dụng đất đối với tổ chức kinh tế có vốn đầu tư nước ngoài
- Chức năng cho phép UBND cấp tỉnh truy cập danh sách báo cáo định kỳ năm, được nhóm theo từng Kỳ hạn báo cáo.

Phân quyền: UBND cấp tỉnh. Tham chiếu: CMR_02.

Truy cập chức năng: Phân hệ Báo cáo → Quản lý đầu tư nước ngoài vào Việt Nam → Báo cáo tình hình giao đất, cho thuê đất (Mẫu A.IV.12)

Chức năng đáp ứng usecase số: 155, 156, 157, 158, 159, 160

Mapping chi tiết:

| UC | Chức năng |
| --- | --- |
| UC155 | Xem danh sách báo cáo |
| UC156 | Lập mới báo cáo |
| UC157 | Chỉnh sửa báo cáo |
| UC158 | Xóa báo cáo |
| UC159 | Xem chi tiết / Nộp báo cáo |
| UC160 | Xuất báo cáo / In / Xem vòng đời |

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện: **Periodic-single** — Giao diện mẫu cho báo cáo có kỳ hạn và gửi lẻ từng báo cáo.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | | |
| 1 | Năm | Yearpicker | Năm hiện tại | x | | Người dùng nhấp để chọn năm từ calendar picker. Hệ thống lọc và nhóm danh sách theo năm được chọn. Kết quả hiển thị ngay lập tức, không cần nhấn thêm nút. Tham chiếu: CMR_07. |
| 2 | Trạng thái kỳ hạn | Multiple-selection Dropdown | Null | x | | Người dùng chọn một hoặc nhiều giá trị: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_04, CMR_07, CMR_16 |
| 3 | Trạng thái báo cáo | Multiple-selection Dropdown | Null | x | | Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07, CMR_16 |
| 4 | Mã báo cáo | Search bar | Null | x | | Nhập liệu tự do để tìm theo mã báo cáo. Kết quả hiển thị ngay khi nhập. Nếu không tìm thấy: hiển thị "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo" |
| **Khung Danh sách Kỳ hạn** | | | | | | |
| 5 | Kỳ hạn báo cáo | Label | Null | | | Hiển thị tên kỳ hạn (VD: "Năm 2026"). Mặc định collapse; người dùng click để expand danh sách báo cáo bên trong. Tham chiếu: CMR_08. |
| 6 | Trạng thái kỳ | Label | Null | | | Hiển thị trạng thái của kỳ hạn: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| 7 | Lập báo cáo | Button | Null | | | Hiển thị trong header của mỗi kỳ. Chỉ hiển thị khi Trong thời hạn. Ẩn khi Chưa tới hạn hoặc đã Qua kỳ báo cáo. Tham chiếu: CF_01. |
| 8 | Nhập từ file | Button | Null | | | Hiển thị trong header của mỗi kỳ. Chỉ hiển thị khi Trong thời hạn. Ẩn khi Chưa tới hạn hoặc đã Qua kỳ báo cáo. Tham chiếu: CF_02 Case 2 (không có Phạm vi dữ liệu nguồn input). |
| **Khung Danh sách Báo cáo** (trong mỗi kỳ) | | | | | | |
| 9 | Mã báo cáo | Label | Null | | | Hiển thị mã báo cáo do hệ thống sinh theo quy tắc. Tham chiếu: CMR_09 |
| 10 | Năm báo cáo | Label | Null | | | Năm lập báo cáo. |
| 11 | Ngày cập nhật | Label | Null | | | Thời điểm thao tác gần nhất. Định dạng: dd/MM/yyyy HH:mm. |
| 12 | Trạng thái | Label | Null | | | Tham chiếu: CMR_03. |
| 13 | Hành động | Button group | Null | | | Hiển thị các nút thao tác theo trạng thái bản ghi. Chi tiết tham chiếu: UC155-160.3. |

---

### 3. Mô tả các xử lý của chức năng

- Hệ thống tự động nhóm danh sách theo Kỳ hạn báo cáo (theo năm), mặc định collapse. Người dùng click để expand từng kỳ.
- Sắp xếp kỳ hạn giảm dần (kỳ mới nhất lên đầu). Báo cáo trong mỗi kỳ sắp xếp mới → cũ.
- Các nút [Lập báo cáo] và [Nhập từ file] bị ẩn với kỳ chưa bắt đầu (Chưa tới hạn) và kỳ đã qua (Qua kỳ báo cáo). Tham chiếu: CF_01.
- Bản ghi đã tồn tại (Lưu nháp / Yêu cầu chỉnh sửa) vẫn có thể Chỉnh sửa, Nộp, Xóa khi kỳ đã "Qua kỳ báo cáo" — CMR_04 chỉ ẩn nút [Lập báo cáo]/[Nhập từ file], không ảnh hưởng hành động trên bản ghi hiện hữu (theo CMR_03).
- Tất cả bộ lọc hiển thị kết quả ngay lập tức sau khi tương tác, không cần nhấn thêm nút.
- Phân trang. Tham chiếu: CMR_10.
- Empty state — chưa có kỳ hạn nào: hiển thị "Chưa có báo cáo nào"

---


## UC155-160.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Lập mới Báo cáo tình hình giao đất, cho thuê đất và cho phép chuyển mục đích sử dụng đất đối với tổ chức kinh tế có vốn đầu tư nước ngoài (Mẫu A.IV.12)
- Chức năng cho phép UBND cấp tỉnh điền biểu mẫu có cấu trúc cố định (Fixed Grid). Bảng gồm các chỉ tiêu được định nghĩa trước (không thêm/xóa dòng). Người dùng nhập Tổng số dự án và Diện tích đất (ha) cho từng chỉ tiêu lá (leaf row). Các chỉ tiêu cha tự động tính tổng.

Phân quyền: UBND cấp tỉnh. Tham chiếu: CMR_02.

Truy cập chức năng: Màn danh sách báo cáo (UC155-160.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 155, 156

---

### 2. Mô tả giao diện

**HEADER (auto-fill)**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Đơn vị lập báo cáo | Label | Auto-fill từ profile tổ chức đăng nhập | | | Disabled. Tham chiếu: CMR_12. |
| 2 | Năm báo cáo | Yearpicker | Năm hiện tại | x | x | Validate: Số nguyên 4 chữ số, ≤ năm hiện tại. Tham chiếu: CMR_05, CMR_08. |
| 3 | Nơi nhận | Label | "Bộ Tài chính (Cục Đầu tư nước ngoài); Bộ Nông nghiệp và Môi trường" | | | Hiển thị cố định. Disabled. |

**BẢNG SỐ LIỆU (Fixed Grid)**

Cấu trúc bảng gồm 4 cột:
- Cột 1: STT (Label)
- Cột 2: Chỉ tiêu (Label — tên dòng, cố định)
- Cột 3: Tổng số dự án
- Cột 4: Diện tích đất (ha)

Mô tả giao diện:

| STT | Chỉ tiêu | Cột 3 – Tổng số dự án | Cột 4 – Diện tích đất (ha) |
| --- | --- | --- | --- |
| **I** | **Giao đất không thu tiền sử dụng đất** | Number. Nhập tay. Số nguyên ≥ 0. Bắt buộc. Tham chiếu: CMR_05, CMR_08. | Number. Nhập tay. Số thực ≥ 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Bắt buộc. Tham chiếu: CMR_05, CMR_08. |
| **II** | **Giao đất có thu tiền sử dụng đất** | Label. Auto-calculated = II.1 + II.2. Disabled. | Label. Auto-calculated. Disabled. |
| II.1 | Đất nông nghiệp | Label. Auto-calculated = II.1a + II.1b. Disabled. | Label. Auto-calculated. Disabled. |
| II.1a | — Thông qua đấu giá, đấu thầu | Number. Nhập tay. Số nguyên ≥ 0. Bắt buộc. | Number. Nhập tay. Số thực ≥ 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Bắt buộc. |
| II.1b | — Không qua đấu giá, đấu thầu | Number. Nhập tay. Số nguyên ≥ 0. Bắt buộc. | Number. Nhập tay. Số thực ≥ 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Bắt buộc. |
| II.2 | Đất phi nông nghiệp | Label. Auto-calculated = II.2a + II.2b. Disabled. | Label. Auto-calculated. Disabled. |
| II.2a | — Thông qua đấu giá, đấu thầu | Number. Nhập tay. Số nguyên ≥ 0. Bắt buộc. | Number. Nhập tay. Số thực ≥ 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Bắt buộc. |
| II.2b | — Không qua đấu giá, đấu thầu | Number. Nhập tay. Số nguyên ≥ 0. Bắt buộc. | Number. Nhập tay. Số thực ≥ 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Bắt buộc. |
| **III** | **Cho thuê đất** | Label. Auto-calculated = III.1 + III.2. Disabled. | Label. Auto-calculated. Disabled. |
| III.1 | Đất nông nghiệp | Label. Auto-calculated = III.1a + III.1b. Disabled. | Label. Auto-calculated. Disabled. |
| III.1a | — Thông qua đấu giá, đấu thầu | Number. Nhập tay. Số nguyên ≥ 0. Bắt buộc. | Number. Nhập tay. Số thực ≥ 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Bắt buộc. |
| III.1b | — Không qua đấu giá, đấu thầu | Number. Nhập tay. Số nguyên ≥ 0. Bắt buộc. | Number. Nhập tay. Số thực ≥ 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Bắt buộc. |
| III.2 | Đất phi nông nghiệp | Label. Auto-calculated = III.2a + III.2b. Disabled. | Label. Auto-calculated. Disabled. |
| III.2a | — Thông qua đấu giá, đấu thầu | Number. Nhập tay. Số nguyên ≥ 0. Bắt buộc. | Number. Nhập tay. Số thực ≥ 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Bắt buộc. |
| III.2b | — Không qua đấu giá, đấu thầu | Number. Nhập tay. Số nguyên ≥ 0. Bắt buộc. | Number. Nhập tay. Số thực ≥ 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Bắt buộc. |
| **IV** | **Cho phép chuyển mục đích sử dụng đất** | Number. Nhập tay. Số nguyên ≥ 0. Bắt buộc. | Number. Nhập tay. Số thực ≥ 0. Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự). Bắt buộc. |
| **Tổng** | **Tổng cộng** | Label. Auto-calculated = I + II + III + IV. Disabled. | Label. Auto-calculated = I + II + III + IV. Disabled. |

**CÁC BUTTON**

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
| --- | --- | --- | --- | --- | --- |
| B1 | Hủy | Button | Luôn Enabled | UBND cấp tỉnh | Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]"). |
| B2 | Xem trước | Button | Luôn Enabled | UBND cấp tỉnh | Mở popup PDF Preview báo cáo (không rời màn Lập). Tham chiếu: CF_07.1. |
| B3 | Lưu nháp | Button | Luôn Enabled | UBND cấp tỉnh | Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]"). |
| B4 | Nộp báo cáo | Button | Luôn Enabled | UBND cấp tỉnh | Bắt buộc nhập đầy đủ các trường "Bắt buộc". Tham chiếu: CF_01. |
---

### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu: CF_01 (Lập báo cáo), CF_04 (Xuất báo cáo Excel), CF_05 (In). Điều hướng Tab giữa các trường nhập liệu: Tham chiếu: CMR_18.

**Xử lý đặc thù biểu mẫu A.IV.12:**

- Khởi tạo màn hình: Header tự động fill Đơn vị lập báo cáo từ profile tổ chức đang đăng nhập. Trường "Nơi nhận" hiển thị cố định 2 cơ quan. Tất cả ô nhập liệu ban đầu là Null.
- Cấu trúc dòng cố định: Hệ thống hiển thị sẵn toàn bộ chỉ tiêu (I, II, III, IV và các chỉ tiêu con). Người dùng không thêm/xóa dòng.
- Auto-calculate (Cascading Sum): Các dòng cha (II, II.1, II.2, III, III.1, III.2, Tổng cộng) tự động cập nhật ngay khi giá trị bất kỳ dòng lá thay đổi. Quy tắc:
  - `II.1 = II.1a + II.1b`
  - `II.2 = II.2a + II.2b`
  - `II = II.1 + II.2`
  - `III.1 = III.1a + III.1b`
  - `III.2 = III.2a + III.2b`
  - `III = III.1 + III.2`
  - `Tổng = I + II + III + IV`
- Validate khi Nộp: Tất cả 10 ô nhập liệu lá (I, II.1a, II.1b, II.2a, II.2b, III.1a, III.1b, III.2a, III.2b, IV) ở cả 2 cột (Tổng số dự án và Diện tích đất) phải có giá trị hợp lệ. Tham chiếu: CMR_05, CMR_06.
- Xuất báo cáo: File xuất là định dạng Excel (không phải Docx). Tham chiếu: CF_04.

---


## UC155-160.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ – Xem chi tiết, Xem vòng đời, In, Xuất báo cáo, Nộp, Chỉnh sửa

Phân quyền: UBND cấp tỉnh. Tham chiếu: CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC155-160.1) → Cột Hành động → Chọn tác vụ tương ứng

Chức năng đáp ứng usecase số: 157, 158, 159, 160

---

### 2. Mô tả giao diện

**Các Button theo Action Mapping:**

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Lưu nháp và Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_09. Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |
| 2 | Chỉnh sửa | Button | Chỉ khi Lưu nháp hoặc Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Tất cả người dùng | Mở màn hình xem toàn bộ bảng (Disabled). Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Tất cả người dùng | Mở popup Vòng đời. Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Tất cả người dùng | Kết xuất file Excel. Tham chiếu: CF_04. |
| 7 | Xóa | Button | Lưu nháp **VÀ** chưa từng nộp | Người tạo | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết: Tham chiếu: CF_07.
- Xem vòng đời: Tham chiếu: CF_06.
- In báo cáo: Tham chiếu: CF_05.
- Xuất báo cáo: Kết xuất ra file Excel. Tham chiếu: CF_04.
- Chỉnh sửa: Tham chiếu: CF_03.

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-06 | 1.0 → 1.1 | Bảng số liệu — Cột 3 (Tổng số dự án) | Số nguyên dương, tối đa 2 chữ số thập phân | Số nguyên ≥ 0 | Sửa mâu thuẫn data type: "số nguyên" không có thập phân. Đồng bộ với UC149-154, UC257-262 |
| 2026-05-06 | 1.0 → 1.1 | Validate khi Nộp — số ô lá | 8 ô (thiếu III.2a) | 10 ô (I, II.1a, II.1b, II.2a, II.2b, III.1a, III.1b, III.2a, III.2b, IV) | Sửa typo: đếm đúng từ bảng Fixed Grid = 10 dòng lá |
| 2026-05-06 | 1.0 → 1.1 | Nút [Nhập từ file] — tham chiếu CF_02 | (Không có) | Tham chiếu: CF_02 Case 2 (không có Phạm vi dữ liệu nguồn input) | Làm rõ luồng Nhập từ file áp dụng cho biểu mẫu này |
| 2026-05-06 | 1.0 → 1.1 | Xử lý danh sách — hành vi kỳ hết hạn | (Không có) | Bản ghi Lưu nháp/YCCS vẫn có thể Sửa/Nộp/Xóa khi kỳ "Qua kỳ báo cáo" (CMR_03 + CMR_04) | Làm rõ edge case: CMR_04 chỉ ẩn nút Lập mới/Nhập từ file |
| 2026-05-06 | 1.0 → 1.1 | Mapping UC → chức năng | (Không có) | Bổ sung bảng mapping UC155→UC160 chi tiết | Tăng traceability cho QA test design |
| 2026-05-07 | 1.1 → 1.2 | Bảng thuộc tính — Phạm vi dữ liệu đầu vào | (Không có) | Không có phạm vi | Bổ sung metadata phân loại phạm vi báo cáo |
| 2026-05-07 | 1.1 → 1.2 | Định dạng bảng Markdown | Dòng phân cách không khớp số cột | Sửa dòng phân cách khớp đúng số cột tiêu đề | Chuẩn hóa định dạng Markdown |
| 2026-05-11 | 1.0→1.1 | Quy tắc sinh mã báo cáo | `DTNN_A4_12_[ID]` | `FDI_AIV12_[ID]` | Chuẩn hóa prefix và mã theo appendices.md v2.0 (INS-10) |
| 2026-05-11 | +1 | Điều kiện hiển thị nút | `Luôn hiển thị` | `Tất cả trạng thái` | Chuẩn hóa điều kiện (INS-07) |
| 2026-05-11 | +1 | Kiểu field Năm báo cáo | `Number` | `Yearpicker` | Đồng nhất kiểu field (INS-04) |
| 2026-05-11 | +1 | Nút [Nộp] điều kiện hiển thị | `Chỉ khi Lưu nháp` | `Lưu nháp và Yêu cầu chỉnh sửa` | Bổ sung trạng thái còn thiếu (INS-02) |
| 2026-05-11 | +1 | Dòng phân cách Markdown | Sai số cột | 6 cột đúng | Sửa lỗi Markdown (INS-05) |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (2 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-18 | 1.2 → 1.3 | Bảng thuộc tính — Loại quy trình | (Không có) | Quy trình 3 bước, CMCĐT_BCTK_09 | Bổ sung metadata loại quy trình |
| 2026-05-22 | CMR Alignment | Numeric — Diện tích đất (ha) | tối đa 2 chữ số thập phân | Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | Chuẩn hóa precision theo CMR (10 ô lá cột Diện tích) |
| 2026-05-22 | CMR Alignment | Buttons B1–B4 — Điều kiện hiển thị | Luôn | Luôn Enabled | Bổ sung "Enabled" cho submit/save buttons |
| 2026-05-22 | CMR Alignment | Tab Navigation | (Không có) | Tham chiếu: CMR_18 | Bổ sung tham chiếu điều hướng Tab giữa các trường nhập liệu |
| 2026-05-22 | CMR Alignment | Trailing dot — CMR_07 references | CMR_07. | CMR_07 | Xóa dấu chấm thừa sau tham chiếu CMR |
| 2026-05-22 | CMR Alignment | Trailing dot — CMR_09 reference (dòng 9) | CMR_09. | CMR_09 | Xóa dấu chấm thừa sau tham chiếu CMR |
| 2026-05-22 | CMR Alignment | Trailing dot — Placeholder search bar | "Tìm kiếm nhanh theo mã báo cáo". | "Tìm kiếm nhanh theo mã báo cáo" | Xóa dấu chấm cuối message |
| 2026-05-22 | CMR Alignment | Trailing dot — Empty state message | "Chưa có báo cáo nào." | "Chưa có báo cáo nào" | Xóa dấu chấm cuối validation/empty-state message |
