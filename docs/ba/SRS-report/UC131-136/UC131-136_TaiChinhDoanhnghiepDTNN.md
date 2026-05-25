# UC131-136: Báo cáo tổng hợp tình hình tài chính và nộp ngân sách của tổ chức kinh tế có vốn đầu tư nước ngoài năm ...... (theo doanh nghiệp) — Mẫu A.IV.9b

| Thuộc tính                          | Giá trị                                        |
| ------------------------------------- | ------------------------------------------------ |
| **BA phụ trách**              | yen.le2                                          |
| **Phân hệ**                   | Quản lý đầu tư nước ngoài vào Việt Nam |
| **Mẫu biểu**                  | Mẫu A.IV.9b                                     |
| **Loại báo cáo**             | Định kỳ năm                                  |
| **Phạm vi báo cáo**          | Không có phạm vi                              |
| **Hình thức nộp**            | Báo cáo đơn lẻ (Single report form)         |
| **Cơ quan nhận**              | Cục Đầu tư nước ngoài, Vụ Ngân sách Nhà nước (Bộ Tài chính) |
| **Đối tượng lập**          | Cục Thuế / Vụ Tài chính (Bộ Tài chính)      |
| **Giao diện**                  | Admin site                                       |
| **Ngày tạo**                  | 2026-04-24                                       |
| **Phiên bản**                 | 1.8                                              |
| **Quy tắc sinh mã báo cáo** | FDI_AIV9B_[ID] |
| **Loại quy trình** | Quy trình 3 bước, CMCĐT_BCTK_09 |

> **Lưu ý kiến trúc:** Mẫu A.IV.9b là báo cáo chi tiết tài chính và nộp ngân sách theo từng doanh nghiệp FDI. **Mẫu 9a (UC125-130) và Mẫu 9b là hai báo cáo hoàn toàn độc lập — 9a lấy dữ liệu từ API TMS, 9b lấy từ API Cục Thuế. Không tổng hợp qua lại.**
> - **Exception CMR_12:** Mẫu A.IV.9b áp dụng Editable sau API fill thay vì Disabled, theo yêu cầu nghiệp vụ — user chịu trách nhiệm cuối cùng về tính chính xác dữ liệu.

---

## UC131-136.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo tổng hợp tình hình tài chính và nộp ngân sách TCKT có vốn ĐTNN theo doanh nghiệp (Mẫu A.IV.9b)
- Chức năng cho phép Cục Thuế / Bộ Tài chính truy cập danh sách báo cáo định kỳ năm, được nhóm theo từng Kỳ hạn báo cáo. Mỗi đơn vị chỉ thấy báo cáo do đơn vị mình lập. Mục tiêu: Cung cấp dữ liệu tài chính chi tiết từng doanh nghiệp FDI để làm nguồn tổng hợp cho Mẫu 9a.
- Out of scope: Không cho phép nộp báo cáo trễ hạn. Việc duyệt báo cáo được thực hiện ở một UC riêng biệt.

Phân quyền: Chỉ người dùng có tổ chức thuộc Cục Thuế / Vụ Tài chính (Bộ Tài chính) mới có quyền truy cập. Mỗi đơn vị chỉ thấy và thao tác trên báo cáo do đơn vị mình lập. Không áp dụng CMR_01/CMR_02 (dành cho NĐT/TCKT).

**Tiền điều kiện (Preconditions):**

- Tài khoản người dùng có quyền lập/xem báo cáo thuộc đơn vị Cục Thuế / Vụ Tài chính (Bộ Tài chính).
- Kỳ báo cáo đang ở trạng thái "Trong thời hạn".

**Hậu điều kiện (Postconditions):**

- Sau khi Nộp báo cáo thành công, hệ thống gửi thông báo (Notification) cho đơn vị cấp trên (Cục ĐTNN).
- Các thao tác Thêm, Sửa, Xóa đều được hệ thống ghi nhận lịch sử (Audit log).
- **Phân quyền Owner:** Chỉ người tạo báo cáo mới được thực hiện Sửa / Nộp / Xóa. Người dùng khác cùng đơn vị chỉ có quyền Xem chi tiết, Xem vòng đời, In, Xuất báo cáo.
- **Kỳ chuyển "Qua kỳ":** Báo cáo ở trạng thái Lưu nháp bị khóa — không cho sửa/nộp, chỉ cho phép Xem và Xóa.

Truy cập chức năng: Phân hệ Báo cáo → Quản lý ĐTNN vào VN → Báo cáo tài chính và nộp ngân sách ĐTNN theo doanh nghiệp (Mẫu A.IV.9b)

Chức năng đáp ứng usecase số: 131, 132, 133, 134, 135, 136

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện: **Periodic-single** — Báo cáo có kỳ hạn năm, gửi lẻ từng đơn vị.

