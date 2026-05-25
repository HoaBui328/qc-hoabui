# UC125-130: Báo cáo tổng hợp tình hình tài chính và nộp ngân sách của TCKT có vốn ĐTNN năm ...... (theo địa bàn tỉnh/thành phố) — Mẫu A.IV.9a

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | yen.le2 |
| **Phân hệ** | Quản lý đầu tư nước ngoài vào Việt Nam |
| **Mẫu biểu** | Mẫu A.IV.9a |
| **Loại báo cáo** | Định kỳ năm |
| **Phạm vi báo cáo**           | Không có phạm vi                                              |
| **Hình thức nộp** | Báo cáo đơn lẻ (Single report form) |
| **Cơ quan nhận** | Cục Đầu tư nước ngoài, Vụ Ngân sách Nhà nước (Bộ Tài chính) |
| **Đối tượng lập** | Cục Thuế / Vụ Tài chính (Bộ Tài chính) |
| **Giao diện** | Admin site |
| **Ngày tạo** | 2026-04-24 |
| **Phiên bản** | 1.7 |
| **Quy tắc sinh mã báo cáo** | FDI_AIV9A_[ID] |
| **Loại quy trình** | Quy trình 3 bước, CMCĐT_BCTK_09 |

> **Lưu ý kiến trúc:** Mẫu A.IV.9a là eForm Grid **Fixed 34 Rows** — bảng cố định 34 dòng tương ứng 34 tỉnh/thành phố theo danh mục hành chính sáp nhập mới. Không cho phép thêm/xóa dòng. 5 cột số liệu có hỗ trợ auto-fill từ API TMS (Hệ thống Quản lý Thuế). Hỗ trợ 2 chế độ:
> - **Mode A (Thủ công)** — Kích hoạt khi API TMS KHÔNG khả dụng (auto-detect). Bảng hiển thị 34 dòng với cột số liệu trống, user tự nhập.
> - **Mode B (API TMS)** — Kích hoạt khi API TMS khả dụng (auto-detect). Hệ thống auto-fill dữ liệu vào các dòng tương ứng. **Tất cả dữ liệu vẫn Editable** — user có thể hiệu chỉnh sau khi API điền.
> - **Exception CMR_12:** Mẫu A.IV.9a áp dụng Editable sau API fill thay vì Disabled, theo yêu cầu nghiệp vụ — user chịu trách nhiệm cuối cùng về tính chính xác dữ liệu.
> - **Cơ chế chuyển đổi:** Auto-detect, **không có toggle/switch trên UI**.
> - Dòng Tổng cuối bảng là Auto-calc SUM. Footer tự động từ hệ thống. **Mẫu 9a và 9b (UC131-136) là hai báo cáo hoàn toàn độc lập — 9a lấy dữ liệu từ API TMS, 9b lấy từ API Cục Thuế. Không tổng hợp qua lại.**

---

## UC125-130.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo tổng hợp tình hình tài chính và nộp ngân sách của TCKT có vốn ĐTNN năm (theo địa bàn tỉnh/TP) (Mẫu A.IV.9a)
- Chức năng cho phép Cục Thuế / Bộ Tài chính truy cập danh sách báo cáo định kỳ năm, được nhóm theo từng Kỳ hạn báo cáo. Mục tiêu: Hỗ trợ nộp báo cáo tổng hợp trực tuyến, làm căn cứ quản lý thuế và nộp ngân sách theo địa bàn.
- Out of scope: Không cho phép nộp báo cáo trễ hạn. Việc duyệt báo cáo được thực hiện ở một UC riêng biệt.

Phân quyền: Chỉ người dùng có tổ chức thuộc Cục Thuế / Vụ Tài chính (Bộ Tài chính) mới có quyền truy cập. Không áp dụng CMR_01/CMR_02 (dành cho NĐT/TCKT).

**Tiền điều kiện (Preconditions):**
- Tài khoản người dùng có quyền lập/xem báo cáo thuộc đơn vị Cục Thuế / Vụ Tài chính (Bộ Tài chính).
- Kỳ báo cáo đang ở trạng thái "Trong thời hạn".

**Hậu điều kiện (Postconditions):**
- Sau khi Nộp báo cáo thành công, hệ thống gửi thông báo (Notification) cho đơn vị cấp trên (Cục ĐTNN).
- Các thao tác Thêm, Sửa, Xóa đều được hệ thống ghi nhận lịch sử (Audit log).

