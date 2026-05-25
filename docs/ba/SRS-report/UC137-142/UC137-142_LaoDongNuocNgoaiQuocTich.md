# UC137-142: Báo cáo tổng hợp tình hình lao động nước ngoài làm việc tại các TCKT có vốn ĐTNN năm ...... (theo quốc tịch) — Mẫu A.IV.10a

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | yen.le2 |
| **Phân hệ** | Quản lý đầu tư nước ngoài vào Việt Nam |
| **Mẫu biểu** | Mẫu A.IV.10a |
| **Loại báo cáo** | Định kỳ năm |
| **Phạm vi báo cáo**           | Không có phạm vi                                              |
| **Hình thức nộp** | Báo cáo đơn lẻ (Single report form) |
| **Cơ quan nhận** | Cục Đầu tư nước ngoài, Bộ Tài chính |
| **Đối tượng lập** | Bộ Nội vụ (Cục Việc làm) |
| **Giao diện** | Admin site |
| **Ngày tạo** | 2026-04-24 |
| **Phiên bản** | 1.7 |
| **Quy tắc sinh mã báo cáo** | FDI_AIV10A_[ID] |
| **Loại quy trình** | Quy trình 3 bước, CMCĐT_BCTK_09 |

> **Lưu ý kiến trúc:** Mẫu A.IV.10a là eForm Grid **lặp động** (Dynamic Rows — max 500 dòng) — số dòng thay đổi theo số quốc tịch. Hệ thống hỗ trợ 2 chế độ vận hành:
> - **Mode A (Thủ công)** — Kích hoạt khi API Cục Việc làm KHÔNG khả dụng (auto-detect). Người dùng tự thêm dòng, chọn quốc tịch từ master data ISO, nhập số lao động.
> - **Mode B (API Cục Việc làm)** — Kích hoạt khi API khả dụng (auto-detect). Hệ thống tự sinh N dòng theo quốc tịch. **Tất cả dữ liệu vẫn Editable** — user có thể hiệu chỉnh sau khi API điền. User vẫn được thêm dòng bổ sung.
> - **Cơ chế chuyển đổi:** Auto-detect, **không có toggle/switch trên UI**.

---

## UC137-142.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo tổng hợp lao động nước ngoài theo quốc tịch (Mẫu A.IV.10a)
- Chức năng cho phép Bộ Nội vụ (Cục Việc làm) truy cập danh sách báo cáo định kỳ năm, được nhóm theo từng Kỳ hạn báo cáo. Mục tiêu: Tổng hợp số lượng lao động nước ngoài làm việc tại các doanh nghiệp FDI theo quốc tịch để quản lý nhân lực ngoại quốc.
- Out of scope: Không cho phép nộp báo cáo trễ hạn. Việc duyệt báo cáo được thực hiện ở một UC riêng biệt.

Phân quyền: Bộ Nội vụ (Cục Việc làm). Tham chiếu: CMR_02.

**Tiền điều kiện (Preconditions):**
- Tài khoản người dùng có quyền lập/xem báo cáo thuộc đơn vị Bộ Nội vụ (Cục Việc làm).
- Kỳ báo cáo đang ở trạng thái "Trong thời hạn".

**Hậu điều kiện (Postconditions):**
- Sau khi Nộp báo cáo thành công, hệ thống gửi thông báo (Notification) cho đơn vị cấp trên (Cục ĐTNN).
- Các thao tác Thêm, Sửa, Xóa đều được hệ thống ghi nhận lịch sử (Audit log).

Truy cập chức năng: Phân hệ Báo cáo → Quản lý ĐTNN vào VN → Báo cáo tổng hợp lao động nước ngoài theo quốc tịch (Mẫu A.IV.10a)