| #                                                     | Tên trường          | Kiểu trường              | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả                                                                                                                                                                                          |
| ----------------------------------------------------- | ---------------------- | --------------------------- | --------------------- | ------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Khung Điều kiện Lọc & Tìm kiếm**        |                        |                             |                       |              |            |                                                                                                                                                                                                  |
| 1                                                     | Năm                   | Yearpicker                  | Năm hiện tại       | x            |            | Người dùng chọn năm; hệ thống lọc và nhóm danh sách theo năm. Kết quả hiển thị ngay lập tức. Tham chiếu: CMR_07.                                                              |
| 2                                                     | Trạng thái kỳ       | Multiple-selection Dropdown | Tất cả               | x            |            | Lọc theo trạng thái kỳ hạn: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Kết quả hiển thị ngay. Tham chiếu: CMR_04, CMR_07, CMR_16.                                                 |
| 3                                                     | Trạng thái báo cáo | Multiple-selection Dropdown | Tất cả               | x            |            | Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07, CMR_16. |
| 4                                                     | Mã báo cáo          | Search bar                  | Null                  | x            |            | Tìm theo mã báo cáo. Kết quả hiển thị ngay khi nhập. Nếu không tìm thấy: hiển thị "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo".     |
| **Khung Danh sách Kỳ hạn**                   |                        |                             |                       |              |            |                                                                                                                                                                                                  |
| 5                                                     | Kỳ hạn báo cáo     | Label                       | Null                  |              |            | Hiển thị tên kỳ hạn (VD: "Năm 2026"). Mặc định collapse; click để expand. Tham chiếu: CMR_08.                                                                                        |
| 6                                                     | Trạng thái kỳ       | Label                       | Null                  |              |            | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04.                                                                                                                     |
| 7                                                     | Lập báo cáo         | Button                      | Null                  |              |            | Hiển thị trong header mỗi kỳ. Chỉ hiển thị khi Trong thời hạn. Ẩn khi Chưa tới hạn hoặc đã Qua kỳ báo cáo. Tham chiếu: CF_01.                                                |
| 8                                                     | Nhập từ file                 | Button                      | Null                  |              |            | Hiển thị trong header mỗi kỳ. Chỉ hiển thị khi Trong thời hạn. Ẩn khi Chưa tới hạn hoặc đã Qua kỳ báo cáo.                                                                    |
| **Khung Danh sách Báo cáo** (trong mỗi kỳ) |                        |                             |                       |              |            |                                                                                                                                                                                                  |
| 9                                                     | Mã báo cáo          | Label                       | Null                  |              |            | Mã do hệ thống sinh. Tham chiếu: CMR_09.                                                                                                                                                     |
| 10                                                    | Ngày cập nhật  | Label                       | Null                  |              |            | Định dạng: dd/MM/yyyy HH:mm.                                                                                                                                                                  |
| 11                                                    | Trạng thái báo cáo | Label                       | Null                  |              |            | Tham chiếu: CMR_03.                                                                                                                                                                             |
| 12                                                    | Hành động           | Button group                | Null                  |              |            | Chi tiết tham chiếu: UC131-136.3.                                                                                                                                                              |

---

### 3. Mô tả các xử lý của chức năng

- Hệ thống nhóm danh sách theo Kỳ hạn báo cáo (năm), mặc định collapse. Người dùng click để expand từng kỳ.
- Sắp xếp kỳ hạn giảm dần (mới nhất lên đầu). Báo cáo trong mỗi kỳ sắp xếp mới → cũ.
- Các nút [Lập báo cáo] và [Nhập từ file] bị ẩn với kỳ chưa bắt đầu (Chưa tới hạn) và kỳ đã qua (Qua kỳ báo cáo). Tham chiếu: CF_01.
- Mỗi đơn vị chỉ thấy báo cáo của đơn vị mình.
- Hiển thị tối đa 10 bản ghi trong mỗi kỳ hạn. Nếu vượt quá 10 bản ghi, hệ thống kích hoạt thanh cuộn dọc (Scroll) bên trong riêng kỳ hạn đó. Tham chiếu: CS_01 Mục 4.

---

## UC131-136.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Lập mới báo cáo tổng hợp tình hình tài chính và nộp ngân sách TCKT có vốn ĐTNN theo doanh nghiệp (Mẫu A.IV.9b)
- Chức năng cho phép Cục Thuế / Bộ Tài chính nhập liệu dữ liệu tài chính và nộp ngân sách theo từng doanh nghiệp FDI. Bảng dữ liệu hỗ trợ 2 chế độ:
  - **Mode A (Thủ công)** — Kích hoạt khi API Cục Thuế KHÔNG khả dụng (auto-detect). User nhập tay. Khi nhập MST hợp lệ → gọi API CSDL Đăng ký KD auto-fill C3, C4, C5, C6.
  - **Mode B (API Cục Thuế)** — Kích hoạt khi API Cục Thuế khả dụng (auto-detect). Hệ thống tự auto-fill toàn bộ dòng. **Tất cả dữ liệu vẫn Editable** — user có thể hiệu chỉnh sau khi API điền. User chịu trách nhiệm cuối cùng về tính chính xác.
  - **Cơ chế chuyển đổi:** Auto-detect dựa trên kết nối API, **không có toggle/switch trên UI**.
  - Cột Lợi nhuận sau thuế cho phép nhập số âm (doanh nghiệp thua lỗ). Hiển thị bình thường với dấu trừ (plain minus sign, không đổi màu).

Phân quyền: Chỉ người dùng có tổ chức thuộc Cục Thuế / Vụ Tài chính (Bộ Tài chính) mới có quyền lập báo cáo. Mỗi đơn vị chỉ thấy và thao tác trên báo cáo do đơn vị mình lập. Không áp dụng CMR_01/CMR_02.