Truy cập chức năng: Phân hệ Báo cáo → Quản lý ĐTNN vào VN → Báo cáo tổng hợp tình hình tài chính và nộp ngân sách TCKT (Mẫu A.IV.9a)

Chức năng đáp ứng usecase số: 125, 126, 127, 128, 129, 130

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện:

**Periodic-single**: Giao diện mẫu cho báo cáo có kỳ hạn năm và gửi lẻ từng báo cáo.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | | |
| 1 | Năm báo cáo | Yearpicker | Năm hiện tại | x | | Chọn năm; lọc và nhóm danh sách theo năm. Kết quả hiển thị ngay. Tham chiếu: CMR_07. |
| 2 | Trạng thái kỳ hạn | Multiple-selection Dropdown | Tất cả | x | | Người dùng chọn một hoặc nhiều giá trị: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_04, CMR_07, CMR_16. |
| 3 | Trạng thái báo cáo | Multiple-selection Dropdown | Tất cả | x | | Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07, CMR_16. |
| 4 | Mã báo cáo | Search bar | Null | x | | Tìm theo mã báo cáo. Hiển thị ngay khi nhập. Nếu không tìm thấy: "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| **Khung Danh sách kỳ hạn** | | | | | | |
| 5 | Kỳ hạn báo cáo | Label | Null | | | VD: "Năm 2026". Tham chiếu: CMR_08. |
| 6 | Trạng thái kỳ | Label | Null | | | Tham chiếu: CMR_04. |
| 7 | Lập báo cáo | Button | Null | | | Chỉ hiển thị khi kỳ ở trạng thái **Trong thời hạn**. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CF_01, CMR_04. |
| 8 | Nhập từ file | Button | Null | | | Chỉ hiển thị khi kỳ ở trạng thái **Trong thời hạn**. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| **Khung Danh sách Báo cáo** (trong mỗi kỳ) | | | | | | |
| 9 | Mã báo cáo | Label | Null | | | Tham chiếu: CMR_09. |
| 10 | Địa bàn | Label | Null | | | Tỉnh/TP của cơ quan lập báo cáo. |
| 11 | Ngày cập nhật | Label | Null | | | Định dạng: dd/MM/yyyy HH:mm. |
| 12 | Trạng thái báo cáo | Label | Null | | | Tham chiếu: CMR_03. |
| 13 | Hành động | Button group | Null | | | Chi tiết tham chiếu: UC125-130.3. |

---

### 3. Mô tả các xử lý của chức năng

- Hệ thống nhóm theo Kỳ hạn năm. Mặc định collapse; sắp xếp giảm dần. Tham chiếu: CMR_10.
- Tất cả bộ lọc hiển thị kết quả ngay lập tức. Tham chiếu: CMR_07.
- Nút [Lập báo cáo] và [Nhập từ file] chỉ hiển thị khi kỳ ở trạng thái **Trong thời hạn**. Tham chiếu: CF_01, CMR_04.

---


## UC125-130.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Tạo mới báo cáo tổng hợp tình hình tài chính và nộp ngân sách của TCKT có vốn ĐTNN năm (theo địa bàn tỉnh/TP) (Mẫu A.IV.9a)
- Chức năng cho phép nhập liệu theo biểu mẫu A.IV.9a. Báo cáo là eForm Grid **Fixed 34 Rows** — bảng cố định 34 dòng tương ứng 34 tỉnh/thành phố theo danh mục hành chính sáp nhập mới, 5 cột số liệu, hỗ trợ auto-fill từ API TMS. Bảng dữ liệu hỗ trợ 2 chế độ:
  - **Mode A (Thủ công)** — Kích hoạt khi API TMS KHÔNG khả dụng (auto-detect). Bảng hiển thị 34 dòng với cột số liệu trống, user tự nhập.
  - **Mode B (API TMS)** — Kích hoạt khi API TMS khả dụng (auto-detect). Hệ thống auto-fill dữ liệu vào các dòng tương ứng. **Tất cả dữ liệu vẫn Editable** — user có thể hiệu chỉnh.
  - **Cơ chế chuyển đổi:** Auto-detect dựa trên kết nối API, **không có toggle/switch trên UI**.
  - **Exception CMR_12:** Mẫu A.IV.9a áp dụng Editable sau API fill thay vì Disabled, theo yêu cầu nghiệp vụ — user chịu trách nhiệm cuối cùng về tính chính xác dữ liệu.
  - Dòng Tổng cuối bảng Auto-calc. Footer tự động từ hệ thống. Tham chiếu: CF_01.