Chức năng đáp ứng usecase số: 137, 138, 139, 140, 141, 142

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
| 2 | Trạng thái kỳ hạn | Multiple-selection Dropdown | Tất cả | x | | Người dùng chọn một hoặc nhiều giá trị: Tất cả / Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Mặc định chọn "Tất cả" — hiển thị toàn bộ, không lọc. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_04, CMR_07, CMR_16. |
| 3 | Trạng thái báo cáo | Multiple-selection Dropdown | Tất cả | x | | Người dùng chọn một hoặc nhiều giá trị: Tất cả / Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Mặc định chọn "Tất cả" — hiển thị toàn bộ, không lọc. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07, CMR_16. |
| 4 | Mã báo cáo | Search bar | Null | x | | Tìm theo mã báo cáo. Hiển thị ngay khi nhập. Nếu không tìm thấy: "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| **Khung Danh sách kỳ hạn** | | | | | | |
| 5 | Kỳ hạn báo cáo | Label | Null | | | VD: "Năm 2026". Tham chiếu: CMR_08. |
| 6 | Trạng thái kỳ | Label | Null | | | Tham chiếu: CMR_04. |
| 7 | Lập báo cáo | Button | Null | | | Chỉ hiển thị khi kỳ ở trạng thái **Trong thời hạn**. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CF_01, CMR_04. |
| 8 | Nhập từ file | Button | Null | | | Chỉ hiển thị khi kỳ ở trạng thái **Trong thời hạn**. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| **Khung Danh sách Báo cáo** (trong mỗi kỳ) | | | | | | |
| 9 | Mã báo cáo | Label | Null | | | Tham chiếu: CMR_09. |
| 10 | Ngày cập nhật | Label | Null | | | Định dạng: dd/MM/yyyy HH:mm. |
| 11 | Trạng thái báo cáo | Label | Null | | | Tham chiếu: CMR_03. |
| 12 | Hành động | Button group | Null | | | Chi tiết tham chiếu: UC137-142.3. |

---

### 3. Mô tả các xử lý của chức năng

- Hệ thống nhóm theo Kỳ hạn năm. Mặc định collapse; sắp xếp giảm dần theo năm kỳ hạn (năm mới nhất ở trên). Tham chiếu: CMR_10, CS_01 Mục 4.
- Hiển thị tối đa 10 bản ghi trong mỗi kỳ hạn. Nếu vượt quá 10 bản ghi → kích hoạt thanh cuộn dọc (Scroll) bên trong kỳ hạn đó. Tham chiếu: CS_01 Mục 4.
- Tất cả bộ lọc hiển thị kết quả ngay lập tức. Tham chiếu: CMR_07.
- Nút [Lập báo cáo] và [Nhập từ file] chỉ hiển thị khi kỳ ở trạng thái **Trong thời hạn**. Tham chiếu: CF_01, CMR_04.

---


## UC137-142.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Tạo mới báo cáo tổng hợp lao động nước ngoài theo quốc tịch (Mẫu A.IV.10a)
- Chức năng cho phép nhập liệu theo biểu mẫu A.IV.10a. Báo cáo là eForm Grid **lặp động** (Dynamic Rows — max 500 dòng). Bảng dữ liệu hỗ trợ 2 chế độ:
  - **Mode A (Thủ công)** — Kích hoạt khi API Cục Việc làm KHÔNG khả dụng (auto-detect). User nhập tay, chọn quốc tịch từ dropdown ISO, nhập số lao động.
  - **Mode B (API Cục Việc làm)** — Kích hoạt khi API khả dụng (auto-detect). Hệ thống auto-generate. **Tất cả dữ liệu vẫn Editable** — user có thể hiệu chỉnh. User vẫn được thêm dòng bổ sung.
  - **Cơ chế chuyển đổi:** Auto-detect, **không có toggle/switch trên UI**.
  - Tham chiếu: CF_01.

Phân quyền: Bộ Nội vụ (Cục Việc làm). Tham chiếu: CMR_02.

