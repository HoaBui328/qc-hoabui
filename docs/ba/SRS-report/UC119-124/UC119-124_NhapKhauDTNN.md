# UC119-124: Báo cáo tình hình nhập khẩu của tổ chức kinh tế có vốn đầu tư nước ngoài năm ...... (Mẫu A.IV.8c)

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | yen.le2 |
| **Phân hệ** | Quản lý đầu tư nước ngoài vào Việt Nam |
| **Mẫu biểu** | Mẫu A.IV.8c |
| **Loại báo cáo** | Định kỳ năm |
| **Phạm vi báo cáo**           | Không có phạm vi                                              |
| **Hình thức nộp** | Báo cáo đơn lẻ (Single report form) |
| **Cơ quan nhận** | Cục Đầu tư nước ngoài, Bộ Tài chính |
| **Đối tượng lập** | Cục Hải quan / Bộ Tài chính |
| **Giao diện** | Admin site |
| **Ngày tạo** | 2026-04-24 |
| **Phiên bản** | 1.6 |
| **Quy tắc sinh mã báo cáo** | FDI_AIV8C_[ID] |
| **Loại quy trình** | Quy trình 3 bước, CMCĐT_BCTK_09 |

> **Lưu ý kiến trúc:** Mẫu A.IV.8c là báo cáo chi tiết nhập khẩu theo từng doanh nghiệp FDI. Dữ liệu từ mẫu này là nguồn tổng hợp nhập khẩu cho Mẫu A.IV.8a (UC107-112) — hệ thống SUM giá trị nhập khẩu theo tỉnh để điền vào cột Nhập khẩu của Mẫu 8a.

---

## UC119-124.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo tình hình nhập khẩu của TCKT có vốn ĐTNN (Mẫu A.IV.8c)
- Chức năng cho phép Cục Hải quan / Bộ Tài chính truy cập danh sách báo cáo định kỳ năm, được nhóm theo từng Kỳ hạn báo cáo. Mỗi đơn vị chỉ thấy báo cáo do đơn vị mình lập. Mục tiêu: Hỗ trợ nộp báo cáo nhập khẩu trực tuyến, làm nguồn dữ liệu tổng hợp cho Mẫu 8a.
- Out of scope: Không cho phép nộp báo cáo trễ hạn. Việc duyệt báo cáo được thực hiện ở một UC riêng biệt.

Phân quyền: Cục Hải quan / Bộ Tài chính. **Chỉ người tạo (Owner) báo cáo mới được sửa/nộp/xóa báo cáo đó. User khác cùng cơ quan chỉ được Xem.**

**Tiền điều kiện (Preconditions):**
- Tài khoản người dùng có quyền lập/xem báo cáo thuộc đơn vị Cục Hải quan / Bộ Tài chính.
- Kỳ báo cáo đang ở trạng thái "Trong thời hạn".

**Hậu điều kiện (Postconditions):**
- Sau khi Nộp báo cáo thành công, hệ thống gửi thông báo (Notification) cho đơn vị cấp trên (Cục ĐTNN), trạng thái chuyển sang "Chờ duyệt", ghi Audit log.
- Các thao tác Thêm, Sửa, Xóa đều được hệ thống ghi nhận lịch sử (Audit log).
- **Khi kỳ báo cáo chuyển sang "Qua kỳ":** Báo cáo đang ở trạng thái "Lưu nháp" bị khóa — không cho phép sửa hoặc nộp, chỉ cho phép Xem và Xóa.

Truy cập chức năng: Phân hệ Báo cáo → Quản lý ĐTNN vào VN → Báo cáo nhập khẩu TCKT có vốn ĐTNN (Mẫu A.IV.8c)