Phân quyền: Chỉ người dùng có tổ chức thuộc Cục Thuế / Vụ Tài chính (Bộ Tài chính) mới có quyền lập báo cáo. Không áp dụng CMR_01/CMR_02.

Truy cập chức năng: Màn danh sách báo cáo (UC125-130.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 125, 126

---

### 2. Mô tả giao diện

**Giao diện thêm mới**

Giao diện: Màn hình tạo mới theo biểu mẫu A.IV.9a.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **PHẦN HEADER** | | | | | | |
| 1 | Năm báo cáo | Yearpicker | Năm hiện tại | | x | Hiển thị năm báo cáo đã chọn từ màn danh sách. **Disabled** — không cho sửa. Năm được truyền từ context kỳ hạn đang mở tại màn danh sách. Tham chiếu: CMR_05. |
| **BẢNG DỮ LIỆU — FIXED 34 ROWS** | | | | | | Bảng cố định 34 dòng tương ứng 34 tỉnh/thành phố theo danh mục hành chính sáp nhập mới. Không cho phép thêm/xóa dòng. |
| Cột (1) | STT | Integer | Auto | | | Hệ thống tự đánh số 1-34. Disabled. |
| Cột (2) | Tỉnh/Thành phố | Label | Auto | | x | Hiển thị tên 34 tỉnh/TP theo danh mục hành chính sáp nhập mới. **Disabled** — không cho sửa. Sắp xếp theo mã đơn vị hành chính. |
| Cột (3) | Nộp ngân sách (triệu VNĐ) - Thu từ xuất, nhập khẩu | Decimal | Null | x | x | Tối đa 5 chữ số thập phân. Giá trị ≥ 0. **Mode B:** Auto-fill từ API TMS, vẫn **Editable**. Tham chiếu: CMR_05. |
| Cột (4) | Nộp ngân sách (triệu VNĐ) - Thu nội địa | Decimal | Null | x | x | Tối đa 5 chữ số thập phân. ≥ 0. **Mode B:** Auto-fill, vẫn **Editable**. Tham chiếu: CMR_05. |
| Cột (5) | Nộp ngân sách (triệu VNĐ) - Thu từ dầu thô | Decimal | Null | x | x | Tối đa 5 chữ số thập phân. ≥ 0. **Mode B:** Auto-fill, vẫn **Editable**. Tham chiếu: CMR_05. |
| Cột (6) | Số doanh nghiệp — Lỗ | Integer | Null | x | x | Integer ≥ 0. **Mode B:** Auto-fill, vẫn **Editable**. Tham chiếu: CMR_05. |
| Cột (7) | Số doanh nghiệp — Lãi | Integer | Null | x | x | Integer ≥ 0. **Mode B:** Auto-fill, vẫn **Editable**. Tham chiếu: CMR_05. |
| **DÒNG TỔNG** | | | | | | Dòng cuối bảng. Disabled. |
| — | Tổng — Cột (3) | Auto-calc | — | | | SUM toàn bộ cột (3) của 34 dòng. Tối đa 5 chữ số thập phân. Cập nhật real-time. |
| — | Tổng — Cột (4) | Auto-calc | — | | | SUM toàn bộ cột (4). Tối đa 5 chữ số thập phân. Real-time. |
| — | Tổng — Cột (5) | Auto-calc | — | | | SUM toàn bộ cột (5). Tối đa 5 chữ số thập phân. Real-time. |
| — | Tổng — Cột (6) | Auto-calc | — | | | SUM toàn bộ cột (6). Integer. Real-time. |
| — | Tổng — Cột (7) | Auto-calc | — | | | SUM toàn bộ cột (7). Integer. Real-time. |
| **PHẦN FOOTER** | | | | | | |
| — | Nơi lập báo cáo | Text/Label | Auto | | | Disabled. Hệ thống tự điền tên tỉnh/TP theo địa chỉ trụ sở của cơ quan đăng nhập. Không cho sửa. |
| — | Ngày, tháng, năm | Date/Label | Auto | | | Disabled. Hệ thống tự điền ngày hiện tại (Current System Date). Định dạng: dd/MM/yyyy. Không cho sửa. |
| **Các Button** | | | | | | |
|  | | — | Hủy | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]"). |
|  | | - | Xem trước | Button | | | | Mở popup PDF Preview báo cáo. Tham chiếu: CF_07.1. |
|  | | — | Lưu nháp | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]"). |
|  | | — | Nộp báo cáo | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |

---

### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu: CF_01 (Lập báo cáo), CF_04 (Xuất báo cáo), CF_05 (In), CMR_18.

**Xử lý đặc thù Mẫu A.IV.9a:**

- **Khởi tạo bảng:** Bảng luôn hiển thị cố định 34 dòng tương ứng 34 tỉnh/thành phố theo danh mục hành chính sáp nhập mới. Không cho phép thêm/xóa dòng. Cột Tỉnh/TP = Label (Disabled), sắp xếp theo mã đơn vị hành chính.

- **Cơ chế chuyển đổi Mode A/B (Auto-detect):**
  - Khi mở form [Lập báo cáo] → hệ thống gọi health-check API TMS.
  - API OK → **Mode B** kích hoạt (auto-fill dữ liệu vào các dòng tương ứng, tất cả vẫn Editable).
  - API Fail/Timeout → **Mode A** kích hoạt + Toast T05. Tham chiếu: CMR_12. Bảng hiển thị 34 dòng với cột số liệu trống.
  - **Không có toggle/switch trên UI**.

- **Mode A — Nhập tay:**
  - Bảng hiển thị 34 dòng cố định. Cột Tỉnh/TP đã điền sẵn (Disabled) theo danh mục hành chính sáp nhập mới.
  - Các cột số liệu (3)-(7) hiển thị trống, placeholder theo CMR_05.
  - Người dùng nhập trực tiếp 5 cột số liệu cho từng dòng.

- **Mode B — API TMS:**
  - Nguồn: Kho dữ liệu Báo cáo Tài chính và Hồ sơ nộp thuế từ Hệ thống Quản lý Thuế (TMS). Format: JSON/REST API.
  - Quy trình: API rà quét toàn bộ DN có MST thuộc diện FDI → Group By tỉnh/TP → Tính toán cột (3)-(7). Auto-fill vào dòng tương ứng.
  - **Tất cả dữ liệu vẫn Editable** — user có thể hiệu chỉnh giá trị sau khi API điền. User chịu trách nhiệm cuối cùng về tính chính xác.
  - Tỉnh/TP không có dữ liệu từ API → cột số liệu để trống, user tự nhập nếu cần.
  - Retry: Nếu API lỗi tạm thời → retry 3 lần, mỗi lần cách 5 giây. Sau 3 lần fail → Toast T05 (Tham chiếu: CMR_12) + chuyển Mode A.

- **Sort:**
  - Các cột hỗ trợ sort: C3 (Thu từ XNK), C4 (Thu nội địa), C5 (Thu từ dầu thô), C6 (Số DN Lỗ), C7 (Số DN Lãi).
  - Icon sort hiển thị trên header các cột trên. Click icon → toggle: Ascending ↑ / Descending ↓.
  - **Mặc định sort:** C7 (Số DN Lãi) Descending (max → min).
  - Dòng Tổng luôn ở cuối bảng, không tham gia sort.
  - **Sort persist:** Sort order được lưu cùng bản ghi (server-side). Khi mở Chỉnh sửa (CF_03) hoặc Xem chi tiết (CF_07), hệ thống restore sort order đã lưu.
  - Mode B: hệ thống auto-sort theo default sort (C7 Descending) trước khi render.

- **Cross-validation DN Lãi + Lỗ:**
  - Nếu tổng SUM Cột (6) + SUM Cột (7) khác tổng số DN FDI trên địa bàn (nếu có dữ liệu tham chiếu) → **Warning only** (yellow banner): "Tổng số DN Lãi + Lỗ không bằng tổng số DN FDI. Vui lòng kiểm tra." Không chặn nộp.

- **Dòng Tổng:** Cập nhật real-time khi người dùng thay đổi bất kỳ ô nào. Disabled — không cho sửa trực tiếp. Cột (3)-(5): tối đa 5 chữ số thập phân. Cột (6)-(7): Integer.