Truy cập chức năng: Màn danh sách báo cáo (UC137-142.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 137, 138

---

### 2. Mô tả giao diện

**Giao diện thêm mới**

Giao diện: Màn hình tạo mới theo biểu mẫu A.IV.10a.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **PHẦN HEADER** | | | | | | |
| 1 | Năm báo cáo | Yearpicker | Năm hiện tại | | x | Hiển thị năm báo cáo đã chọn từ màn danh sách. **Disabled** — không cho sửa. Tham chiếu: CS_01 Mục 2. |
| **BẢNG DỮ LIỆU — LẶP ĐỘNG (Dynamic Rows — max 500 dòng)** | | | | | | Số dòng thay đổi tùy theo số quốc tịch. |
| Cột (1) | STT | Integer | Auto | | | Hệ thống tự đánh số 1, 2, 3... Disabled. Cập nhật lại (re-index) sau mỗi lần thêm/xóa dòng. |
| Cột (2) | Quốc tịch | Dropdown | Null | x | x | Chọn từ danh mục Quốc gia/Quốc tịch chuẩn **ISO 3166-1**. Kiểu: **Searchable Single-Choice Dropdown** (CMR_07.1 + CMR_06 Live Search) — gõ ký tự → lọc danh sách real-time, chỉ chọn 1 giá trị/dòng. Không được trùng lặp giữa các dòng. Validate: bắt buộc chọn — lỗi: *"Vui lòng chọn quốc tịch"*. Lỗi trùng: *"Quốc tịch đã tồn tại trong danh sách"*. Placeholder: *"Chọn quốc tịch"*. **Mode B:** Auto-fill, vẫn **Editable**. Hiển thị lỗi trong eForm Grid: viền đỏ quanh ô + tooltip chứa message lỗi khi hover. Tham chiếu: CMR_07, CMR_06. |
| Cột (3) | Tổng số lao động ở thời điểm báo cáo | Integer | Null | x | x | Integer > 0. Max length: 18 ký tự. Placeholder: *"Nhập tổng số lao động"*. **Mode B:** Auto-fill, vẫn **Editable**. Validate: phải > 0 — lỗi: *"Tổng số lao động phải lớn hơn 0"*. Trường bắt buộc bỏ trống — lỗi: *"Vui lòng nhập tổng số lao động"*. Hiển thị lỗi trong eForm Grid: viền đỏ quanh ô + tooltip chứa message lỗi khi hover. Tham chiếu: CMR_05. |
| **[Nút thao tác dòng]** | | | | | | |
| — | [+ Thêm dòng] | Button | — | | | Hiển thị ở **footer bảng** (bên dưới dòng cuối cùng). Thêm 1 dòng trống mới. Max 500 dòng; vượt → Toast T16 *"Vượt quá số dòng tối đa cho phép (500)"*. Tham chiếu: CMR_15. |
| — | Xóa dòng | Icon Button (mỗi dòng) | — | | | Chỉ hiển thị khi bảng có **từ 2 dòng trở lên**. Khi chỉ còn 1 dòng → ẩn nút. Nhấn → xóa dòng ngay lập tức, **không hiển thị popup xác nhận**. STT re-index. Tham chiếu: CMR_15. |
| **DÒNG TỔNG SỐ** | | | | | | Dòng cuối bảng. Disabled. |
| — | Tổng số lao động | Auto-calc | — | | | SUM cột (3) toàn bộ dòng. Cập nhật real-time. Read-only. |
| **PHẦN FOOTER** | | | | | | |
| — | Nơi lập báo cáo | Text/Label | Auto | | | Disabled. Hệ thống tự điền tên tỉnh/TP theo địa chỉ trụ sở cơ quan đăng nhập. Không cho sửa. |
| — | Ngày, tháng, năm lập báo cáo | Date/Label | Auto | | | Disabled. Hệ thống tự điền ngày hiện tại (Current System Date). Định dạng: dd/MM/yyyy. Không cho sửa. |
| **Các Button** | | | | | | |
|  | | — | Hủy | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]"). |
|  | | — | Xem trước | Button | | | | Mở popup PDF Preview báo cáo. **Disabled** khi báo cáo chưa được Lưu nháp lần nào (tooltip: *"Vui lòng Lưu nháp hoặc Nộp báo cáo trước khi xem preview."*). **Enabled** sau khi Lưu nháp/Nộp thành công ít nhất 1 lần. Tham chiếu: CF_01 (Xem trước), CF_07.1. |
|  | | — | Lưu nháp | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]"). |
|  | | — | Nộp báo cáo | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |

---

### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu: CF_01 (Lập báo cáo), CF_04 (Xuất báo cáo), CF_05 (In), CMR_18.

**Xử lý đặc thù Mẫu A.IV.10a:**

A. Cơ chế chuyển đổi Mode A/B (Auto-detect):
- Khi mở form [Lập báo cáo] → hệ thống gọi health-check API Hệ thống Giấy phép lao động (Cục Việc làm).
- **Loading state:** Trong khoảng chờ API (≤ 5s), hệ thống hiển thị loading indicator (spinner) trên vùng bảng dữ liệu. Các nút hành động (Lưu nháp, Nộp, Hủy) vẫn hiển thị nhưng vùng bảng ở trạng thái chờ.
- API OK → **Mode B** kích hoạt (auto-generate dòng quốc tịch).
- API Fail/Timeout (> 5s) → **Mode A** kích hoạt + Toast T05. Tham chiếu: CMR_12. Enable toàn bộ form.
- **Không có toggle/switch trên UI**.
- **Baseline dirty form (Mode B):** Dữ liệu auto-fill từ API Mode B được coi là giá trị khởi tạo (baseline) — form KHÔNG dirty sau auto-fill. Dirty Form Guard (CMR_14) chỉ kích hoạt khi user thay đổi giá trị so với baseline này.

B. Mode A — Nhập tay (Manual Mode):
- Người dùng tự thêm dòng bằng nút [+ Thêm dòng], chọn quốc tịch từ Dropdown ISO 3166-1 (có auto-filter: gõ ký tự → lọc), nhập số lao động.
- Validate quốc tịch không trùng lặp giữa các dòng — nếu trùng → viền đỏ quanh ô + tooltip "Quốc tịch đã tồn tại trong danh sách".
- Validate cột (3) > 0. Lỗi: viền đỏ quanh ô + tooltip "Tổng số lao động phải lớn hơn 0".
- **Hiển thị lỗi eForm Grid:** Do không gian hạn chế trong ô lưới, lỗi hiển thị dạng **viền đỏ** quanh ô; hover vào ô hiển thị **tooltip** chứa message lỗi tương ứng. Tham chiếu: CMR_05, CMR_07.
- Dòng Tổng cập nhật real-time.

C. Mode B — API Cục Việc làm:
- Hệ thống truy vấn danh sách lao động nước ngoài làm việc tại các tổ chức FDI trong kỳ đã chọn, **có giấy phép lao động còn thời hạn tới ngày cuối cùng của năm báo cáo** → đối chiếu MST với danh sách DN FDI → Group By quốc tịch → COUNT số lao động.
- Tự động sinh N dòng (1 dòng/quốc tịch), điền cột (2) và (3).
- **Tất cả dữ liệu vẫn Editable** — user có thể hiệu chỉnh giá trị sau khi API điền. User chịu trách nhiệm cuối cùng về tính chính xác.
- **User vẫn được thêm dòng bổ sung** (quốc tịch chưa có trong API) qua [+ Thêm dòng]. Dropdown auto-filter quốc tịch đã có → khi chọn quốc tịch trùng → viền đỏ quanh ô + tooltip "Quốc tịch đã tồn tại trong danh sách".
- Dòng Tổng SUM(Cột 3) toàn bộ dòng.

D. Sort:
- Cột hỗ trợ sort: C3 (Tổng số lao động).
- Icon sort hiển thị trên header cột C3. Click icon → toggle: Ascending ↑ / Descending ↓.
- **Mặc định sort:** C3 Descending (max → min).
- Dòng Tổng luôn ở cuối bảng, không tham gia sort.
- Dòng mới thêm vào cuối bảng, user tự sort lại nếu muốn.
- Sort persist khi Lưu nháp → mở lại giữ nguyên thứ tự.
- Mode B: hệ thống auto-sort theo default sort (C3 Descending) trước khi render.

