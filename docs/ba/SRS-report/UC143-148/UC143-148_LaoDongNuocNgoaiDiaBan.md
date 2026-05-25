# UC143-148: Báo cáo tổng hợp tình hình lao động nước ngoài làm việc tại các TCKT có vốn ĐTNN năm ...... (theo địa bàn tỉnh/thành phố) — Mẫu A.IV.10b

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | yen.le2 |
| **Phân hệ** | Quản lý đầu tư nước ngoài vào Việt Nam |
| **Mẫu biểu** | Mẫu A.IV.10b |
| **Loại báo cáo** | Định kỳ năm |
| **Phạm vi báo cáo**           | Không có phạm vi                                              |
| **Hình thức nộp** | Báo cáo đơn lẻ (Single report form) |
| **Cơ quan nhận** | Bộ Kế hoạch và Đầu tư (Cục Đầu tư nước ngoài) |
| **Đối tượng lập** | Bộ Lao động, Thương binh và Xã hội (Cục Việc làm) |
| **Giao diện** | Admin site |
| **Ngày tạo** | 2026-04-24 |
| **Phiên bản** | 1.8 |
| **Quy tắc sinh mã báo cáo** | FDI_AIV10B_[ID] |
| **Loại quy trình** | Quy trình 3 bước, CMCĐT_BCTK_09 |

> **Lưu ý kiến trúc:** Mẫu A.IV.10b là eForm Grid **Fixed 34 Rows** — bảng cố định 34 dòng tương ứng 34 tỉnh/thành phố theo danh mục hành chính sáp nhập mới. Không cho phép thêm/xóa dòng. Hệ thống hỗ trợ 2 chế độ vận hành:
> - **Mode A (Thủ công)** — Kích hoạt khi API Cục Việc làm KHÔNG khả dụng (auto-detect). Bảng hiển thị 34 dòng với cột số liệu trống, người dùng tự nhập số lao động.
> - **Mode B (API Cục Việc làm)** — Kích hoạt khi API khả dụng (auto-detect). Hệ thống auto-fill dữ liệu vào các dòng tương ứng. **Tất cả dữ liệu vẫn Editable** — user có thể hiệu chỉnh sau khi API điền.
> - **Cơ chế chuyển đổi:** Auto-detect, **không có toggle/switch trên UI**.

---

## UC143-148.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo tổng hợp lao động nước ngoài theo địa bàn tỉnh/TP (Mẫu A.IV.10b)
- Chức năng cho phép Bộ Lao động, Thương binh và Xã hội (Cục Việc làm) truy cập danh sách báo cáo định kỳ năm, được nhóm theo từng Kỳ hạn báo cáo. Mục tiêu: Tổng hợp số lượng lao động nước ngoài làm việc tại các doanh nghiệp FDI theo địa bàn tỉnh/thành phố để làm căn cứ quản lý lao động.
- Out of scope: Không cho phép nộp báo cáo trễ hạn. Việc duyệt báo cáo được thực hiện ở một UC riêng biệt.

Phân quyền: Chỉ người dùng thuộc Bộ Lao động, Thương binh và Xã hội (Cục Việc làm) mới có quyền truy cập. **Phân quyền Owner:** Chỉ người tạo báo cáo mới được thực hiện Sửa / Nộp / Xóa. Người dùng khác cùng đơn vị chỉ có quyền Xem chi tiết, Xem vòng đời, In, Xuất báo cáo. Không áp dụng CMR_01/CMR_02.

**Tiền điều kiện (Preconditions):**
- Tài khoản người dùng có quyền lập/xem báo cáo thuộc đơn vị Bộ Lao động, Thương binh và Xã hội (Cục Việc làm).
- Kỳ báo cáo đang ở trạng thái "Trong thời hạn".

**Hậu điều kiện (Postconditions):**
- Sau khi Nộp báo cáo thành công, hệ thống gửi thông báo (Notification) cho đơn vị cấp trên (Cục ĐTNN).
- Các thao tác Thêm, Sửa, Xóa đều được hệ thống ghi nhận lịch sử (Audit log).
- **Phân quyền Owner:** Chỉ người tạo báo cáo mới được thực hiện Sửa / Nộp / Xóa. Người dùng khác cùng đơn vị chỉ có quyền Xem chi tiết, Xem vòng đời, In, Xuất báo cáo.
- **Kỳ chuyển "Qua kỳ":** Báo cáo ở trạng thái Lưu nháp bị khóa — không cho sửa/nộp, chỉ cho phép Xem và Xóa.