- **Footer:** Nơi lập báo cáo và Ngày tháng năm tự động từ hệ thống. Không cho sửa.

- **Validate khi Nộp:** Tất cả 5 cột số liệu ≥ 0. Cột (3)-(5): tối đa 5 chữ số thập phân. Cột (6)-(7): integer. Nếu vi phạm validate → lỗi inline, dừng luồng. Tham chiếu: CF_01.

- **Nhập từ file:** Tham chiếu CF_02 Case 2 (báo cáo không có Phạm vi dữ liệu nguồn input). File .xlsx only, max 10MB.
  - **Template structure:** File mẫu gồm 34 dòng tương ứng 34 tỉnh/TP (cột Tỉnh/TP pre-filled, Disabled). Người dùng chỉ điền 5 cột số liệu (3)-(7).
  - **Validate số dòng:** Hệ thống kiểm tra file upload phải có đúng 34 dòng dữ liệu. Nếu khác 34 dòng → Alert: *"Cấu trúc file không đúng định dạng template. Vui lòng sử dụng file template đã tải."*
  - **Mapping logic:** Hệ thống map dữ liệu từ file vào bảng theo cột Tỉnh/TP (khớp tên tỉnh/TP). Nếu tên tỉnh/TP trong file không khớp danh mục → Alert: *"Dữ liệu không khớp danh mục tỉnh/thành phố. Vui lòng kiểm tra lại."*

- **Validate khi Lưu nháp (CF_01 Case 2):** Báo cáo không có Phạm vi dữ liệu nguồn input — bắt buộc ít nhất 1 ô số liệu (C3-C7) phải có dữ liệu trước khi lưu. Nếu tất cả ô trống → Toast lỗi: *"Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp"*. Tham chiếu: CF_01.

- **Notification khi Nộp:** Hệ thống gửi thông báo cho Cục ĐTNN với nội dung: "Báo cáo [Mã báo cáo] đã được nộp bởi [Tên đơn vị lập] cho kỳ [Năm YYYY]."

- Xuất báo cáo: Kết xuất file **Excel (.xlsx)**. Tham chiếu: CF_04.

---


## UC125-130.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ — Xem chi tiết, Xem vòng đời, In, Kết xuất, Nộp, Chỉnh sửa
- Chức năng cho phép người dùng thực hiện các tác vụ bổ trợ tương ứng trạng thái bản ghi.

Phân quyền: Kiểm soát theo trạng thái bản ghi. Chỉ người dùng thuộc Cục Thuế / Vụ Tài chính (Bộ Tài chính) mới có quyền Nộp/Chỉnh sửa/Xóa. Tham chiếu: CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC125-130.1) → Cột Hành động → Chọn tác vụ tương ứng

Chức năng đáp ứng usecase số: 127, 128, 129, 130

---

### 2. Mô tả giao diện

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Chỉ Lưu nháp và Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_09. Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |
| 2 | Chỉnh sửa | Button | Chỉ Lưu nháp và Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Tất cả người dùng | Kết xuất file Excel (.xlsx). Tham chiếu: CF_04. |
| 7 | Xóa | Button | Lưu nháp **VÀ** chưa từng nộp | Người tạo | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết: Tham chiếu: CF_07.
- Xem vòng đời: Tham chiếu: CF_06.
- In báo cáo: Tham chiếu: CF_05.
- Xuất báo cáo: Kết xuất ra file **Excel (.xlsx)**. Tham chiếu: CF_04.
- Chỉnh sửa báo cáo: Tham chiếu: CF_03.

---

## 3.4 Acceptance Criteria (Tiêu chí nghiệm thu)