F. Validate khi Nộp:
- Bảng phải có ít nhất 1 dòng quốc tịch. Nếu 0 dòng → Toast T15 *"Vui lòng nhập ít nhất 1 dòng dữ liệu"*, chặn nộp.
- Tất cả cột (2) và (3) đã điền đầy đủ và hợp lệ. Cột (3) > 0.
- Vi phạm → viền đỏ quanh ô + tooltip chứa message lỗi (eForm Grid rule), dừng luồng. Tham chiếu: CF_01, CMR_05, CMR_07.
- Nộp thành công → trạng thái "Chờ duyệt".

- Xuất báo cáo: Kết xuất file **Excel**. Tham chiếu: CF_04.

E. Nhập từ file (Import):
- Tham chiếu: CF_02 Case 2 (Báo cáo không có Phạm vi dữ liệu nguồn input).
- Template import cho bảng lặp động gồm 2 cột: Quốc tịch (text — tên quốc tịch theo ISO 3166-1) + Tổng số lao động (integer > 0).
- Validate khi import: Quốc tịch không trùng lặp trong file. Max 500 dòng. Giá trị cột Tổng số lao động > 0.
- Nếu file chứa quốc tịch trùng → Alert: *"File chứa quốc tịch trùng lặp. Vui lòng kiểm tra lại."*
- Nếu file vượt 500 dòng → Alert: *"File vượt quá số dòng tối đa cho phép (500). Vui lòng kiểm tra lại."*

---


## UC137-142.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ — Xem chi tiết, Xem vòng đời, In, Kết xuất, Nộp, Chỉnh sửa
- Chức năng cho phép người dùng thực hiện các tác vụ bổ trợ tương ứng trạng thái bản ghi.

Phân quyền: Kiểm soát theo trạng thái bản ghi. Tham chiếu: CMR_02, CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC137-142.1) → Cột Hành động → Chọn tác vụ tương ứng

Chức năng đáp ứng usecase số: 139, 140, 141, 142

---

### 2. Mô tả giao diện

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Chỉ Lưu nháp và Yêu cầu chỉnh sửa | Bộ Nội vụ (Cục Việc làm) | Tham chiếu: CF_09. Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |
| 2 | Chỉnh sửa | Button | Chỉ Lưu nháp và Yêu cầu chỉnh sửa | Bộ Nội vụ (Cục Việc làm) | Tham chiếu: CF_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Tất cả người dùng | Kết xuất file Excel. Tham chiếu: CF_04. |
| 7 | Xóa | Button | Lưu nháp **VÀ** chưa từng nộp | Bộ Nội vụ (Cục Việc làm) | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết: Tham chiếu: CF_07.
- Xem vòng đời: Tham chiếu: CF_06.
- In báo cáo: Tham chiếu: CF_05.
- Xuất báo cáo: Kết xuất ra file **Excel**. Tham chiếu: CF_04.
- Chỉnh sửa báo cáo: Tham chiếu: CF_03.

---

## 3.4 Acceptance Criteria (Tiêu chí nghiệm thu)