Truy cập chức năng: Màn danh sách báo cáo (UC131-136.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 131, 132

---

### 2. Mô tả giao diện

| #                                                     | Tên trường                                  | Kiểu trường           | Giá trị mặc định  | Được sửa | Bắt buộc | Ghi chú                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------------------------------- | ---------------------------------------------- | ------------------------ | ---------------------- | ------------ | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PHẦN HEADER**                                |                                                |                          |                        |              |            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 1                                                     | Năm báo cáo                                 | Yearpicker | Năm hiện tại        |             | x          | Hiển thị năm báo cáo đã chọn từ màn danh sách. **Disabled** — không cho sửa. Năm này là context xuyên suốt: API Cục Thuế truy vấn theo năm, tiêu đề báo cáo hiển thị năm, xuất file đặt tên theo năm. Tham chiếu: CS_01 Mục 2.                                                                                                                                                                                                                                                                                                      |
| **BẢNG DỮ LIỆU — DANH SÁCH DOANH NGHIỆP (Dynamic Table — max 500 dòng)** |                                                |                          |                        |              |            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| C1                                                    | STT                                            | Integer                  | Auto-fill              |              |            | Hệ thống tự động điền số thứ tự tăng dần từ 1. Cập nhật lại (re-index) sau mỗi lần thêm/xóa dòng. Read-only.                                                                                                                                                                                                                                                                                                                                                                  |
| C2                                                    | Mã số thuế                                  | Text                     | Null                   | x | x          | Validate on-blur + **debounce 500ms**. Validate định dạng: 10 hoặc 13 chữ số. Validate trùng on-blur: nếu có → lỗi inline "Mã số thuế này đã được nhập ở dòng [STT]". MST hợp lệ → gọi API CSDL Đăng ký KD auto-fill C3, C4, C5, C6. **Mode B:** Auto-fill, vẫn **Editable**. Placeholder: "Nhập mã số thuế". Tham chiếu: CMR_05, CMR_06. |
| C3                                                    | Tên doanh nghiệp                             | Text                     | Từ CSDL Đăng ký KD | x | x          | Auto-fill nếu tìm thấy từ CSDL Đăng ký KD; không tìm thấy → Enabled nhập tay. **Mode B:** Auto-fill, vẫn **Editable**. Max 255 ký tự. Placeholder: "Nhập tên doanh nghiệp". Tham chiếu: CMR_06, CMR_12. |
| C4                                                    | Ngày cấp                                     | Date                     | Từ CSDL Đăng ký KD | x | x          | Auto-fill hoặc Enabled. **Mode B:** Auto-fill, vẫn **Editable**. Validate ≤ ngày hiện tại. dd/MM/yyyy. Tham chiếu: CMR_12. |
| C5                                                    | Địa chỉ                                     | Text                     | Từ CSDL Đăng ký KD | x | x          | Auto-fill hoặc Enabled. **Mode B:** Auto-fill, vẫn **Editable**. Max 255 ký tự. Placeholder: "Nhập địa chỉ". Tham chiếu: CMR_06, CMR_12. |
| C6                                                    | Tỉnh/Thành phố                              | Dropdown                 | Từ CSDL Đăng ký KD | x | x          | Auto-fill hoặc Enabled (danh mục 34 tỉnh/TP theo danh mục hành chính sáp nhập mới). **Mode B:** Auto-fill, vẫn **Editable**. Tham chiếu: CMR_07, CMR_12. |
| C7                                                    | Doanh thu                        | Decimal                  | Null                   | x | x          | Tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân (tổng 21 ký tự bao gồm dấu `.`). Cho phép nhập số âm. **Mode B:** Auto-fill từ BCTC đã chốt, vẫn **Editable**. Placeholder: "Nhập doanh thu". Tham chiếu: CMR_05. |
| C8                                                    | Lợi nhuận sau thuế             | Decimal                  | Null                   | x | x          | Tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân (tổng 21 ký tự bao gồm dấu `.`). Cho phép nhập số âm (DN thua lỗ). Hiển thị dấu trừ bình thường (plain minus sign, không đổi màu). Cross-validate: C7 > C8. **Mode B:** Auto-fill, vẫn **Editable**. Placeholder: "Nhập lợi nhuận sau thuế". Tham chiếu: CMR_05. |
| C9                                                    | Thuế và các khoản phải nộp ngân sách nhà nước | Decimal                | Null                   | x | x          | Tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân (tổng 21 ký tự bao gồm dấu `.`). Cho phép nhập số âm. **Mode B:** Auto-fill, vẫn **Editable**. Placeholder: "Nhập thuế và các khoản phải nộp". Tham chiếu: CMR_05. |
| **DÒNG TỔNG CỘNG**                           |                                                |                          |                        |              |            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| T1                                                    | Tổng cộng — Doanh thu (triệu VND)          | Tính toán              | Auto                   |              |            | Read-only. SUM(C7). Tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân. Cập nhật real-time.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| T2                                                    | Tổng cộng — Lợi nhuận sau thuế (triệu VND) | Tính toán            | Auto                   |              |            | Read-only. SUM(C8). Có thể hiển thị số âm. Hiển thị dấu trừ bình thường (plain minus sign, không đổi màu). Tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân. Cập nhật real-time.                                                                                                                                                                                                                                                                                               |
| T3                                                    | Tổng cộng — Thuế và khoản nộp NSNN (triệu VND) | Tính toán          | Auto                   |              |            | Read-only. SUM(C9). Tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân. Cập nhật real-time.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **FOOTER**                                      |                                                |                          |                        |              |            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| F1                                                    | Nơi lập báo cáo                            | Text                     | Auto-fill              |              |            | Hệ thống tự động điền tên Tỉnh/Thành phố theo địa chỉ trụ sở của Cục Thuế đang đăng nhập. Disabled. Tham chiếu: CMR_12.                                                                                                                                                                                                                                                                                                                                         |
| F2                                                    | Ngày, tháng, năm                            | Date                     | Auto-fill              |              |            | Hệ thống tự động điền ngày hiện tại (Current System Date). Cập nhật real-time. Disabled. Tham chiếu: CMR_12.                                                                                                                                                                                                                                                                                                                                                               |
| **CÁC BUTTON THAO TÁC BẢNG**                 |                                                |                          |                        |              |            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| B1                                                    | Thêm dòng                                    | Button                   |                        |              |            | Thêm 1 dòng mới vào cuối bảng. STT tự động tăng. Max 500 dòng; vượt → Toast T16 *"Vượt quá số dòng tối đa cho phép (500)"*.                                                                                                                                                                                                                                                                                                                                                                  |
| B2                                                    | Xóa dòng                                     | Icon Button (mỗi dòng) |                        |              |            | Chỉ hiển thị khi bảng có từ 2 dòng trở lên (khi chỉ còn 1 dòng → ẩn). Nhấn → xóa dòng ngay lập tức, không hiển thị popup xác nhận. STT re-index. Tham chiếu: CMR_15.                                                                                                                                                                                                                                 |
| **CÁC BUTTON HÀNH ĐỘNG CHÍNH**             |                                                |                          |                        |              |            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| B3                                                    | Lưu nháp                                     | Button                   |                        |              |            | **Luôn Enabled.** Validate trước khi lưu: ít nhất 1 dòng phải có dữ liệu (CF_01 Case 2 — báo cáo không có "Phạm vi dữ liệu nguồn input"). Nếu 0 dòng hoặc tất cả dòng trống → Toast T15 *"Vui lòng nhập ít nhất 1 dòng dữ liệu"*, chặn lưu. Lưu toàn bộ dữ liệu ở trạng thái Lưu nháp. Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]").                                                                                                                                                                                                                                                                                                                                                                             |
| B4                                                    | Xem trước                                    | Button                   |                        |              |            | Mở popup PDF Preview. Disabled khi chưa Lưu nháp lần nào; Enabled sau khi bản ghi đã tồn tại trong DB. Tham chiếu: CF_01 (mục "Xử lý nút [Xem trước]").                                                                                                                                                                                                                                                                                                                                                                             |
| B5                                                    | Nộp báo cáo                                 | Button                   |                        |              |            | **Luôn Enabled.** Validate toàn bộ trường bắt buộc và ràng buộc logic trước khi nộp. **Empty table:** 0 dòng → Toast T15 *"Vui lòng nhập ít nhất 1 dòng dữ liệu"*, chặn nộp. Lỗi validate trong bảng hiển thị dạng viền đỏ + tooltip (theo CMR_05/06/07 eForm Grid rule). Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]").                                                                                                                                                                                                                                                                                                                                               |
| B6                                                    | Hủy                                           | Button                   |                        |              |            | **Luôn Enabled.** Quay về màn hình Danh sách. Popup xác nhận nếu có dữ liệu chưa lưu (dirty form — thêm/xóa/sửa bất kỳ dòng nào = form dirty). Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]"), CMR_14.                                                                                                                                                                                                                                                                                                                                                        |