- **AC1 Fixed 34 Rows:** Khi vào màn hình "Lập báo cáo", bảng luôn hiển thị cố định 34 dòng tương ứng 34 tỉnh/TP theo danh mục hành chính sáp nhập mới. Không cho phép thêm/xóa dòng.
- **AC2 Mode Detect:** Khi mở form, hệ thống gọi health-check API TMS. API OK → Mode B (auto-fill, Editable). API Fail → Mode A + Toast T05 (Tham chiếu: CMR_12). Retry 3x5s trước khi chuyển Mode A.
- **AC3 Auto-fill TMS (Mode B):** Hệ thống gọi API TMS → auto-fill cột (3)-(7) cho các dòng tỉnh/TP có dữ liệu. Tất cả dữ liệu vẫn Editable — user có thể hiệu chỉnh.
- **AC4 API Fail (Mode A):** API TMS không khả dụng → Toast T05 (Tham chiếu: CMR_12) + bảng 34 dòng với cột số liệu trống, user tự nhập.
- **AC5 Tỉnh/TP Disabled:** Cột Tỉnh/TP = Label, Disabled. User không thể sửa tên tỉnh/TP.
- **AC6 SUM Real-time:** Dòng Tổng phải cập nhật ngay lập tức giá trị tổng của các cột (3)-(7) mỗi khi thay đổi bất kỳ ô nào. Cột (3)-(5): tối đa 5dp. Cột (6)-(7): Integer.
- **AC7 Validate số dương:** Khi nhấn "Nộp báo cáo", tất cả ô số liệu (C3-C7) ≥ 0. Nếu vi phạm → lỗi inline "Giá trị phải ≥ 0" và chặn nộp.
- **AC8 Decimal precision:** Cột (3)-(5): tối đa 5 chữ số thập phân. Cột (6)-(7): integer.
- **AC9 DN Lãi+Lỗ Warning:** Nếu SUM C6 + SUM C7 khác tổng DN FDI → Warning only (không chặn nộp).
- **AC10 Footer tự động:** Nơi lập báo cáo và Ngày lập Disabled, điền tự động.
- **AC11 Sort:** Icon sort hiển thị trên header C3, C4, C5, C6, C7. Click → toggle Ascending/Descending. Mặc định: C7 Descending (max → min). Dòng Tổng luôn ở cuối. Sort order lưu server-side, restore khi mở Chỉnh sửa/Xem chi tiết.
- **AC12 Concurrent Edit:** Last Write Wins — khi 2 user cùng lưu/nộp cùng lúc, thao tác sau ghi đè thao tác trước. Cả 2 thao tác được ghi vào Lifecycle Log. Tham chiếu: CF_06.
- **AC13 9a/9b Độc lập:** Mẫu 9a (UC125-130) và Mẫu 9b (UC131-136) là hai báo cáo hoàn toàn độc lập. Không tổng hợp qua lại.

---

## 3.5 Non-Functional Requirements (Yêu cầu phi chức năng)