- **AC1 Mode Detect:** Mở form → health-check API Cục Việc làm. OK → Mode B (auto-generate, Editable). Fail → Mode A + Toast T05.
- **AC2 Dynamic Rows:** Mode A: user thêm/xóa dòng. Max 500 dòng; vượt → Toast. STT re-index.
- **AC3 Unique Quốc tịch:** Chặn chọn trùng quốc tịch. Lỗi inline "Quốc tịch đã tồn tại".
- **AC4 ISO Master Data:** Dropdown quốc tịch sử dụng danh mục ISO 3166-1. Có auto-filter (gõ ký tự → lọc).
- **AC5 API Cục Việc làm (Mode B):** Auto-generate N dòng. Tất cả dữ liệu vẫn Editable — user có thể hiệu chỉnh. User thêm dòng bổ sung.
- **AC6 API Logic:** Chỉ tính số lao động nước ngoài làm việc tại các tổ chức FDI trong kỳ đã chọn, có giấy phép lao động còn thời hạn tới ngày cuối cùng của năm báo cáo.
- **AC7 Validate số dương:** Cột (3) > 0. Lỗi: "Tổng số lao động phải lớn hơn 0".
- **AC8 SUM Real-time:** Dòng Tổng cập nhật real-time SUM(Cột 3). Integer.
- **AC9 Validate bắt buộc:** Nộp → bảng ≥ 1 dòng, cột (2) + (3) đầy đủ.
- **AC10 Empty table:** 0 dòng → Toast, chặn nộp.
- **AC11 Xóa dòng:** Nút Xóa chỉ hiển thị khi bảng có ≥ 2 dòng. Khi còn 1 dòng → ẩn nút. Nhấn → xóa ngay lập tức, không popup xác nhận. STT re-index. Tham chiếu: CMR_15.
- **AC12 Sort:** Icon sort hiển thị trên header C3. Click → toggle Ascending/Descending. Mặc định: C3 Descending (max → min). Dòng Tổng luôn ở cuối. Sort persist khi Lưu nháp.
- **AC13 Concurrent Edit:** Last Write Wins — khi 2 user cùng lưu/nộp cùng lúc, thao tác sau ghi đè thao tác trước. Cả 2 thao tác được ghi vào Lifecycle Log. Tham chiếu: CMR_02, CF_06.
- **AC14 Nộp thành công:** Trạng thái "Chờ duyệt".

---

## 3.5 Non-Functional Requirements (Yêu cầu phi chức năng)