Truy cập chức năng: Phân hệ Báo cáo → Quản lý ĐTNN vào VN → Báo cáo tổng hợp lao động nước ngoài theo địa bàn (Mẫu A.IV.10b)

Chức năng đáp ứng usecase số: 143, 144, 145, 146, 147, 148

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
| 10 | Địa bàn | Label | Null | | | Tỉnh/TP của cơ quan lập báo cáo. |
| 11 | Ngày cập nhật | Label | Null | | | Định dạng: dd/MM/yyyy HH:mm. |
| 12 | Trạng thái báo cáo | Label | Null | | | Tham chiếu: CMR_03. |
| 13 | Hành động | Button group | Null | | | Chi tiết tham chiếu: UC143-148.3. |

---

### 3. Mô tả các xử lý của chức năng

- Hệ thống nhóm theo Kỳ hạn năm. Mặc định collapse; sắp xếp giảm dần theo năm kỳ hạn (năm mới nhất ở trên). Tham chiếu: CMR_10, CS_01 Mục 4.
- Hiển thị tối đa 10 bản ghi trong mỗi kỳ hạn. Nếu vượt quá 10 bản ghi → kích hoạt thanh cuộn dọc (Scroll) bên trong kỳ hạn đó. Tham chiếu: CS_01 Mục 4.
- Tất cả bộ lọc hiển thị kết quả ngay lập tức. Tham chiếu: CMR_07.
- Nút [Lập báo cáo] và [Nhập từ file] chỉ hiển thị khi kỳ ở trạng thái **Trong thời hạn**. Tham chiếu: CF_01, CMR_04.

---


## UC143-148.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Tạo mới báo cáo tổng hợp lao động nước ngoài theo địa bàn tỉnh/TP (Mẫu A.IV.10b)
- Chức năng cho phép nhập liệu theo biểu mẫu A.IV.10b. Báo cáo là eForm Grid **Fixed 34 Rows** — bảng cố định 34 dòng tương ứng 34 tỉnh/thành phố theo danh mục hành chính sáp nhập mới, 1 cột số liệu. Bảng dữ liệu hỗ trợ 2 chế độ:
  - **Mode A (Thủ công)** — Kích hoạt khi API Cục Việc làm KHÔNG khả dụng (auto-detect). Bảng hiển thị 34 dòng với cột số liệu trống, user tự nhập.
  - **Mode B (API Cục Việc làm)** — Kích hoạt khi API khả dụng (auto-detect). Hệ thống auto-fill dữ liệu vào các dòng tương ứng. **Tất cả dữ liệu vẫn Editable** — user có thể hiệu chỉnh.
  - **Cơ chế chuyển đổi:** Auto-detect, **không có toggle/switch trên UI**.
  - Tham chiếu: CF_01.

Phân quyền: Bộ Lao động, Thương binh và Xã hội (Cục Việc làm). Chỉ người tạo (Owner) mới được sửa/nộp/xóa. Không áp dụng CMR_01/CMR_02.