---

### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu CF_01 (Lập báo cáo). Tham chiếu CMR_18: Tab key điều hướng giữa các field theo thứ tự logic (C2 → C3 → C4 → C5 → C6 → C7 → C8 → C9 → dòng tiếp theo). Shift+Tab di chuyển ngược. Tab ở field cuối cùng của dòng cuối → focus đến nút [Thêm dòng] hoặc [Lưu nháp]. Lỗi validate trong bảng hiển thị dạng viền đỏ + tooltip (theo CMR_05/06/07 eForm Grid rule).

**Xử lý đặc thù Mẫu A.IV.9b:**

A. Cơ chế chuyển đổi Mode A/B (Auto-detect):
- Khi mở form [Lập báo cáo] → hệ thống gọi health-check API Cục Thuế.
- API OK → **Mode B** kích hoạt (auto-fill toàn bộ dòng FDI).
- API Fail/Timeout → **Mode A** kích hoạt + Toast T05. Tham chiếu: CMR_12. Enable toàn bộ form.
- **Không có toggle/switch trên UI**.

B. Mode A — Nhập tay (Không có API Cục Thuế):
- Người dùng nhấn [Thêm dòng] để thêm từng doanh nghiệp.
- Nhập MST vào C2; hệ thống validate định dạng (10 hoặc 13 số) **on-blur + debounce 500ms** (sửa MST trong 500ms → cancel API call cũ).
- Validate trùng trong bảng on-blur.
- Nếu MST hợp lệ → hệ thống gọi API CSDL Đăng ký KD: tìm thấy → auto-fill C3, C4, C5, C6; không tìm thấy → C3, C4, C5, C6 Enabled cho nhập tay. Tham chiếu: CMR_12.
- Người dùng nhập C7 (Doanh thu, tối đa 15 chữ số phần nguyên + 5dp, cho phép âm), C8 (Lợi nhuận — cho phép âm, tối đa 15 chữ số phần nguyên + 5dp), C9 (Thuế, tối đa 15 chữ số phần nguyên + 5dp, cho phép âm).
- Cross-validate: C7 > C8 (Warning only).
- Dòng Tổng T1, T2, T3 cập nhật real-time.

C. Mode B — API Cục Thuế (BCTC đã chốt):
- Hệ thống rà quét toàn bộ doanh nghiệp có MST thuộc diện FDI từ hệ thống Cục Thuế.
- Tự động điền toàn bộ C2–C9 cho từng dòng.
- **Override CMR_12:** Tất cả dữ liệu vẫn **Editable** sau khi API điền — user có thể hiệu chỉnh giá trị. User chịu trách nhiệm cuối cùng về tính chính xác. *(Lý do override: dữ liệu tài chính cần được cán bộ Cục Thuế xác nhận/hiệu chỉnh trước khi nộp.)*
- **User vẫn được thêm dòng bổ sung** (DN FDI chưa có trong API) qua [Thêm dòng].
- Dòng Tổng T1, T2, T3 SUM toàn bộ dòng.

E. Cross-validation C7/C8 (Warning only):
- Nếu C8 ≥ C7 (Lợi nhuận ≥ Doanh thu) → Warning (yellow banner): "Lợi nhuận [Dòng STT] lớn hơn hoặc bằng Doanh thu. Vui lòng kiểm tra" Không chặn nộp.
- Placeholder C7: "Nhập doanh thu (triệu VND)". C8: "Nhập lợi nhuận (triệu VND, có thể âm)". C9: "Nhập thuế và khoản nộp (triệu VND)".