- **Performance:** Thời gian gọi API Cục Việc làm và render Grid không quá 5 giây. Nếu quá 5s → Toast T05 (Tham chiếu: CMR_12) + Enable toàn bộ form cho nhập thủ công.
- **Security & Audit:** Chỉ Bộ Nội vụ (Cục Việc làm) mới thấy và lập báo cáo. Lưu vết Audit log đầy đủ.
- **Concurrency:** Áp dụng Last Write Wins — khi 2 user cùng lưu/nộp cùng lúc, thao tác sau ghi đè thao tác trước. Cả 2 thao tác đều được ghi vào Lifecycle Log (Actor, Action, Timestamp). Tham chiếu: CMR_02, CF_06.

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-07 | 1.0 → 1.1 | Thông tin chung | (Không có) | Thêm Mục tiêu, Phạm vi, Tiền kiện, Hậu kiện. | Chuẩn hóa tài liệu theo QC Audit. |
| 2026-05-07 | 1.0 → 1.1 | Tiêu chí nghiệm thu | (Không có) | Bổ sung 6 AC chi tiết cho luồng lao động theo quốc tịch. | Chuẩn hóa tài liệu theo QC Audit. |
| 2026-05-07 | 1.0 → 1.1 | Yêu cầu phi chức năng | (Không có) | Bổ sung NFR (Performance, Security). | Chuẩn hóa tài liệu theo QC Audit. |
| 2026-05-07 | 1.1 → 1.2 | Phiên bản | 1.1 | 1.2 | Cập nhật sau QC Re-Audit Round 2. |
| 2026-05-07 | 1.2 | Kiến trúc | Read-only 100% khi API | Mode A/B auto-detect, dòng API Disabled, user thêm manual | QC Audit — sửa API deadlock. |
| 2026-05-07 | 1.2 | Bảng | Dynamic (không giới hạn) | Dynamic — max 500 dòng | QC Audit — giới hạn dòng. |
| 2026-05-07 | 1.2 | Quốc tịch | Dropdown ISO | ISO 3166-1 + auto-filter | QC Audit — UX. |
| 2026-05-07 | 1.2 | Cột (3) | Integer > 0 | Thêm error message cụ thể | QC Audit — error msg. |
| 2026-05-07 | 1.2 | Xóa dòng | Mỗi dòng | Chỉ manual, popup [Đồng ý]/[Hủy] | QC Audit — API protection. |
| 2026-05-07 | 1.2 | Xử lý | 2 chế độ cơ bản | A-F (Mode detect, Mode A, Mode B, Partial, Cross-validate 10a/10b, Validate) | QC Audit — viết lại. |
| 2026-05-07 | 1.2 | AC | AC1-AC6 | AC1-AC14 (thêm Mode detect, ISO, max, empty, partial, cross-validate, concurrent) | QC Audit — bổ sung AC. |
| 2026-05-07 | 1.2 | NFR | Performance, Security | Thêm Concurrency | QC Audit — concurrent edit. |
| 2026-05-11 | 1.0→1.1 | Quy tắc sinh mã báo cáo | `DTNN_A4_10a_[ID]` | `FDI_AIV10A_[ID]` | Chuẩn hóa prefix và mã theo appendices.md v2.0 (INS-10) |
| 2026-05-11 | +1 | Label Trạng thái kỳ | `Trạng thái (cấp kỳ)` | `Trạng thái kỳ` | Chuẩn hóa tên label (INS-06) |
| 2026-05-11 | +1 | Kiểu field Năm báo cáo | `Number` | `Yearpicker` | Đồng nhất kiểu field (INS-04) |
| 2026-05-11 | 1.2 → 1.3 | Toast T05 (Mode A fallback) | Nội dung toast tự viết | Tham chiếu CMR_12 (T05 chuẩn) | QC Feedback — chuẩn hóa toast. |
| 2026-05-11 | 1.2 → 1.3 | Mục D (API Partial Failure) | Có mục + AC11 + toast warning | Xóa — không có cơ chế phát hiện data thiếu/đủ | QC Feedback — logic không khả thi. |
| 2026-05-11 | 1.2 → 1.3 | AC | AC1-AC14 (có AC11 API Partial) | AC1-AC13 (bỏ AC11, đánh lại số) | QC Feedback — đồng bộ với xóa mục D. |
| 2026-05-11 | 1.2 → 1.3 | AC12 + NFR Concurrency | Optimistic locking — conflict + refresh | Last Write Wins theo CMR_02 — thao tác sau ghi đè, cả 2 ghi Lifecycle Log | QC Feedback — đồng bộ CMR_02, CF_06. |
| 2026-05-14 | 1.3 → 1.4 | Dòng API | Disabled (không sửa, không xóa), có tag "API" | Editable (cho sửa, cho xóa), bỏ tag "API" | Client feedback — user chịu trách nhiệm cuối cùng. |
| 2026-05-14 | 1.4 | API Logic | Giấy phép còn hiệu lực (chung) | Chỉ tính lao động FDI có giấy phép còn hạn tới ngày cuối cùng của năm báo cáo | Client feedback — clarify API logic. |
| 2026-05-14 | 1.4 | Sort | Không có | Icon sort C3. Mặc định: C3 Descending (max → min) | Client feedback — thêm sort. |
| 2026-05-14 | 1.4 | AC | AC1-AC13 | AC1-AC15 (thêm AC6 API Logic, AC12 Sort, sửa AC5 Editable, AC11 Xóa tất cả dòng) | Viết lại AC. |
| 2026-05-14 | 1.4 → 1.5 | Năm báo cáo (form Lập) | Editable, validate 4 chữ số | Disabled — hiển thị năm đã chọn từ màn danh sách | QC Review — năm đã chọn ở màn danh sách, không cần nhập lại. |
| 2026-05-14 | 1.5 | Cross-validate 10a/10b | Mục E + AC13: Warning khi tổng 10a ≠ 10b | Xóa — hệ thống cho phép nộp nhiều bản, không xác định được bản nào đúng để compare | QC Review — logic không khả thi. |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (2 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-21 | 1.5 → 1.6 | Filter Dropdown default (C3, C4) | Giá trị mặc định: Null | Giá trị mặc định: "Tất cả". Thêm option "Tất cả" đầu danh sách | Đồng bộ CMR_16 |
| 2026-05-21 | 1.5 → 1.6 | Xóa dòng — bỏ popup (C1) | Popup xác nhận [Đồng ý] / [Hủy] | Xóa ngay lập tức, không hiển thị popup xác nhận | Đồng bộ CMR_15 |
| 2026-05-21 | 1.5 → 1.6 | Xóa dòng — ẩn khi 1 dòng (C2) | Hiển thị trên tất cả dòng | Chỉ hiển thị khi bảng có ≥ 2 dòng. Khi còn 1 dòng → ẩn nút | Đồng bộ CMR_15 |
| 2026-05-21 | 1.5 → 1.6 | Cột (3) — placeholder + max length (C5) | Không có placeholder, không có max length | Placeholder: "Nhập tổng số lao động". Max length: 18 ký tự | Đồng bộ CMR_05 |
| 2026-05-21 | 1.5 → 1.6 | Cột (2) — placeholder + error msg (C6) | Không có placeholder, không có error message chuẩn | Placeholder: "Chọn quốc tịch". Lỗi bắt buộc: "Vui lòng chọn quốc tịch" | Đồng bộ CMR_07 |
| 2026-05-21 | 1.5 → 1.6 | eForm Grid error display (C7) | Lỗi inline text bên dưới trường | Viền đỏ quanh ô + tooltip chứa message lỗi khi hover (eForm Grid rule) | Đồng bộ CMR_05/06/07 v2.4 |
| 2026-05-21 | 1.5 → 1.6 | Nút [+ Thêm dòng] vị trí (C8) | Không ghi rõ vị trí | Hiển thị ở footer bảng (bên dưới dòng cuối cùng) | Đồng bộ CMR_15 |
| 2026-05-21 | 1.5 → 1.6 | Năm báo cáo — tham chiếu | Tham chiếu: CMR_05 | Tham chiếu: CS_01 Mục 2 (Yearpicker không phải Numeric) | Fix tham chiếu sai |
| 2026-05-21 | 1.6 → 1.7 | Danh sách kỳ hạn — sort + scroll (G3, G7) | "sắp xếp giảm dần" (không rõ tiêu chí), không có scroll rule | Sắp xếp giảm dần theo năm kỳ hạn. Bổ sung scroll rule: max 10 bản ghi/kỳ, scroll nếu vượt. Tham chiếu: CS_01 Mục 4 | QC Audit v5 |
| 2026-05-21 | 1.6 → 1.7 | Cột (2) Quốc tịch — kiểu dropdown (G6) | "Dropdown có auto-filter" | Searchable Single-Choice Dropdown (CMR_07.1 + CMR_06 Live Search) | QC Audit v5 — xác nhận kiểu dropdown |
| 2026-05-21 | 1.6 → 1.7 | Nút [Xem trước] — trạng thái (G8) | Chỉ ghi "Tham chiếu: CF_07.1" | Bổ sung Disabled/Enabled rule: Disabled khi chưa Lưu nháp, Enabled sau khi Lưu nháp/Nộp. Tham chiếu: CF_01 | QC Audit v5 |
| 2026-05-21 | 1.6 → 1.7 | Mode A/B — loading state + dirty baseline (G1, G9) | Không có loading state, không có dirty baseline rule | Bổ sung: spinner khi chờ API (≤ 5s). Dữ liệu auto-fill = baseline, form KHÔNG dirty sau auto-fill | QC Audit v5 |
| 2026-05-21 | 1.6 → 1.7 | Nhập từ file — đặc tả dynamic rows (G2) | Không có mô tả import đặc thù | Bổ sung mục E: template 2 cột, validate unique quốc tịch, max 500 dòng, cột > 0 | QC Audit v5 |
| 2026-05-21 | 1.6 → 1.7 | Phân quyền UC137-142.3 (G5) | "Người tạo" | "Bộ Nội vụ (Cục Việc làm)" — ghi rõ role cụ thể | QC Audit v5 |