Chức năng đáp ứng usecase số: 119, 120, 121, 122, 123, 124

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện: **Periodic-single** — Báo cáo có kỳ hạn năm, gửi lẻ từng đơn vị.

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | | |
| 1 | Năm | Yearpicker | Năm hiện tại | x | | Người dùng chọn năm; hệ thống lọc và nhóm danh sách theo năm. Kết quả hiển thị ngay lập tức. Tham chiếu: CMR_07. |
| 2 | Trạng thái kỳ | Multiple-selection Dropdown | Tất cả | x | | Lọc theo trạng thái kỳ hạn: Tất cả / Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Kết quả hiển thị ngay. Tham chiếu: CMR_04, CMR_07., CMR_16 |
| 3 | Trạng thái báo cáo | Multiple-selection Dropdown | Tất cả | x | | Người dùng chọn một hoặc nhiều giá trị: Tất cả / Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07., CMR_16 |
| 4 | Mã báo cáo | Search bar | Null | x | | Tìm theo mã báo cáo. Kết quả hiển thị ngay khi nhập. Nếu không tìm thấy: hiển thị "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| **Khung Danh sách Kỳ hạn** | | | | | | |
| 5 | Kỳ hạn báo cáo | Label | Null | | | Hiển thị tên kỳ hạn (VD: "Năm 2026"). Mặc định collapse; click để expand. Tham chiếu: CMR_08. |
| 6 | Trạng thái kỳ | Label | Null | | | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| 7 | Lập báo cáo | Button | Null | | | Hiển thị trong header mỗi kỳ. Chỉ hiển thị khi Trong thời hạn. Ẩn khi Chưa tới hạn hoặc đã Qua kỳ báo cáo. Tham chiếu: CF_01. |
| 8 | Nhập từ file | Button | Null | | | Hiển thị trong header mỗi kỳ. Chỉ hiển thị khi Trong thời hạn. Ẩn khi Chưa tới hạn hoặc đã Qua kỳ báo cáo. |
| **Khung Danh sách Báo cáo** (trong mỗi kỳ) | | | | | | |
| 9 | Mã báo cáo | Label | Null | | | Mã do hệ thống sinh. Tham chiếu: CMR_09. |
| 10 | Ngày cập nhật | Label | Null | | | Định dạng: dd/MM/yyyy HH:mm. |
| 11 | Trạng thái báo cáo | Label | Null | | | Tham chiếu: CMR_03. |
| 12 | Hành động | Button group | Null | | | Chi tiết tham chiếu: UC119-124.3. |

---

### 3. Mô tả các xử lý của chức năng

- Hệ thống nhóm danh sách theo Kỳ hạn báo cáo (năm), mặc định collapse. Người dùng click để expand từng kỳ.
- Sắp xếp kỳ hạn giảm dần (mới nhất lên đầu). Báo cáo trong mỗi kỳ sắp xếp mới → cũ.
- Các nút [Lập báo cáo] và [Nhập từ file] bị ẩn với kỳ chưa bắt đầu (Chưa tới hạn) và kỳ đã qua (Qua kỳ báo cáo). Tham chiếu: CF_01.
- Mỗi đơn vị chỉ thấy báo cáo của đơn vị mình. Tham chiếu: CMR_02.
- Phân trang. Tham chiếu: CMR_10.

---


## UC119-124.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Lập mới báo cáo tình hình nhập khẩu của TCKT có vốn ĐTNN (Mẫu A.IV.8c)
- Chức năng cho phép Cục Hải quan / Bộ Tài chính nhập liệu tình hình nhập khẩu theo từng doanh nghiệp FDI. Bảng dữ liệu hỗ trợ 2 chế độ:
  - **Mode A (Thủ công)** — Kích hoạt khi API Tổng cục Hải quan KHÔNG khả dụng (auto-detect). User nhập tay. Khi nhập MST hợp lệ → gọi API CSDL Đăng ký KD auto-fill C3, C4, C5.
  - **Mode B (API Hải quan)** — Kích hoạt khi API Tổng cục Hải quan khả dụng (auto-detect). Hệ thống tự auto-fill toàn bộ dòng. Dữ liệu auto-fill vẫn cho phép user chỉnh sửa. User vẫn được thêm dòng manual bổ sung.
  - **Cơ chế chuyển đổi:** Auto-detect dựa trên kết nối API, **không có toggle/switch trên UI**.

Phân quyền: Cục Hải quan / Bộ Tài chính. **Chỉ người tạo (Owner) mới được sửa/nộp/xóa.**