F. Validate khi Nộp:
- Validate tất cả trường bắt buộc (C2-C9) trên toàn bộ dòng.
- C7, C8, C9: tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân (tổng 21 ký tự bao gồm dấu `.`), cho phép nhập số âm. Phần thập phân > 5 chữ số → block không cho nhập thêm. Phần nguyên > 15 chữ số → hiển thị lỗi inline.
- Cross-validate: C7 > C8 (Warning only, không chặn nộp).
- **Validate bảng không trống:** Nếu 0 dòng → Toast T15 *"Vui lòng nhập ít nhất 1 dòng dữ liệu"*, chặn nộp.
- Nếu vi phạm → lỗi inline viền đỏ + tooltip "Vui lòng nhập [tên trường]" hoặc "Giá trị không hợp lệ" tại ô vi phạm (theo CMR_05/06/07 eForm Grid rule). Dừng luồng, không nộp. Tham chiếu: CF_01.

G. Mẫu 9a và 9b độc lập:
- **Mẫu 9a (UC125-130) và Mẫu 9b (UC131-136) là hai báo cáo hoàn toàn độc lập.** Không tổng hợp qua lại. 9a lấy dữ liệu từ API TMS, 9b lấy từ API Cục Thuế.

H. Sort:
- Các cột hỗ trợ sort: C4 (Ngày cấp), C7 (Doanh thu), C8 (Lợi nhuận), C9 (Thuế).
- Icon sort hiển thị trên header các cột trên. Click icon → toggle: Ascending ↑ / Descending ↓.
- **Mặc định sort:** C8 (Lợi nhuận sau thuế) Descending (max → min).
- Dòng Tổng luôn ở cuối bảng, không tham gia sort.
- Dòng mới thêm vào cuối bảng, user tự sort lại nếu muốn.
- Sort persist khi Lưu nháp → mở lại giữ nguyên thứ tự. Sort thực hiện **server-side** (API trả về dữ liệu đã sort). Khi mở lại bản ghi (CF_03 Xem chi tiết / CF_07 Chỉnh sửa), hệ thống restore sort order đã lưu.
- Mode B: hệ thống auto-sort theo default sort (C8 Descending) trước khi render.

I. Nhập từ file (Import Excel):
- Cho phép người dùng upload file Excel (.xlsx) để nhập hàng loạt doanh nghiệp vào bảng.
- **Template:** Hệ thống cung cấp file mẫu (.xlsx) với cấu trúc cột: STT | Mã số thuế | Tên doanh nghiệp | Ngày cấp | Địa chỉ | Tỉnh/Thành phố | Doanh thu | Lợi nhuận sau thuế | Thuế và khoản nộp NSNN.
- **Validate file:** Chỉ chấp nhận .xlsx, max 5MB. Sai định dạng → Toast *"Vui lòng chọn file Excel (.xlsx)"*.
- **Validate dữ liệu từng dòng:**
  - MST: validate định dạng (10 hoặc 13 số) + validate trùng (trong file và trong bảng hiện tại).
  - Doanh thu, Lợi nhuận, Thuế: validate số, tối đa 5dp, cho phép âm.
  - Ngày cấp: validate format dd/MM/yyyy, ≤ ngày hiện tại.
- **Max 500 dòng tổng cộng** (dòng hiện có + dòng import). Vượt → Toast T16 *"Vượt quá số dòng tối đa cho phép (500)"*, chặn import.
- **Mapping:** Cột file → cột bảng theo thứ tự template. Dòng header bị bỏ qua.
- **Kết quả:** Dòng hợp lệ → thêm vào cuối bảng, STT re-index. Dòng lỗi → hiển thị danh sách lỗi (số dòng + lý do) trong popup, cho phép user sửa file và upload lại.
- **MST hợp lệ sau import:** Hệ thống gọi API CSDL Đăng ký KD cho từng MST mới → auto-fill C3-C6 nếu tìm thấy.
- Tham chiếu: CF_01.

- Xuất báo cáo: Kết xuất file Excel (.xlsx). Tham chiếu: CF_04.

---

## UC131-136.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ – Xem chi tiết, Xem vòng đời, In, Xuất báo cáo, Nộp, Chỉnh sửa
- Cho phép người dùng thực hiện tác vụ tương ứng trạng thái bản ghi.

Phân quyền: Kiểm soát theo trạng thái bản ghi. Tham chiếu: CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC131-136.1) → Cột Hành động

Chức năng đáp ứng usecase số: 133, 134, 135, 136

---

### 2. Mô tả giao diện

| # | Tên            | Kiểu  | Điều kiện hiển thị                         | Phân quyền           | Mô tả                                                                      |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp            | Button | Chỉ khi Lưu nháp hoặc Yêu cầu chỉnh sửa | Người tạo           | Tham chiếu: CF_09. Tham chiếu: CF_01.                                      |
| 2 | Chỉnh sửa     | Button | Chỉ khi Lưu nháp hoặc Yêu cầu chỉnh sửa | Người tạo           | Tham chiếu: CF_03.                                                          |
| 3 | Xem chi tiết   | Button | Tất cả trạng thái                           | Tất cả người dùng | Màn hình xem toàn trang, toàn bộ trường Disabled. Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái                           | Tất cả người dùng | Popup Audit Trail. Tham chiếu: CF_06.                                       |
| 5 | In              | Button | Tất cả trạng thái                           | Tất cả người dùng | Tham chiếu: CF_05.                                                          |
| 6 | Xuất báo cáo          | Button | Tất cả trạng thái                           | Tất cả người dùng | Kết xuất file Excel (.xlsx). Tham chiếu: CF_04.                                   |
| 7 | Xóa            | Button | Lưu nháp**VÀ** chưa từng nộp        | Người tạo           | Tham chiếu: CF_08.                                                          |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết: Tham chiếu: CF_07.
- Xem vòng đời: Tham chiếu: CF_06.
- In báo cáo: Tham chiếu: CF_05.
- Xuất báo cáo: Kết xuất ra file Excel (.xlsx). Tham chiếu: CF_04.
- Chỉnh sửa: Tham chiếu: CF_03.