Truy cập chức năng: Màn danh sách báo cáo (UC143-148.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 143, 144

---

### 2. Mô tả giao diện

**Giao diện thêm mới**

Giao diện: Màn hình tạo mới theo biểu mẫu A.IV.10b.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **PHẦN HEADER** | | | | | | |
| 1 | Năm báo cáo | Yearpicker | Năm hiện tại | | x | Hiển thị năm báo cáo đã chọn từ màn danh sách. **Disabled** — không cho sửa. Tham chiếu: CS_01 Mục 2. |
| **BẢNG DỮ LIỆU — FIXED 34 ROWS** | | | | | | Bảng cố định 34 dòng tương ứng 34 tỉnh/thành phố theo danh mục hành chính sáp nhập mới. Không cho phép thêm/xóa dòng. |
| Cột (1) | STT | Integer | Auto | | | Hệ thống tự đánh số 1-34. Disabled. |
| Cột (2) | Tỉnh/Thành phố | Label | Auto | | x | Hiển thị tên 34 tỉnh/TP theo danh mục hành chính sáp nhập mới. **Disabled** — không cho sửa. Sắp xếp theo mã đơn vị hành chính. |
| Cột (3) | Tổng số lao động ở thời điểm báo cáo | Integer | Null | x | x | Integer ≥ 0. Max length: 18 ký tự. Max value: 999.999.999. Placeholder: *"Nhập tổng số lao động"*. Trường bắt buộc bỏ trống — lỗi: *"Vui lòng nhập tổng số lao động"*. Nhập số âm — lỗi: *"Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy"*. **Mode B:** Auto-fill từ API, vẫn **Editable**. Hiển thị lỗi trong eForm Grid: viền đỏ quanh ô + tooltip chứa message lỗi khi hover. Tham chiếu: CMR_05. |
| **DÒNG TỔNG CỘNG** | | | | | | Dòng cuối bảng. Disabled. |
| — | Tổng cộng | Auto-calc | — | | | SUM cột (3) toàn bộ dòng. Cập nhật real-time. Read-only. |
| **PHẦN FOOTER** | | | | | | |
| — | Nơi lập báo cáo | Text/Label | Auto | | | Disabled. Hệ thống tự điền tên tỉnh/TP theo địa chỉ trụ sở cơ quan đăng nhập. Không cho sửa. |
| — | Ngày, tháng, năm lập báo cáo | Date/Label | Auto | | | Disabled. Hệ thống tự điền ngày hiện tại (Current System Date). Định dạng: dd/MM/yyyy. Không cho sửa. |
| **Các Button** | | | | | | |
|  | | — | Hủy | Button | | | | **Luôn Enabled.** Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]"), CMR_14. |
|  | | - | Xem trước | Button | | | | Mở popup PDF Preview báo cáo. **Disabled** khi báo cáo chưa được Lưu nháp lần nào (tooltip: *"Vui lòng Lưu nháp hoặc Nộp báo cáo trước khi xem preview"*). **Enabled** sau khi Lưu nháp/Nộp thành công ít nhất 1 lần. Tham chiếu: CF_01 (Xem trước), CF_07.1. |
|  | | — | Lưu nháp | Button | | | | **Luôn Enabled.** Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]"). |
|  | | — | Nộp báo cáo | Button | | | | **Luôn Enabled.** Validate toàn bộ trước khi nộp. Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |

---

### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu: CF_01 (Lập báo cáo), CF_04 (Xuất báo cáo), CF_05 (In). Tham chiếu CMR_18: Tab key điều hướng giữa các ô cột (3) theo thứ tự dòng 1→34. Shift+Tab di chuyển ngược. Tab ở ô cuối cùng (dòng 34) → focus đến nút [Lưu nháp].

**Xử lý đặc thù Mẫu A.IV.10b:**

A. Cơ chế chuyển đổi Mode A/B (Auto-detect):
- Khi mở form [Lập báo cáo] → hệ thống gọi health-check API Hệ thống Giấy phép lao động (Cục Việc làm).
- **Loading state:** Trong khoảng chờ API (≤ 5s), hệ thống hiển thị loading indicator (spinner) trên vùng bảng dữ liệu. Các nút hành động (Lưu nháp, Nộp, Hủy) vẫn hiển thị nhưng vùng bảng ở trạng thái chờ.
- API OK → **Mode B** kích hoạt (auto-fill dữ liệu vào các dòng tương ứng, tất cả vẫn Editable).
- API Fail/Timeout (> 5s) → **Mode A** kích hoạt + Toast T05. Tham chiếu: CMR_12. Bảng hiển thị 34 dòng với cột số liệu trống.
- **Không có toggle/switch trên UI**. Không chuyển Mode giữa phiên.
- **Baseline dirty form (Mode B):** Dữ liệu auto-fill từ API Mode B được coi là giá trị khởi tạo (baseline) — form KHÔNG dirty sau auto-fill. Dirty Form Guard (CMR_14) chỉ kích hoạt khi user thay đổi giá trị so với baseline này.