Truy cập chức năng: Màn danh sách báo cáo (UC119-124.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 119, 120

---

### 2. Mô tả giao diện

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **PHẦN HEADER** | | | | | | |
| 1 | Năm báo cáo | Yearpicker | Năm hiện tại | | x | Hiển thị năm báo cáo đã chọn từ màn danh sách. **Disabled** — không cho sửa. Tham chiếu: CMR_05. |
| **BẢNG DỮ LIỆU — DANH SÁCH DOANH NGHIỆP NHẬP KHẨU (Dynamic Table — max 500 dòng)** | | | | | | |
| C1 | STT | Integer | Auto-fill | | | Hệ thống tự động điền số thứ tự tăng dần từ 1. Cập nhật lại (re-index) sau mỗi lần thêm/xóa dòng. Read-only. |
| C2 | Mã số thuế của doanh nghiệp | Text | Null | x | x | User nhập MST. Validate định dạng: **10 hoặc 13 chữ số**. Sai số lượng → lỗi inline "Mã số thuế phải có 10 hoặc 13 chữ số". Validate trùng: nếu có → lỗi inline "Mã số thuế này đã được nhập ở dòng [STT]". MST hợp lệ → gọi API CSDL Đăng ký KD auto-fill C3, C4, C5. **Mode B:** Auto-fill, vẫn cho phép chỉnh sửa. Tham chiếu: CMR_05, CMR_06. |
| C3 | Ngày cấp | Date | Từ CSDL Đăng ký KD | x | x | Auto-fill nếu tìm thấy trong CSDL; không tìm thấy → Enabled nhập tay. **Mode B:** Auto-fill, vẫn cho phép chỉnh sửa. Validate ≤ ngày hiện tại. dd/MM/yyyy. Tham chiếu: CMR_05, CMR_12. |
| C4 | Tên doanh nghiệp | Text | Từ CSDL Đăng ký KD | x | x | Auto-fill hoặc Enabled nhập tay. **Mode B:** Auto-fill, vẫn cho phép chỉnh sửa. Tham chiếu: CMR_06, CMR_12. |
| C5 | Tỉnh/Thành phố | Dropdown | Từ CSDL Đăng ký KD | x | x | Auto-fill hoặc Enabled (danh mục 63 tỉnh/TP). **Mode B:** Auto-fill, vẫn cho phép chỉnh sửa. Tham chiếu: CMR_07, CMR_12. |
| C6 | Nhập khẩu kỳ báo cáo (USD) | Decimal | Null | x | x | **Decimal precision: tối đa 5 chữ số thập phân.** Validate ≥ 0; cấm số âm. **Mode B:** Auto-fill từ SUM tờ khai, vẫn cho phép chỉnh sửa. Tham chiếu: CMR_05. |
| **DÒNG TỔNG CỘNG** | | | | | | |
| T1 | Tổng cộng — Nhập khẩu (USD) | Tính toán | Auto | | | Read-only. Bằng SUM tất cả giá trị cột C6. **Decimal: tối đa 5 chữ số thập phân.** Cập nhật real-time mỗi khi người dùng nhập/sửa C6 hoặc thêm/xóa dòng. |
| **FOOTER** | | | | | | |
| F1 | Nơi lập báo cáo | Text | Auto-fill | | | Hệ thống tự động điền tên Tỉnh/Thành phố theo địa chỉ trụ sở của Cục Hải quan đang đăng nhập. Disabled. Tham chiếu: CMR_12. |
| F2 | Ngày, tháng, năm | Date | Auto-fill | | | Hệ thống tự động điền ngày hiện tại (Current System Date). Cập nhật real-time. Disabled. Tham chiếu: CMR_12. |
| **CÁC BUTTON THAO TÁC BẢNG** | | | | | | |
| B1 | Thêm dòng | Button | | | | Thêm 1 dòng mới vào cuối bảng. STT tự động tăng. Max 500 dòng; vượt → Toast T16 *"Vượt quá số dòng tối đa cho phép (500)"*. |
| B2 | Xóa dòng | Icon Button (mỗi dòng) | | | | Chỉ hiển thị khi bảng có **≥ 2 dòng** (1 dòng → ẩn). Nhấn → xóa ngay lập tức, không hiển thị popup xác nhận. STT re-index. Tham chiếu: CMR_15. |
| **CÁC BUTTON HÀNH ĐỘNG CHÍNH** | | | | | | |
| B3 | Lưu nháp | Button | | | | Lưu toàn bộ dữ liệu ở trạng thái Lưu nháp. **Luôn Enabled** (validate on tap). Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]"), CMR_18. |
| B4 | Nộp báo cáo | Button | | | | Validate toàn bộ trường bắt buộc và ràng buộc logic trước khi nộp. **Luôn Enabled** (validate on tap). **Empty table:** 0 dòng → Toast T15 *"Vui lòng nhập ít nhất 1 dòng dữ liệu"*, chặn nộp. Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"), CMR_18. |
| B5 | Hủy | Button | | | | Quay về màn hình Danh sách. Popup xác nhận nếu có dữ liệu chưa lưu. Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]"), CMR_14, CMR_18. |
| B6 | Xem trước | Button | | | | Disabled khi chưa Lưu nháp lần nào. Enabled sau khi đã Lưu nháp. Mở popup PDF Preview. Tham chiếu: CF_01. |