---

## 3.4 Acceptance Criteria (Tiêu chí nghiệm thu)

- **AC1 Validate MST:** Nhập MST sai định dạng (không phải 10 hoặc 13 chữ số) → Báo lỗi. Trùng lặp → lỗi inline. Validate on-blur + debounce 500ms.
- **AC2 Auto-fill CSDL:** MST hợp lệ → gọi API CSDL Đăng ký KD, auto-fill C3-C6. Không tìm thấy → Enabled nhập tay.
- **AC3 Mode Detect:** Mở form → health-check API Cục Thuế. OK → Mode B. Fail → Mode A + Toast T05 (Tham chiếu: CMR_12).
- **AC4 API Cục Thuế (Mode B):** Auto-fill toàn bộ C2-C9. Tất cả dữ liệu vẫn Editable — user có thể hiệu chỉnh. User thêm dòng bổ sung.
- **AC5 Số âm:** C7, C8, C9 và T1, T2, T3 cho phép giá trị âm. Hiển thị plain minus sign, không đổi màu.
- **AC6 SUM Real-time:** T1, T2, T3 cập nhật ngay lập tức. Tối đa 5 chữ số thập phân.
- **AC7 Validate bắt buộc:** Nộp → kiểm tra C2-C9 bắt buộc. C7, C8, C9: tối đa 15 chữ số phần nguyên + 5dp, cho phép âm. Lỗi inline viền đỏ + tooltip.
- **AC8 Decimal precision:** C7, C8, C9: tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân (tổng 21 ký tự). Phần thập phân > 5 → block. Phần nguyên > 15 → lỗi inline.
- **AC9 Max dòng:** Bảng tối đa 500 dòng. Vượt → Toast.
- **AC10 Empty table:** 0 dòng khi Nộp → Toast, chặn nộp.
- **AC11 Cross-validation C7>C8:** C8 ≥ C7 → Warning only (yellow). Không chặn nộp.
- **AC12 Sort:** Icon sort hiển thị trên header C4, C7, C8, C9. Click → toggle Ascending/Descending. Mặc định: C8 Descending (max → min). Dòng Tổng luôn ở cuối. Sort persist khi Lưu nháp.
- **AC13 Concurrent Edit:** Last Write Wins — khi 2 user cùng lưu/nộp cùng lúc, thao tác sau ghi đè thao tác trước. Cả 2 thao tác được ghi vào Lifecycle Log. Tham chiếu: CF_06.
- **AC14 9a/9b Độc lập:** Mẫu 9a và 9b không tổng hợp qua lại.
- **AC15 Nộp thành công:** Tất cả validate pass → Click [Nộp báo cáo] → Trạng thái chuyển "Chờ duyệt", Notification gửi Cục ĐTNN, Audit log ghi nhận.

---

## 3.5 Non-Functional Requirements (Yêu cầu phi chức năng)

- **Performance:** Thời gian gọi API CSDL hoặc API Cục Thuế không quá 5 giây. Nếu quá 5s → Toast T05 (Tham chiếu: CMR_12) + Enable toàn bộ form cho nhập thủ công.
- **Security & Audit:** Chỉ Cục Thuế / Bộ Tài chính mới có quyền lập báo cáo. Chỉ người tạo (Owner) mới được sửa/nộp/xóa. Lưu vết Audit log cho mọi hành động Thêm/Sửa/Xóa/Nộp (Actor, Action, Timestamp). Tham chiếu: CF_06.
- **Concurrency:** Áp dụng Last Write Wins — khi 2 user cùng lưu/nộp cùng lúc, thao tác sau ghi đè thao tác trước. Cả 2 thao tác đều được ghi vào Lifecycle Log (Actor, Action, Timestamp). Tham chiếu: CF_06.
- **Maxlength:**