B. Mode A — Nhập tay (Manual Mode):
- Bảng hiển thị cố định 34 dòng. Cột Tỉnh/TP đã điền sẵn (Disabled).
- Người dùng nhập trực tiếp cột (3) cho từng dòng.
- Validate cột (3) ≥ 0, integer. Max value: 999.999.999. Max length: 18 ký tự.
- **Hiển thị lỗi eForm Grid:** Do không gian hạn chế trong ô lưới, lỗi hiển thị dạng **viền đỏ** quanh ô; hover vào ô hiển thị **tooltip** chứa message lỗi tương ứng. Tham chiếu: CMR_05.
- Dòng Tổng cộng cập nhật real-time.

C. Mode B — API Cục Việc làm:
- Truy vấn danh sách lao động nước ngoài làm việc tại các tổ chức FDI trong kỳ đã chọn, **có giấy phép lao động còn thời hạn tới ngày cuối cùng của năm báo cáo** → đối chiếu MST với danh sách DN FDI → Group By Tỉnh/TP → COUNT.
- Auto-fill cột (3) vào dòng tương ứng.
- **Tất cả dữ liệu vẫn Editable** — user có thể hiệu chỉnh giá trị sau khi API điền. User chịu trách nhiệm cuối cùng về tính chính xác.
- Tỉnh/TP không có dữ liệu từ API → cột (3) để trống, user tự nhập nếu cần.
- Dòng Tổng SUM(Cột 3) toàn bộ dòng.

D. Sort:
- Cột hỗ trợ sort: C3 (Tổng số lao động).
- Icon sort hiển thị trên header cột C3. Click icon → toggle: Ascending ↑ / Descending ↓.
- **Mặc định sort:** C3 Descending (max → min).
- Dòng Tổng luôn ở cuối bảng, không tham gia sort.
- Sort persist khi Lưu nháp → mở lại giữ nguyên thứ tự.
- Mode B: hệ thống auto-sort theo default sort (C3 Descending) trước khi render.

F. Validate khi Nộp:
- Tất cả cột (3) đã điền đầy đủ và hợp lệ. Cột (3) ≥ 0, integer, max 999.999.999.
- Vi phạm → viền đỏ quanh ô + tooltip chứa message lỗi (eForm Grid rule), dừng luồng. Tham chiếu: CF_01, CMR_05.
- Nộp thành công → trạng thái "Chờ duyệt".

G. Nhập từ file: CF_02 — **Case 2** (không có Phạm vi). .xlsx only, max 10MB.
- Template gồm 34 dòng tỉnh/TP (pre-filled theo danh mục hành chính sáp nhập mới) + 1 cột số liệu "Tổng số lao động".
- Validate khi import: File phải có đúng 34 dòng. Tên tỉnh/TP phải khớp danh mục hành chính. Cột số liệu ≥ 0, integer.
- Nếu file không đúng 34 dòng → Alert: *"Cấu trúc file không đúng định dạng template. Vui lòng sử dụng file template đã tải."*

H. Chỉnh sửa (Edit Mode B):
- Khi mở Chỉnh sửa bản ghi đã lưu, hệ thống **KHÔNG gọi lại API** — hiển thị dữ liệu đã lưu (snapshot). User tự chỉnh sửa nếu cần cập nhật.
- Tham chiếu: CF_03.

- Xuất báo cáo: Kết xuất file **Excel**. Tham chiếu: CF_04.

---


## UC143-148.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ — Xem chi tiết, Xem vòng đời, In, Kết xuất, Nộp, Chỉnh sửa
- Chức năng cho phép người dùng thực hiện các tác vụ bổ trợ tương ứng trạng thái bản ghi.

Phân quyền: Kiểm soát theo trạng thái bản ghi. Chỉ người tạo (Owner) mới được Nộp/Chỉnh sửa/Xóa. Tham chiếu: CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC143-148.1) → Cột Hành động → Chọn tác vụ tương ứng

Chức năng đáp ứng usecase số: 145, 146, 147, 148

---