---

### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu CF_01 (Lập báo cáo), CMR_18.

**Xử lý đặc thù Mẫu A.IV.8c:**

A. Cơ chế chuyển đổi Mode A/B (Auto-detect):
- Khi mở form [Lập báo cáo] → hệ thống gọi health-check API Tổng cục Hải quan.
- API OK → **Mode B** kích hoạt (auto-fill toàn bộ dòng FDI).
- API Fail/Timeout → **Mode A** kích hoạt + Toast T05. Tham chiếu: CMR_12. Enable toàn bộ form.
- **Không có toggle/switch trên UI**.

B. Mode A — Nhập tay (Không có API Hải quan):
- Người dùng nhấn [Thêm dòng] để thêm từng doanh nghiệp.
- Nhập MST vào C2; hệ thống validate định dạng (10 hoặc 13 số) **on-blur + debounce 500ms** (sửa MST trong 500ms → cancel API call cũ).
- Validate trùng trong bảng on-blur.
- Nếu MST hợp lệ → hệ thống gọi API CSDL Đăng ký KD: tìm thấy → auto-fill C3, C4, C5 và Disabled các trường này; không tìm thấy → C3, C4, C5 Enabled cho nhập tay. Tham chiếu: CMR_12.
- Người dùng nhập giá trị nhập khẩu vào C6 (tối đa 5 chữ số thập phân, ≥ 0).
- Dòng Tổng cộng cập nhật real-time theo SUM(C6).

C. Mode B — API Tổng cục Hải quan:
- Hệ thống quét toàn bộ tờ khai nhập khẩu đã thông quan trong kỳ báo cáo.
- Logic lọc: Chỉ lấy tờ khai có MST thuộc danh sách doanh nghiệp FDI.
- Tính toán: SUM giá trị nhập khẩu theo từng MST → điền tự động C2, C3, C4, C5, C6.
- **Dữ liệu auto-fill vẫn cho phép user chỉnh sửa** — user chịu trách nhiệm cuối cùng về tính chính xác.
- **User vẫn được thêm dòng manual bổ sung** (DN FDI chưa có trong API) qua [Thêm dòng]. Hành vi như Mode A.
- Tất cả dòng đều có icon Xóa.
- Dòng Tổng cộng SUM(C6) toàn bộ dòng.

E. Validate khi Nộp:
- Validate tất cả trường bắt buộc (C2, C3, C4, C5, C6) trên toàn bộ dòng trong bảng.
- **Validate bảng không trống:** Nếu 0 dòng → Toast T15 *"Vui lòng nhập ít nhất 1 dòng dữ liệu"*, chặn nộp.
- Nếu thiếu → lỗi inline màu đỏ "Vui lòng nhập [tên trường]" tại từng ô vi phạm. Dừng luồng, không nộp.
- Tham chiếu: CF_01.