| Loại trường | Max Length | Áp dụng |
|---|---|---|
| Textbox | 255 ký tự | C3 (Tên DN), C5 (Địa chỉ) |
| Number (Decimal) | 21 ký tự (15 nguyên + 1 dấu `.` + 5 thập phân) | C7, C8, C9 |
| Search | 255 ký tự | Search bar (#4) |

---

## 4. Lịch sử cập nhật

| Ngày      | Phiên bản | Mục cập nhật           | Before       | After                                                       | Ghi chú                                                       |
| ---------- | ----------- | ------------------------- | ------------ | ----------------------------------------------------------- | -------------------------------------------------------------- |
| 2026-05-03 | N/A         | Trạng thái báo cáo    | Đã nộp    | Chờ duyệt / Đã tiếp nhận                              | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-07 | 1.0 → 1.1  | Thông tin chung          | (Không có) | Thêm Mục tiêu, Phạm vi, Tiền kiện, Hậu kiện.        | Chuẩn hóa tài liệu theo QC Audit.                          |
| 2026-05-07 | 1.0 → 1.1  | Tiêu chí nghiệm thu    | (Không có) | Bổ sung 6 AC chi tiết cho luồng báo cáo doanh nghiệp. | Chuẩn hóa tài liệu theo QC Audit.                          |
| 2026-05-07 | 1.0 → 1.1  | Yêu cầu phi chức năng | (Không có) | Bổ sung NFR (Performance, Security).                       | Chuẩn hóa tài liệu theo QC Audit.                          |
| 2026-05-07 | 1.1 → 1.2  | Phiên bản | 1.1 | 1.2 | Cập nhật sau QC Re-Audit Round 2. |
| 2026-05-07 | 1.2 | Kiến trúc | (Chung) | Bổ sung 9a/9b độc lập, Mode A/B auto-detect | QC Audit — làm rõ kiến trúc. |
| 2026-05-07 | 1.2 | Bảng dữ liệu | Dynamic Table | Dynamic Table — max 500 dòng. Dòng API Disabled, dòng manual Enabled. | QC Audit — API row locking + max rows. |
| 2026-05-07 | 1.2 | C2 MST | on-blur | on-blur + debounce 500ms, phân biệt Mode A/B | QC Audit — debounce. |
| 2026-05-07 | 1.2 | C7, C8, C9 | Decimal | Integer 0dp triệu VND, round half up. C8 plain minus sign. | QC Audit — decimal precision. |
| 2026-05-07 | 1.2 | B1 Thêm dòng | (Không có max) | Max 500 dòng + Toast | QC Audit — giới hạn dòng. |
| 2026-05-07 | 1.2 | B2 Xóa dòng | Mỗi dòng | Chỉ dòng manual, popup [Đồng ý]/[Hủy], STT re-index | QC Audit — API row protection. |
| 2026-05-07 | 1.2 | B4 Nộp | (Chung) | Bổ sung empty table rule | QC Audit — edge case. |
| 2026-05-07 | 1.2 | Xử lý đặc thù | A-C (cơ bản) | A-G (Mode detect, Mode A, Mode B, Partial, Cross-validate, Validate, 9a/9b) | QC Audit — viết lại. |
| 2026-05-07 | 1.2 | AC | AC1-AC6 | AC1-AC14 (thêm Mode detect, API rows, max, empty, decimal, cross-validate, concurrent, 9a/9b) | QC Audit — bổ sung AC. |
| 2026-05-07 | 1.2 | NFR | Performance, Security | Thêm Concurrency (optimistic locking) | QC Audit — concurrent edit. |
| 2026-05-07 | 1.2 | Hậu điều kiện | Tổng hợp cho 9a | Sửa: 9a/9b độc lập, xóa tham chiếu tổng hợp sai | QC Audit — sửa lỗi logic. |
| 2026-05-11 | 1.0→1.1 | Quy tắc sinh mã báo cáo | `DTNN_A4_9B_[ID]` | `FDI_AIV9B_[ID]` | Chuẩn hóa prefix và mã theo appendices.md v2.0 (INS-10) |
| 2026-05-11 | +1 | Kiểu field Năm báo cáo | `Number` | `Yearpicker` | Đồng nhất kiểu field (INS-04) |
| 2026-05-11 | +1 | Dòng phân cách bảng Markdown | Thiếu cột (1 chỗ) | Đủ số cột theo header | Chuẩn hóa separator (INS-05) |
| 2026-05-11 | 1.2 → 1.3 | Toast T05 (Mode A fallback) | Nội dung toast tự viết | Tham chiếu CMR_12 (T05 chuẩn) | QC Feedback — chuẩn hóa toast. |
| 2026-05-11 | 1.2 → 1.3 | Mục D (API Partial Failure) | Có mục + AC12 + toast warning | Xóa — không có cơ chế phát hiện data thiếu/đủ | QC Feedback — logic không khả thi. |
| 2026-05-11 | 1.2 → 1.3 | AC | AC1-AC14 (có AC12 API Partial) | AC1-AC13 (bỏ AC12, đánh lại số) | QC Feedback — đồng bộ với xóa mục D. |
| 2026-05-11 | 1.2 → 1.3 | AC12 + NFR Concurrency | Optimistic locking — conflict + refresh | Last Write Wins theo CMR_02 — thao tác sau ghi đè, cả 2 ghi Lifecycle Log | QC Feedback — đồng bộ CMR_02, CF_06. |
| 2026-05-14 | 1.3 → 1.4 | C2 MST | Validate 10 hoặc 14 chữ số | Validate 10 hoặc 13 chữ số | Client feedback — chuẩn hóa MST. |
| 2026-05-14 | 1.4 | C7, C8, C9 decimal | 0dp integer triệu VND, round half up | Tối đa 5 chữ số thập phân, cho phép nhập số âm | Client feedback — tăng precision + cho phép âm. |
| 2026-05-14 | 1.4 | Cross-validate | C8 > C7 hoặc C9 > C7 → Warning | C8 ≥ C7 → Warning only (C7 > C8) | Client feedback — chỉ validate C7 > C8. |
| 2026-05-14 | 1.4 | Dòng API | Disabled (không sửa, không xóa), có tag "API" | Editable (cho sửa, cho xóa), bỏ tag "API" | Client feedback — user chịu trách nhiệm cuối cùng. |
| 2026-05-14 | 1.4 | Sort | Không có | Icon sort C4, C7, C8, C9. Mặc định: C8 Descending (max → min) | Client feedback — thêm sort. |
| 2026-05-14 | 1.4 | Dropdown Tỉnh/TP | Danh mục 63 tỉnh/TP | Danh mục 34 tỉnh/TP theo sáp nhập mới | Client feedback — cập nhật danh mục hành chính. |
| 2026-05-14 | 1.4 | AC | AC1-AC13 | AC1-AC14 (thêm Sort, sửa MST 10/13, sửa decimal 5dp, sửa cross-validate) | Viết lại AC. |
| 2026-05-14 | 1.4 → 1.5 | Năm báo cáo (form Lập) | Editable, validate 4 chữ số | Disabled — hiển thị năm đã chọn từ màn danh sách | QC Review — năm đã chọn ở màn danh sách, không cần nhập lại. |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (2 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | STD-02 Required message trong AC logic | Truong bat buoc | Vui long nhap [ten truong] | Dong bo CMR v2.0 |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-21 | 1.5 → 1.6 | B2 Xóa dòng | Popup xác nhận [Đồng ý]/[Hủy], hiển thị trên tất cả dòng | Xóa ngay không popup, ẩn khi chỉ còn 1 dòng. Tham chiếu: CMR_15 | Đồng bộ CMR_15 (QC Audit v4) |
| 2026-05-21 | 1.5 → 1.6 | Mode B — Override CMR_12 | "Tất cả dữ liệu vẫn Editable" (không ghi override) | Ghi rõ "Override CMR_12" + lý do: user chịu trách nhiệm cuối cùng | QC Audit v4 — ghi nhận override |
| 2026-05-21 | 1.5 → 1.6 | Danh sách — Phân trang | Phân trang. Tham chiếu: CMR_10 | Scroll dọc khi >10 bản ghi/kỳ. Tham chiếu: CS_01 Mục 4 | Đồng bộ CS_01 (QC Audit v4) |
| 2026-05-21 | 1.5 → 1.6 | Filter default | Null | Tất cả (theo CMR_16) | Đồng bộ CMR_16 (QC Audit v4) |
| 2026-05-21 | 1.5 → 1.6 | Tham chiếu CMR sai | #1: CMR_05, C4: CMR_05, B2: CMR_06 | #1: CS_01 Mục 2, C4: bỏ CMR_05, B2: CMR_15 | Sửa tham chiếu (QC Audit v4) |
| 2026-05-21 | 1.5 → 1.6 | Thiếu nút [Xem trước] | Chỉ có B3-B5 (3 nút) | Thêm B4 [Xem trước], đánh lại B5 Nộp, B6 Hủy | Đồng bộ CF_01 (QC Audit v4) |
| 2026-05-21 | 1.5 → 1.6 | Phân quyền — CMR_02 | Tham chiếu CMR_02 | Bỏ CMR_02, ghi rõ: mỗi đơn vị chỉ thao tác trên báo cáo của mình | CMR_02 không áp dụng cho Admin site (QC Audit v4) |
| 2026-05-21 | 1.6 → 1.7 | Exception CMR_12 | Không ghi exception | Thêm "Exception: CMR_12" vào header tài liệu | QC Audit v5 — ghi nhận override CMR_12 ở cấp tài liệu |
| 2026-05-21 | 1.6 → 1.7 | Năm báo cáo context | Chỉ ghi "Disabled" | Thêm mô tả: năm là context xuyên suốt (API query, tiêu đề, tên file) | QC Audit v5 — GAP-06 |
| 2026-05-21 | 1.6 → 1.7 | Validate Lưu nháp | Không validate trước khi lưu | Thêm validate CF_01 Case 2: ít nhất 1 dòng có dữ liệu trước khi lưu nháp | QC Audit v5 — GAP-02 |
| 2026-05-21 | 1.6 → 1.7 | Nhập từ file | Không có section | Thêm section I. Nhập từ file: template, validate MST/format, max 500 dòng, mapping, error report | QC Audit v5 — GAP-03 |
| 2026-05-21 | 1.6 → 1.7 | Sort persistence | "Sort persist khi Lưu nháp" | Bổ sung: server-side, restore on CF_03/CF_07 | QC Audit v5 — GAP-04 |
| 2026-05-21 | 1.6 → 1.7 | Excel format | "Excel" | "Excel (.xlsx)" — chỉ rõ định dạng | QC Audit v5 — INC-01 |
| 2026-05-21 | 1.6 → 1.7 | AC13 + NFR Concurrency | Tham chiếu: CMR_02, CF_06 | Bỏ CMR_02, chỉ giữ CF_06 | QC Audit v5 — CMR_02 không áp dụng |
| 2026-05-21 | 1.6 → 1.7 | Cơ quan nhận / Đối tượng lập | Bộ Tài chính (chung) | Phân biệt: Vụ Tài chính (lập) vs Vụ NSNN (nhận) | QC Audit v5 — phân biệt 2 đơn vị BTC |
| 2026-05-22 | 1.7 → 1.8 | Phân quyền Owner | Không ghi rõ Owner-only | Bổ sung: chỉ người tạo sửa/nộp/xóa, user khác chỉ Xem | QC Audit v6 — Post-BA Answers |
| 2026-05-22 | 1.7 → 1.8 | Hành vi Qua kỳ | Không có | Lưu nháp khi Qua kỳ bị khóa — chỉ Xem và Xóa | QC Audit v6 — Post-BA Answers |
| 2026-05-22 | 1.7 → 1.8 | Numeric precision C7/C8/C9 | "Tối đa 5 chữ số thập phân" | "15 chữ số phần nguyên + 5 thập phân (tổng 21 ký tự)" | QC Audit v6 — CMR_05 (C05b) |
| 2026-05-22 | 1.7 → 1.8 | Placeholder C2-C9 | Không có (trừ C7/C8/C9 đã có) | Bổ sung placeholder "Nhập [tên trường]" cho C2, C3, C5 | QC Audit v6 — CMR_06 (A05) |
| 2026-05-22 | 1.7 → 1.8 | CMR_18 Tab Navigation | Không có | Bổ sung tham chiếu CMR_18 + thứ tự tab C2→C9→dòng tiếp | QC Audit v6 — FIX-03 |
| 2026-05-22 | 1.7 → 1.8 | Button state B3/B5/B6 | Không ghi rõ | "Luôn Enabled" — validate khi tap | QC Audit v6 — CMR Section I |
| 2026-05-22 | 1.7 → 1.8 | NFR Maxlength | Không có | Bổ sung bảng maxlength: Textbox=255, Number=21, Search=255 | QC Audit v6 — FIX-06 |
| 2026-05-22 | 1.7 → 1.8 | eForm Grid error display | "Lỗi inline màu đỏ" | "Viền đỏ + tooltip" theo CMR_05/06/07 eForm Grid rule | QC Audit v6 — GAP-05 |
| 2026-05-22 | 1.7 → 1.8 | AC15 | Không có | Bổ sung AC15 Nộp thành công (happy-path) | QC Audit v6 — Post-BA Answers |
| 2026-05-22 | 1.7 → 1.8 | Error message — bỏ dấu "." cuối | Có dấu "." cuối câu cuối | Bỏ dấu "." cuối câu cuối cùng (giữ "." giữa câu) | QC Audit v6 — FIX-04 |