### 2. Mô tả giao diện

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Chỉ Lưu nháp và Yêu cầu chỉnh sửa | Người tạo (Owner) | Tham chiếu: CF_09. Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |
| 2 | Chỉnh sửa | Button | Chỉ Lưu nháp và Yêu cầu chỉnh sửa | Người tạo (Owner) | Tham chiếu: CF_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Tất cả người dùng | Kết xuất file Excel. Tham chiếu: CF_04. |
| 7 | Xóa | Button | Lưu nháp **VÀ** chưa từng nộp | Người tạo (Owner) | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết: Tham chiếu: CF_07.
- Xem vòng đời: Tham chiếu: CF_06.
- In báo cáo: Tham chiếu: CF_05.
- Xuất báo cáo: Kết xuất ra file **Excel**. Tham chiếu: CF_04.
- Chỉnh sửa báo cáo: Tham chiếu: CF_03.

---

## 3.4 Acceptance Criteria (Tiêu chí nghiệm thu)

- **AC1 Fixed 34 Rows:** Khi vào màn hình "Lập báo cáo", bảng luôn hiển thị cố định 34 dòng tương ứng 34 tỉnh/TP theo danh mục hành chính sáp nhập mới. Không cho phép thêm/xóa dòng.
- **AC2 Mode Detect:** Mở form → health-check API Cục Việc làm. OK → Mode B (auto-fill, Editable). Fail → Mode A (bảng 34 dòng trống) + Toast T05. Tham chiếu: CMR_12.
- **AC3 API Cục Việc làm (Mode B):** Auto-fill cột (3) cho các dòng tỉnh/TP có dữ liệu. Tất cả dữ liệu vẫn Editable — user có thể hiệu chỉnh.
- **AC4 API Logic:** Chỉ tính số lao động nước ngoài làm việc tại các tổ chức FDI trong kỳ đã chọn, có giấy phép lao động còn thời hạn tới ngày cuối cùng của năm báo cáo.
- **AC5 Tỉnh/TP Disabled:** Cột Tỉnh/TP = Label, Disabled. User không thể sửa tên tỉnh/TP.
- **AC6 Validate số:** Cột (3) ≥ 0, integer. Max 999.999.999.
- **AC7 SUM Real-time:** Dòng Tổng cập nhật real-time SUM(Cột 3). Integer.
- **AC8 Footer tự động:** Nơi lập, Ngày tháng Disabled, auto-fill.
- **AC9 Sort:** Icon sort hiển thị trên header C3. Click → toggle Ascending/Descending. Mặc định: C3 Descending (max → min). Dòng Tổng luôn ở cuối. Sort persist khi Lưu nháp.
- **AC10 Concurrent Edit:** Last Write Wins — khi 2 user cùng lưu/nộp cùng lúc, thao tác sau ghi đè thao tác trước. Cả 2 thao tác đều được ghi vào Lifecycle Log. Tham chiếu: CF_06.
- **AC11 Nộp thành công:** Tất cả validate pass → Click [Nộp báo cáo] → Trạng thái chuyển "Chờ duyệt", Notification gửi Cục ĐTNN, Audit log ghi nhận.

---

## 3.5 Non-Functional Requirements (Yêu cầu phi chức năng)

- **Performance:** Thời gian gọi API Cục Việc làm và render Grid 34 dòng không quá 5 giây. Nếu quá 5s → Toast T05 + Mode A. Tham chiếu: CMR_12.
- **Security & Audit:** Chỉ Bộ Lao động, Thương binh và Xã hội (Cục Việc làm) mới có quyền lập báo cáo. Chỉ người tạo (Owner) mới được sửa/nộp/xóa. Mọi hành động đều được ghi Audit log đầy đủ (Actor, Action, Timestamp). Tham chiếu: CF_06.
- **Concurrency:** Áp dụng Last Write Wins — khi 2 user cùng mở chỉnh sửa và cùng lưu/nộp cùng lúc, thao tác sau ghi đè thao tác trước. Cả 2 thao tác đều được ghi vào Lifecycle Log (Actor, Action, Timestamp) để truy vết. Tham chiếu: CF_06.
- **Maxlength:**