F. Liên kết với Mẫu 8a (UC107-112):
- Sau khi bản ghi được lưu nháp hoặc đã nộp, dữ liệu C5 (Tỉnh/TP) và C6 (Nhập khẩu) sẵn sàng để Mẫu 8a đọc và tổng hợp.
- **Cơ chế:** Manual — user Mẫu 8a nhấn [Tổng hợp] → query 8c đã Nộp, Group By tỉnh, SUM C6. **Không auto real-time.** 8c sửa sau → 8a KHÔNG tự cập nhật.
- **Snapshot:** Khi 8a nhấn [Tổng hợp], hệ thống lưu lại timestamp tổng hợp và mã báo cáo 8c đã sử dụng, hiển thị trên form 8a để user biết data lấy từ thời điểm nào.
- Tham chiếu: UC107-112.2.

G. MST trùng giữa 8b và 8c:
- **Cho phép** — 1 DN FDI có thể vừa XK vừa NK. Không cần warning.

- Xuất báo cáo: Kết xuất file Excel. Tham chiếu: CF_04.

**Sort (Sắp xếp dòng trong bảng):**

- Cột C3 (Ngày cấp) và C6 (Nhập khẩu kỳ báo cáo) có **icon sort** trên header.
- Click icon → toggle: Ascending ↑ / Descending ↓.
  - Cột ngày (C3): xa nhất → gần nhất / gần nhất → xa nhất.
  - Cột số (C6): max → min / min → max.
- **Mặc định sort:** Theo C6 (Nhập khẩu) Descending (max → min).
- Dòng mới thêm vào cuối bảng, user tự sort lại nếu muốn.
- Sort persist khi Lưu nháp → mở lại giữ nguyên thứ tự.
- Mode B (API): hệ thống auto-sort theo default sort trước khi render.
- Dòng Tổng cộng luôn ở cuối bảng, không tham gia sort.

---


## UC119-124.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ – Xem chi tiết, Xem vòng đời, In, Xuất báo cáo, Nộp, Chỉnh sửa
- Cho phép người dùng thực hiện tác vụ tương ứng trạng thái bản ghi.

Phân quyền: Kiểm soát theo trạng thái bản ghi. **Chỉ người tạo (Owner) mới được thực hiện Nộp, Chỉnh sửa, Xóa. User khác cùng cơ quan chỉ được Xem chi tiết, Xem vòng đời, In, Xuất báo cáo.** Tham chiếu: CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC119-124.1) → Cột Hành động

Chức năng đáp ứng usecase số: 121, 122, 123, 124

---

### 2. Mô tả giao diện

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Chỉ khi Lưu nháp hoặc Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_09. Tham chiếu: CF_01. |
| 2 | Chỉnh sửa | Button | Chỉ khi Lưu nháp hoặc Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Tất cả người dùng | Màn hình xem toàn trang, toàn bộ trường Disabled. Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Tất cả người dùng | Popup Audit Trail. Tham chiếu: CF_06. |
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

## 3.4 Acceptance Criteria (Tiêu chí nghiệm thu)