- **Performance:** Thời gian tải bảng 34 dòng và auto-fill từ API không vượt quá 5 giây. API TMS retry 3 lần mỗi lần cách 5 giây trước khi fallback sang nhập thủ công (Toast T05, Tham chiếu: CMR_12). Format API: JSON/REST.
- **Security & Audit:** Chỉ người dùng thuộc Cục Thuế / Vụ Tài chính (Bộ Tài chính) mới có quyền Thêm/Sửa/Nộp. Mọi hành động đều được ghi log chi tiết (Actor, Action, Target, Timestamp).
- **Concurrency:** Áp dụng Last Write Wins — khi 2 user cùng lưu/nộp cùng lúc, thao tác sau ghi đè thao tác trước. Cả 2 thao tác đều được ghi vào Lifecycle Log (Actor, Action, Timestamp). Tham chiếu: CF_06.

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-07 | 1.0 → 1.1 | Thông tin chung | (Không có) | Thêm Mục tiêu, Phạm vi, Tiền kiện, Hậu kiện. | Chuẩn hóa tài liệu theo QC Audit. |
| 2026-05-07 | 1.0 → 1.1 | Tiêu chí nghiệm thu | (Không có) | Bổ sung 6 AC chi tiết cho luồng báo cáo tổng hợp. | Chuẩn hóa tài liệu theo QC Audit. |
| 2026-05-07 | 1.0 → 1.1 | Yêu cầu phi chức năng | (Không có) | Bổ sung NFR (Performance, Security). | Chuẩn hóa tài liệu theo QC Audit. |
| 2026-05-07 | 1.1 → 2.0 | Phiên bản | 1.1 | 2.0 | Cập nhật sau QC Re-Audit Round 2. |
| 2026-05-07 | 2.0 | Kiến trúc | (Chung) | Bổ sung 9a/9b độc lập, Mode A/B auto-detect, admin code order | QC Audit — làm rõ kiến trúc. |
| 2026-05-07 | 2.0 | Bảng dữ liệu | Editable toàn bộ | Mode B: ô fill Disabled / ô null Enabled. Mode A: Enabled toàn bộ | QC Audit — API row locking. |
| 2026-05-07 | 2.0 | Cột (3)-(5) | Decimal | Integer 0dp triệu VND, round half up | QC Audit — decimal precision. |
| 2026-05-07 | 2.0 | Xử lý đặc thù | (Cơ bản) | Thêm Mode A/B, API partial, retry 3x5s, DN Lãi+Lỗ warning, Nhập từ file validate 63 dòng | QC Audit — chi tiết hóa. |
| 2026-05-07 | 2.0 | AC | AC1-AC6 | AC1-AC14 (thêm Mode detect, API partial, decimal, DN warning, nhập từ file, concurrent, 9a/9b) | QC Audit — bổ sung AC. |
| 2026-05-07 | 2.0 | NFR | Performance, Security | Thêm Concurrency, API retry, JSON/REST format | QC Audit — bổ sung NFR. |
| 2026-05-11 | 1.0→1.1 | Quy tắc sinh mã báo cáo | `DTNN_A4_9a_[ID]` | `FDI_AIV9A_[ID]` | Chuẩn hóa prefix và mã theo appendices.md v2.0 (INS-10) |
| 2026-05-11 | +1 | Label Trạng thái kỳ | `Trạng thái (cấp kỳ)` | `Trạng thái kỳ` | Chuẩn hóa tên label (INS-06) |
| 2026-05-11 | +1 | Kiểu field Năm báo cáo | `Number` | `Yearpicker` | Đồng nhất kiểu field (INS-04) |
| 2026-05-11 | 1.2 → 1.3 | Toast T05 (Mode A fallback) | Nội dung toast tự viết | Tham chiếu CMR_12 (T05 chuẩn) | QC Feedback — chuẩn hóa toast. |
| 2026-05-11 | 1.2 → 1.3 | Mục API Partial Failure | Có mục + AC5 + toast warning | Xóa — không có cơ chế phát hiện data thiếu/đủ | QC Feedback — logic không khả thi. |
| 2026-05-11 | 1.2 → 1.3 | AC | AC1-AC14 (có AC5 API Partial) | AC1-AC13 (bỏ AC5, đánh lại số) | QC Feedback — đồng bộ với xóa API Partial. |
| 2026-05-11 | 1.2 → 1.3 | AC12 + NFR Concurrency | Optimistic locking — conflict + refresh | Last Write Wins theo CMR_02 — thao tác sau ghi đè, cả 2 ghi Lifecycle Log | QC Feedback — đồng bộ CMR_02, CF_06. |
| 2026-05-12 | 1.3 → 1.4 | Kiến trúc bảng | Cố định 63 dòng (load sẵn 63 tỉnh/TP) | Dynamic Rows — chỉ sinh dòng cho tỉnh/TP có dữ liệu | Client confirm: chỉ tỉnh nào có số thì báo cáo. |
| 2026-05-12 | 1.3 → 1.4 | Cột Tỉnh/TP | Text/Label (Disabled, từ master data) | Dropdown (chọn từ 63 tỉnh/TP, unique, auto-filter) | Chuyển từ fixed → dynamic. |
| 2026-05-12 | 1.3 → 1.4 | Thêm/Xóa dòng | Không có (63 dòng cố định) | [+ Thêm dòng] + icon Xóa dòng manual | Dynamic Rows cần thao tác thêm/xóa. |
| 2026-05-12 | 1.3 → 1.4 | Mode B behavior | Ô fill Disabled, ô null Enabled | Dòng API Disabled toàn bộ, user thêm dòng manual bổ sung | Đồng bộ pattern với UC137-142, UC143-148. |
| 2026-05-12 | 1.3 → 1.4 | Nhập từ file | CF_02 Case 2, phải đúng 63 dòng | CF_02, không validate số dòng cố định | Bỏ ràng buộc 63 dòng. |
| 2026-05-12 | 1.3 → 1.4 | AC | AC1-AC13 | AC1-AC14 (thêm unique, empty table, xóa dòng, đánh lại số) | Bổ sung AC cho Dynamic Rows. |
| 2026-05-14 | 1.4 → 1.5 | Kiến trúc bảng | Dynamic Rows — chỉ sinh dòng cho tỉnh/TP có dữ liệu | Fixed 34 Rows — 34 tỉnh/TP theo danh mục sáp nhập mới, không thêm/xóa dòng | Client confirm: chuyển sang 34 tỉnh sáp nhập. |
| 2026-05-14 | 1.5 | Cột Tỉnh/TP | Dropdown (chọn từ 63 tỉnh/TP, unique, auto-filter) | Label (Disabled, pre-filled 34 tỉnh/TP) | Fixed 34 Rows. |
| 2026-05-14 | 1.5 | Cột (3)-(5) decimal | 0 chữ số thập phân (integer, round half up) | Tối đa 5 chữ số thập phân | Client feedback — tăng precision. |
| 2026-05-14 | 1.5 | Dòng API | Disabled (không sửa, không xóa), có tag "API" | Editable (cho sửa), bỏ tag "API" | Client feedback — user chịu trách nhiệm cuối cùng. |
| 2026-05-14 | 1.5 | Sort | Không có | Icon sort C3, C4, C5, C6, C7. Mặc định: C7 Descending (max → min) | Client feedback — thêm sort. |
| 2026-05-14 | 1.5 | Thêm/Xóa dòng | [+ Thêm dòng] + icon Xóa dòng manual | Xóa — bảng cố định 34 dòng | Fixed 34 Rows. |
| 2026-05-14 | 1.5 | AC | AC1-AC14 (Dynamic Rows, unique, empty table, xóa dòng) | AC1-AC13 (Fixed 34, Editable, Sort) | Viết lại AC cho Fixed 34 Rows. |
| 2026-05-14 | 1.5 → 1.6 | Filter Địa bàn (danh sách) | Có filter Địa bàn (row #2) | Xóa — báo cáo đơn lẻ, không cần lọc theo địa bàn | QC Review. |
| 2026-05-14 | 1.6 | Năm báo cáo (form Lập) | Editable, validate 4 chữ số | Disabled — hiển thị năm đã chọn từ màn danh sách | QC Review — năm đã chọn ở màn danh sách, không cần nhập lại. |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (2 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-21 | 1.6 → 1.7 | Phân quyền | Tham chiếu CMR_02 | Xóa CMR_02 — chỉ phân quyền cho user có tổ chức thuộc Cục Thuế / Vụ Tài chính (BTC). Không áp dụng CMR_01/CMR_02 | QC Audit — cơ quan nhà nước không thuộc mô hình NĐT/TCKT |
| 2026-05-21 | 1.7 | Exception CMR_12 | Không có ghi chú | Bổ sung "Exception CMR_12: Editable sau API fill thay vì Disabled — user chịu trách nhiệm cuối cùng" | QC Audit — giải quyết conflict CMR_12 vs Mode B Editable |
| 2026-05-21 | 1.7 | Filter dropdown mặc định | Null | Tất cả | QC Audit — đồng bộ CMR_16 |
| 2026-05-21 | 1.7 | Validate Lưu nháp | Không mô tả | Bổ sung CF_01 Case 2: ít nhất 1 ô số liệu phải có dữ liệu | QC Audit — CONFLICT-03 |
| 2026-05-21 | 1.7 | Mode A initial state | Mô tả chung | Bổ sung: cột Tỉnh/TP điền sẵn theo danh mục, cột số liệu trống + placeholder CMR_05 | QC Audit — GAP-02 |
| 2026-05-21 | 1.7 | Nhập từ file | Chỉ tham chiếu CF_02 | Bổ sung template 34 dòng, validate số dòng = 34, mapping theo tên tỉnh/TP | QC Audit — GAP-03 |
| 2026-05-21 | 1.7 | Sort persistence | Sort persist khi Lưu nháp | Sort order lưu server-side, restore khi mở CF_03/CF_07 | QC Audit — GAP-04 |
| 2026-05-21 | 1.7 | Năm báo cáo (form Lập) | Disabled, hiển thị năm từ danh sách | Bổ sung: năm truyền từ context kỳ hạn đang mở | QC Audit — GAP-06 |
| 2026-05-21 | 1.7 | Xuất báo cáo | Excel | Excel (.xlsx) | QC Audit — INC-01 làm rõ format |
| 2026-05-21 | 1.7 | Cơ quan nhận / Đối tượng lập | Bộ Tài chính (chung) | Phân biệt: Cơ quan nhận = Vụ NSNN (BTC), Đối tượng lập = Cục Thuế / Vụ Tài chính (BTC) | QC Audit — INC-02 làm rõ 2 đơn vị |