| Loại trường | Max Length | Áp dụng |
|---|---|---|
| Number (Integer) | 18 ký tự (max 999.999.999) | Cột (3) |
| Search | 255 ký tự | Search bar (#4) |

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-07 | 1.0 → 1.1 | Thông tin chung | (Không có) | Thêm Mục tiêu, Phạm vi, Tiền kiện, Hậu kiện. | Chuẩn hóa tài liệu theo QC Audit. |
| 2026-05-07 | 1.0 → 1.1 | Tiêu chí nghiệm thu | (Không có) | Bổ sung 6 AC chi tiết cho luồng lao động theo địa bàn. | Chuẩn hóa tài liệu theo QC Audit. |
| 2026-05-07 | 1.0 → 1.1 | Yêu cầu phi chức năng | (Không có) | Bổ sung NFR (Performance, Security). | Chuẩn hóa tài liệu theo QC Audit. |
| 2026-05-07 | 1.1 → 1.2 | Phiên bản | 1.1 | 1.2 | Cập nhật sau QC Re-Audit Round 2. |
| 2026-05-07 | 1.2 | Kiến trúc | Read-only 100% khi API | Mode A/B auto-detect — Mode B: ô fill Disabled / ô null Enabled; Mode A: Enabled toàn bộ | QC Audit — sửa API deadlock. |
| 2026-05-07 | 1.2 | Bảng dữ liệu | 63 dòng cố định | 63 dòng + max value 999.999.999 + sắp theo mã đơn vị hành chính | QC Audit — chi tiết hóa. |
| 2026-05-07 | 1.2 | Xử lý | 2 chế độ cơ bản | A-H (Mode detect, Mode A, Mode B, API Partial, All zeros valid, Validate, Nhập từ file, Listing filter) | QC Audit — viết lại. |
| 2026-05-07 | 1.2 | AC | AC1-AC6 | AC1-AC13 (Mode detect, API partial, all zeros, nhập từ file, concurrent) | QC Audit — bổ sung AC. |
| 2026-05-07 | 1.2 | NFR | Performance, Security | Thêm Concurrency | QC Audit — concurrent edit. |
| 2026-05-11 | 1.2 → 1.3 | Toast Mode A | Nội dung toast tự viết | Tham chiếu CMR_12 (T05 chuẩn) | QC Feedback — chuẩn hóa toast. |
| 2026-05-11 | 1.2 → 1.3 | Mục D (API Partial Failure) | Có mục D riêng + Toast warning | Xóa — không có cơ chế phát hiện data thiếu/đủ | QC Feedback — logic không khả thi. |
| 2026-05-11 | 1.2 → 1.3 | AC | AC1-AC13 (có AC5 API Partial) | AC1-AC12 (bỏ AC5, đánh lại số) | QC Feedback — đồng bộ với xóa mục D. | | `DTNN_A4_10b_[ID]` | `FDI_AIV10B_[ID]` | Chuẩn hóa prefix và mã theo appendices.md v2.0 (INS-10) |
| 2026-05-11 | +1 | Label Trạng thái kỳ | `Trạng thái (cấp kỳ)` | `Trạng thái kỳ` | Chuẩn hóa tên label (INS-06) |
| 2026-05-11 | +1 | Kiểu field Năm báo cáo | `Number` | `Yearpicker` | Đồng nhất kiểu field (INS-04) |
| 2026-05-11 | 1.3 | AC11 + NFR Concurrency | "Optimistic locking" (không mô tả chi tiết) | Áp dụng Last Write Wins theo CMR_02 — thao tác sau ghi đè, cả 2 ghi Lifecycle Log | QC Feedback 51.3 — đồng bộ CMR_02. |
| 2026-05-12 | 1.3 → 1.4 | Kiến trúc | Cố định 63 dòng, Mode B ô-level Disabled/Enabled | Dynamic Rows — Mode B chỉ sinh dòng có dữ liệu, dòng API Disabled toàn bộ, user thêm manual | Client confirm: chỉ tỉnh có số thì báo cáo. |
| 2026-05-12 | 1.4 | Bảng dữ liệu | 63 dòng cố định, Tỉnh/TP = Text/Label | Dynamic Rows, Tỉnh/TP = Dropdown auto-filter, thêm [+ Thêm dòng] + Xóa dòng | Đồng bộ kiến trúc Dynamic Rows. |
| 2026-05-12 | 1.4 | Xử lý Mode A | Load sẵn 63 dòng, user nhập cột (3) | Bảng trống, user thêm dòng + chọn Tỉnh/TP từ dropdown | Dynamic Rows. |
| 2026-05-12 | 1.4 | Xử lý Mode B | Auto-fill 63 dòng, ô fill Disabled / ô null Enabled | Auto-generate N dòng (chỉ tỉnh có data), dòng API Disabled toàn bộ, user thêm manual | Dynamic Rows. |
| 2026-05-12 | 1.4 | Mục D (All 63 = 0) | Edge case cho phép nộp + Warning | Xóa — không còn 63 dòng cố định | Dynamic Rows — validate ≥ 1 dòng thay thế. |
| 2026-05-12 | 1.4 | Nhập từ file | Template pre-fill 63 dòng; ≠ 63 → lỗi | Bỏ ràng buộc 63 dòng | Dynamic Rows. |
| 2026-05-12 | 1.4 | AC | AC1-AC12 (fixed 63 rows) | AC1-AC14 (Dynamic Rows, unique, empty table, xóa dòng, cross-validate) | Viết lại AC cho Dynamic Rows. |
| 2026-05-14 | 1.4 → 1.5 | Kiến trúc bảng | Dynamic Rows — chỉ sinh dòng cho tỉnh/TP có dữ liệu | Fixed 34 Rows — 34 tỉnh/TP theo danh mục sáp nhập mới, không thêm/xóa dòng | Client confirm: chuyển sang 34 tỉnh sáp nhập. |
| 2026-05-14 | 1.5 | Cột Tỉnh/TP | Dropdown (chọn từ 63 tỉnh/TP, unique, auto-filter) | Label (Disabled, pre-filled 34 tỉnh/TP) | Fixed 34 Rows. |
| 2026-05-14 | 1.5 | Dòng API | Disabled (không sửa, không xóa), có tag "API" | Editable (cho sửa), bỏ tag "API" | Client feedback — user chịu trách nhiệm cuối cùng. |
| 2026-05-14 | 1.5 | API Logic | Giấy phép còn hiệu lực (chung) | Chỉ tính lao động FDI có giấy phép còn hạn tới ngày cuối cùng của năm báo cáo | Client feedback — clarify API logic. |
| 2026-05-14 | 1.5 | Sort | Không có | Icon sort C3. Mặc định: C3 Descending (max → min) | Client feedback — thêm sort. |
| 2026-05-14 | 1.5 | Thêm/Xóa dòng | [+ Thêm dòng] + icon Xóa dòng manual | Xóa — bảng cố định 34 dòng | Fixed 34 Rows. |
| 2026-05-14 | 1.5 | AC | AC1-AC14 (Dynamic Rows, unique, empty table, xóa dòng) | AC1-AC12 (Fixed 34, Editable, Sort, API Logic) | Viết lại AC cho Fixed 34 Rows. |
| 2026-05-14 | 1.5 → 1.6 | Filter Địa bàn (danh sách) | Có filter Địa bàn (row #2) | Xóa — báo cáo đơn lẻ, không cần lọc theo địa bàn | QC Review. |
| 2026-05-14 | 1.6 | Năm báo cáo (form Lập) | Editable, validate 4 chữ số | Disabled — hiển thị năm đã chọn từ màn danh sách | QC Review — năm đã chọn ở màn danh sách, không cần nhập lại. |
| 2026-05-14 | 1.6 | Cross-validate 10a/10b | Mục E + AC10: Warning khi tổng 10b ≠ 10a | Xóa — hệ thống cho phép nộp nhiều bản, không xác định được bản nào đúng để compare | QC Review — logic không khả thi. |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (2 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-21 | 1.6 → 1.7 | Filter Dropdown default (C1, C2) | Giá trị mặc định: Null, thiếu option "Tất cả" | Giá trị mặc định: "Tất cả". Thêm option "Tất cả" đầu danh sách | Đồng bộ CMR_16 |
| 2026-05-21 | 1.6 → 1.7 | Cột (3) — placeholder + error msg + eForm Grid (C3, C4) | Không có placeholder, error msg, eForm Grid rule | Placeholder: "Nhập tổng số lao động". Lỗi bắt buộc: "Vui lòng nhập tổng số lao động". Lỗi số âm theo CMR_05. Viền đỏ + tooltip trong eForm Grid | Đồng bộ CMR_05 v2.4 |
| 2026-05-21 | 1.6 → 1.7 | Năm báo cáo — tham chiếu (C5) | Tham chiếu: CMR_05 | Tham chiếu: CS_01 Mục 2 (Yearpicker không phải Numeric) | Fix tham chiếu sai |
| 2026-05-21 | 1.6 → 1.7 | Nút [Xem trước] — trạng thái (C6) | Chỉ ghi "Tham chiếu: CF_07.1" | Bổ sung Disabled/Enabled rule theo CF_01 | QC Audit v4 |
| 2026-05-21 | 1.6 → 1.7 | Mode A/B — loading state + dirty baseline (G1, G2) | Không có loading state, không có dirty baseline | Spinner khi chờ API (≤ 5s). Auto-fill = baseline, form KHÔNG dirty | QC Audit v4 |
| 2026-05-21 | 1.6 → 1.7 | Danh sách kỳ hạn — sort + scroll (G3) | "sắp xếp giảm dần" (không rõ tiêu chí) | Sắp xếp giảm dần theo năm kỳ hạn. Scroll rule: max 10/kỳ. Tham chiếu: CS_01 Mục 4 | QC Audit v4 |
| 2026-05-21 | 1.6 → 1.7 | Phân quyền UC143-148.3 (G4) | "Người tạo" | "Bộ LĐ-TB&XH (Cục Việc làm)" — ghi rõ role cụ thể | QC Audit v4 |
| 2026-05-21 | 1.6 → 1.7 | Validate + eForm Grid error (Mode A) | Không có eForm Grid rule | Bổ sung viền đỏ + tooltip cho lỗi validate trong eForm Grid | Đồng bộ CMR_05 v2.4 |
| 2026-05-21 | 1.6 → 1.7 | Nhập từ file — đặc tả Fixed 34 Rows (G6) | "CF_02 Case 2, .xlsx, max 10MB" (không có validate đặc thù) | Template 34 dòng pre-filled, validate đúng 34 dòng + tên tỉnh/TP khớp danh mục | QC Audit v4 |
| 2026-05-21 | 1.6 → 1.7 | Edit Mode B — data refresh (G7) | Không mô tả | Bổ sung: Không gọi lại API khi Edit, hiển thị snapshot đã lưu | QC Audit v4 |
| 2026-05-22 | 1.7 → 1.8 | Phân quyền Owner | Tham chiếu CMR_02 | Bỏ CMR_02, ghi rõ: chỉ người tạo (Owner) sửa/nộp/xóa, user khác chỉ Xem | QC Audit v5 — Post-BA Answers |
| 2026-05-22 | 1.7 → 1.8 | Hành vi Qua kỳ | Không có | Lưu nháp khi Qua kỳ bị khóa — chỉ Xem và Xóa | QC Audit v5 — Post-BA Answers |
| 2026-05-22 | 1.7 → 1.8 | CMR_18 Tab Navigation | Không có | Bổ sung tham chiếu CMR_18 + thứ tự tab dòng 1→34 | QC Audit v5 — FIX-03 |
| 2026-05-22 | 1.7 → 1.8 | Button state | Không ghi rõ | Lưu nháp/Nộp/Hủy: "Luôn Enabled" — validate khi tap | QC Audit v5 — CMR Button I01 |
| 2026-05-22 | 1.7 → 1.8 | NFR Maxlength | Không có | Bổ sung bảng maxlength: Number=18, Search=255 | QC Audit v5 — FIX-06 |
| 2026-05-22 | 1.7 → 1.8 | Error messages — bỏ dấu "." cuối | Có dấu "." cuối | Bỏ dấu "." cuối câu cuối cùng | QC Audit v5 — FIX-04 |
| 2026-05-22 | 1.7 → 1.8 | AC10 + NFR Concurrency | Tham chiếu CMR_02 | Bỏ CMR_02, chỉ giữ CF_06 | QC Audit v5 — CMR_02 không áp dụng |
| 2026-05-22 | 1.7 → 1.8 | AC11 Nộp thành công | "Trạng thái Chờ duyệt" | Bổ sung Notification Cục ĐTNN + Audit log | QC Audit v5 — Post-BA Answers |