- **AC1 Validate MST:** Người dùng nhập MST, nếu sai định dạng (không phải 10 hoặc 13 số) → Báo lỗi inline "Mã số thuế phải có 10 hoặc 13 chữ số". Nếu nhập MST đã tồn tại trong bảng → Báo lỗi inline: "Mã số thuế này đã được nhập ở dòng [STT]". Validate on-blur + debounce 500ms.
- **AC2 Auto-fill CSDL:** Nhập MST hợp lệ và không trùng → Hệ thống tự động gọi API CSDL Đăng ký KD và điền thông tin vào cột Ngày cấp, Tên doanh nghiệp, Tỉnh/Thành phố. Các cột này bị Disabled.
- **AC3 Nhập tay (Fallback):** Nếu không tìm thấy MST trong CSDL Đăng ký KD → Các cột Ngày cấp, Tên, Tỉnh được Enabled để người dùng tự nhập tay.
- **AC4 Mode Detect:** Khi mở form [Lập báo cáo], hệ thống gọi health-check API Tổng cục Hải quan. API OK → Mode B kích hoạt (auto-fill). API Fail/Timeout → Mode A kích hoạt + Toast T05. Không có toggle/switch trên UI.
- **AC5 API Hải quan (Mode B):** Hệ thống quét tất cả tờ khai nhập khẩu trong kỳ theo danh sách MST FDI, tự động SUM tiền nhập khẩu theo từng MST và đổ vào bảng. Dữ liệu auto-fill vẫn cho phép user chỉnh sửa. User vẫn được thêm dòng manual bổ sung.
- **AC6 Editable:** Tất cả dòng (bao gồm dòng auto-fill từ API) đều cho phép chỉnh sửa và xóa. Không phân biệt visual giữa dòng API và dòng manual.
- **AC7 Tính tổng:** Cột "Tổng cộng — Nhập khẩu (USD)" luôn cập nhật real-time bằng SUM(C6) toàn bộ dòng, mỗi khi thêm/xóa/sửa dòng. Decimal: tối đa 5 chữ số thập phân.
- **AC8 Validate bắt buộc:** Khi nhấn "Nộp báo cáo", nếu bất kỳ ô nào thuộc các cột bắt buộc (C2, C3, C4, C5, C6) bị bỏ trống → Hệ thống báo lỗi inline "Vui lòng nhập [tên trường]" và chặn luồng nộp.
- **AC9 Max dòng:** Bảng tối đa 500 dòng. Vượt quá → Toast T16 *"Vượt quá số dòng tối đa cho phép (500)"*.
- **AC10 Empty table:** Nếu bảng có 0 dòng khi nhấn [Nộp báo cáo] → Toast T15 *"Vui lòng nhập ít nhất 1 dòng dữ liệu"*, chặn nộp.
- **AC11 Decimal precision:** Cột C6 (Nhập khẩu USD): tối đa 5 chữ số thập phân. Validate ≥ 0.
- **AC12 Sort:** Cột C3 (Ngày cấp) và C6 (Nhập khẩu) có icon sort trên header. Click → toggle Ascending ↑ / Descending ↓. Mặc định sort theo C6 Descending (max → min). Dòng Tổng cộng luôn ở cuối, không tham gia sort.
- **AC13 API Fail (Toast T05):** Nếu API Hải quan không khả dụng → Toast T05 (Tham chiếu: CMR_12) + Enable toàn bộ form.
- **AC14 Concurrent Edit:** Last Write Wins — khi 2 user cùng lưu/nộp cùng lúc, thao tác sau ghi đè thao tác trước. Cả 2 thao tác được ghi vào Lifecycle Log. Tham chiếu: CF_06.
- **AC15 Nộp thành công:** Khi tất cả validate pass và nhấn [Nộp báo cáo] → trạng thái chuyển sang "Chờ duyệt", hệ thống gửi Notification cho Cục ĐTNN, ghi Audit log (Actor, Action, Timestamp). Tham chiếu: CF_01, CF_09.

---

## 3.5 Non-Functional Requirements (Yêu cầu phi chức năng)

- **Performance:** Khi gọi API CSDL Đăng ký KD hoặc API Tổng cục Hải quan, thời gian phản hồi tối đa là 5 giây. Nếu quá 5 giây (timeout), hệ thống hiển thị Toast T05 (Tham chiếu: CMR_12) và cho phép nhập tay.
- **Security & Audit:** Chỉ người dùng thuộc Cục Hải quan / Bộ Tài chính mới thấy và lập báo cáo. Mọi thao tác lưu, xóa, nộp đều được ghi Audit log (Actor, Action, Timestamp).
- **Concurrency:** Áp dụng Last Write Wins — khi 2 user cùng lưu/nộp cùng lúc, thao tác sau ghi đè thao tác trước. Cả 2 thao tác đều được ghi vào Lifecycle Log (Actor, Action, Timestamp). Tham chiếu: CMR_02, CF_06.

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-06 | 1.0 → 1.1 | Thông tin chung | (Không có) | Thêm Mục tiêu, Phạm vi, Tiền kiện, Hậu kiện. | Chuẩn hóa tài liệu theo QC Audit. |
| 2026-05-06 | 1.0 → 1.1 | Tiêu chí nghiệm thu | (Không có) | Bổ sung 6 AC chi tiết cho luồng nhập liệu. | Chuẩn hóa tài liệu theo QC Audit. |
| 2026-05-06 | 1.0 → 1.1 | Yêu cầu phi chức năng | (Không có) | Bổ sung NFR (Performance, Security). | Chuẩn hóa tài liệu theo QC Audit. |
| 2026-05-07 | 1.1 → 2.0 | Phiên bản | 1.1 | 2.0 | Cập nhật sau QC Re-Audit Round 2. |
| 2026-05-07 | 2.0 | UC119-124.2 Mô tả | (Mô tả chung) | Bổ sung Mode A/B (auto-detect API Hải quan), cơ chế chuyển đổi, debounce 500ms | QC Audit — làm rõ Mode A/B. |
| 2026-05-07 | 2.0 | Bảng dữ liệu | (Không có max) | Dynamic Table — max 500 dòng | QC Audit — giới hạn dòng. |
| 2026-05-07 | 2.0 | C2 MST | Validate on-blur | Validate on-blur + debounce 500ms, phân biệt Mode A/B | QC Audit — debounce + mode behavior. |
| 2026-05-07 | 2.0 | C3, C4, C5 | (Chung) | Phân biệt Mode A (auto-fill/Enabled) vs Mode B (Disabled) | QC Audit — API row locking. |
| 2026-05-07 | 2.0 | C6 | (Chung) | Decimal 2dp round half up, Mode B = Disabled | QC Audit — decimal precision + mode. |
| 2026-05-07 | 2.0 | B2 Xóa dòng | Mỗi dòng | Chỉ dòng manual, dòng API không có icon Xóa | QC Audit — API row protection. |
| 2026-05-07 | 2.0 | B4 Nộp | (Chung) | Bổ sung empty table rule (0 dòng → chặn nộp) | QC Audit — edge case. |
| 2026-05-07 | 2.0 | Xử lý đặc thù | (Chung) | Viết lại hoàn toàn: A-G (Mode detect, Mode A, Mode B, Partial failure, Validate, 8c→8a link, MST cross-report) | QC Audit — chi tiết hóa logic. |
| 2026-05-07 | 2.0 | AC | AC1-AC6 | AC1-AC14 (thêm Mode detect, API rows, max rows, empty table, decimal, partial failure, concurrent edit) | QC Audit — bổ sung AC. |
| 2026-05-07 | 2.0 | NFR | Performance, Security | Thêm Concurrency (optimistic locking) | QC Audit — concurrent edit. |
| 2026-05-11 | 1.0→1.1 | Quy tắc sinh mã báo cáo | `DTNN_A4_8C_[ID]` | `FDI_AIV8C_[ID]` | Chuẩn hóa prefix và mã theo appendices.md v2.0 (INS-10) |
| 2026-05-11 | +1 | Kiểu field Năm báo cáo | `Number` | `Yearpicker` | Đồng nhất kiểu field (INS-04) |
| 2026-05-11 | 1.2 → 1.3 | Toast T05 (Mode A fallback) | Nội dung toast tự viết | Tham chiếu CMR_12 (T05 chuẩn) | QC Feedback — chuẩn hóa toast. |
| 2026-05-11 | 1.2 → 1.3 | Mục D (API Partial Failure) | Có mục + AC12 + toast warning | Xóa — không có cơ chế phát hiện data thiếu/đủ | QC Feedback — logic không khả thi. |
| 2026-05-11 | 1.2 → 1.3 | AC | AC1-AC14 (có AC12 API Partial) | AC1-AC13 (bỏ AC12, đánh lại số) | QC Feedback — đồng bộ với xóa mục D. |
| 2026-05-11 | 1.2 → 1.3 | AC13 + NFR Concurrency | Optimistic locking — conflict + refresh | Last Write Wins theo CMR_02 — thao tác sau ghi đè, cả 2 ghi Lifecycle Log | QC Feedback — đồng bộ CMR_02, CF_06. |
| 2026-05-14 | 1.3 → 1.4 | C2 MST validate | 10 hoặc 14 chữ số | 10 hoặc 13 chữ số | Client feedback — chuẩn hóa MST. |
| 2026-05-14 | 1.4 | C6 Decimal | 2 chữ số thập phân, round half up | Tối đa 5 chữ số thập phân, validate ≥ 0 | Client feedback. |
| 2026-05-14 | 1.4 | Dòng API | Disabled toàn bộ (C2-C6), có tag "API", không cho xóa | Editable (cho sửa, cho xóa), bỏ tag "API" | Client feedback — user chịu trách nhiệm cuối cùng. |
| 2026-05-14 | 1.4 | Sort | Không có | Icon sort C3 (Ngày cấp), C6 (Nhập khẩu); mặc định C6 Descending (max → min) | Client feedback. |
| 2026-05-14 | 1.4 | AC | AC1-AC13 (dòng API Disabled, 2dp) | AC1-AC14 (Editable, 5dp, sort, bỏ tag) | Viết lại AC. |
| 2026-05-14 | 1.4 → 1.5 | Năm báo cáo (form Lập) | Editable, validate 4 chữ số | Disabled — hiển thị năm đã chọn từ màn danh sách | QC Review — năm đã chọn ở màn danh sách, không cần nhập lại. |
| 2026-05-14 | 1.5 | C2 MST mô tả | "Validate on-blur + debounce 500ms (sửa MST trong 500ms → cancel API call cũ)" | Xóa mô tả kỹ thuật debounce — chỉ giữ validate định dạng + trùng + auto-fill | QC Review — bỏ chi tiết implementation. |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (2 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | STD-02 Required message trong AC logic | Truong bat buoc | Vui long nhap [ten truong] | Dong bo CMR v2.0 |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-22 | 1.5 → 1.6 | Phân quyền Owner | Tham chiếu CMR_02 chung | Chỉ Owner (người tạo) được sửa/nộp/xóa; user khác chỉ Xem | QC Audit — đồng bộ với UC113-118 |
| 2026-05-22 | 1.5 → 1.6 | Hậu điều kiện — Qua kỳ | Không đề cập hành vi Lưu nháp khi Qua kỳ | Báo cáo Lưu nháp khi kỳ Qua hạn → khóa, chỉ Xem và Xóa | QC Audit — đồng bộ với UC113-118 |
| 2026-05-22 | 1.5 → 1.6 | Link 8c→8a Snapshot | Không lưu thông tin snapshot | Lưu timestamp + mã báo cáo 8c đã dùng khi 8a tổng hợp | QC Audit — đồng bộ với UC113-118 |
| 2026-05-22 | 1.5 → 1.6 | B6 Xem trước | Không có | Bổ sung nút [Xem trước] theo CF_01. Disabled khi chưa Lưu nháp | QC Audit Q3 |
| 2026-05-22 | 1.5 → 1.6 | C2 MST error message | Lỗi inline chung | Bổ sung verbatim: "Mã số thuế phải có 10 hoặc 13 chữ số" | QC Audit Q4 |
| 2026-05-22 | 1.5 → 1.6 | B2 Xóa dòng | Popup xác nhận, hiển thị tất cả dòng | Xóa ngay không popup, chỉ hiển thị khi ≥ 2 dòng. Tham chiếu CMR_15 | QC Audit Q1-Q2 |
| 2026-05-22 | 1.5 → 1.6 | B1 Hủy → B5 | Button ID trùng B1 | Đánh lại: B5 Hủy. Bổ sung CMR_14, CMR_18 | QC Audit — fix numbering |
| 2026-05-22 | 1.5 → 1.6 | AC | AC1-AC14 | Bổ sung AC15 (Nộp thành công). AC1 bổ sung verbatim MST error | QC Audit |
| 2026-05-22 | 1.6 | Giá trị mặc định bộ lọc | Null (Trạng thái kỳ, Trạng thái báo cáo) | Tất cả + thêm option "Tất cả" vào danh sách giá trị | Tuân thủ CMR_16 — filter dropdown mặc định "Tất cả". |
