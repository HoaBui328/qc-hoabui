# UC101-106: Báo cáo tình hình tạm ngừng, chấm dứt hoạt động dự án đầu tư nước ngoài trong lĩnh vực ... Quý ... (Mẫu A.IV.7)

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | yen.le2 |
| **Phân hệ** | Quản lý đầu tư nước ngoài vào Việt Nam |
| **Mẫu biểu** | Mẫu A.IV.7 |
| **Loại báo cáo** | Định kỳ quý |
| **Phạm vi báo cáo**           | Không có phạm vi                                              |
| **Hình thức nộp** | Báo cáo đơn lẻ (Single report form) |
| **Cơ quan nhận** | Bộ Tài chính (Cục Đầu tư nước ngoài) |
| **Đối tượng lập** | Bộ Tư pháp / Bộ Công thương / Ngân hàng Nhà nước VN |
| **Giao diện** | Admin site |
| **Ngày tạo** | 2026-04-23 |
| **Phiên bản** | 1.6 |
| **Quy tắc sinh mã báo cáo** | FDI_AIV7_[ID] |
| **Loại quy trình** | Quy trình 3 bước, CMCĐT_BCTK_09 |

## 1. Thông tin chung
**Mục tiêu (Objective):**
Tính năng giúp các Bộ/Ngành (Bộ Tư pháp, Bộ Công thương, NHNN) báo cáo định kỳ danh sách các dự án ĐTNN bị tạm ngừng hoặc chấm dứt hoạt động thuộc lĩnh vực quản lý của mình. Hỗ trợ hệ thống tích hợp API để tự động lọc và lấy dữ liệu chính xác, giảm thiểu nhập liệu thủ công.

**Phạm vi (Scope):**
- Bao gồm quy trình tạo mới, lưu nháp, nộp và các tác vụ xem/sửa/xóa/xuất báo cáo báo cáo theo Mẫu A.IV.7.
- Out of scope: Không xử lý trường hợp nộp trễ hạn (kỳ hạn đóng sẽ không hiển thị nút Lập/Nhập từ file).

**Tiền điều kiện (Preconditions):**
- Người dùng có tài khoản thuộc tổ chức tương ứng (Bộ Tư pháp/Công thương/NHNN) và có quyền lập báo cáo.
- Kỳ báo cáo đang ở trạng thái "Trong thời hạn".
- **Tối đa 1 bản báo cáo được nộp cho mỗi Bộ/Ngành trong mỗi kỳ.** Nhiều user cùng Bộ có thể tạo mới đồng thời, nhưng user nào lưu trước thì thắng — các user sau khi lưu sẽ nhận thông báo lỗi: "Báo cáo cho kỳ này đã tồn tại."

**Hậu điều kiện (Postconditions):**
- Sau khi Nộp báo cáo thành công, báo cáo chuyển sang trạng thái "Chờ duyệt", hệ thống gửi notification cho Cục ĐTNN.
- Các thao tác Nộp, Chỉnh sửa, Xóa đều được hệ thống ghi nhận lịch sử (Audit log).

> **Lưu ý:** Báo cáo được lập **riêng biệt bởi từng Bộ** (Bộ Tư pháp / Bộ Công thương / Ngân hàng Nhà nước VN). Mỗi Bộ gửi 1 bản độc lập theo lĩnh vực quản lý của mình.

---

## UC101-106.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo tình hình tạm ngừng, chấm dứt hoạt động dự án ĐTNN theo lĩnh vực (Mẫu A.IV.7)
- Chức năng cho phép Bộ Tư pháp / Bộ Công thương / Ngân hàng Nhà nước VN truy cập danh sách báo cáo định kỳ quý, được nhóm theo từng Kỳ hạn báo cáo. Mỗi Bộ chỉ thấy báo cáo do Bộ mình lập.

Phân quyền: Bộ Tư pháp / Bộ Công thương / Ngân hàng Nhà nước VN. Tham chiếu: CMR_02.

Truy cập chức năng: Phân hệ Báo cáo → Quản lý ĐTNN vào VN → Báo cáo tạm ngừng, chấm dứt hoạt động ĐTNN theo lĩnh vực (Mẫu A.IV.7)

Chức năng đáp ứng usecase số: 101, 102, 103, 104, 105, 106

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện: **Periodic-single** — Giao diện mẫu cho báo cáo có kỳ hạn và gửi lẻ từng báo cáo.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | | |
| 1 | Năm | Yearpicker | Năm hiện tại | x | | Người dùng nhấp để chọn năm. Hệ thống lọc và nhóm danh sách theo năm. Kết quả hiển thị ngay, không cần nhấn thêm nút. Tham chiếu: CMR_07. |
| 2 | Trạng thái kỳ | Multiple-selection Dropdown | Tất cả | x | | Lọc theo trạng thái kỳ hạn. Chọn một hoặc nhiều giá trị: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Kết quả hiển thị ngay. Logic filter: AND khi chọn nhiều giá trị đồng thời với các bộ lọc khác. Tham chiếu: CMR_04, CMR_07, CMR_16. |
| 3 | Trạng thái báo cáo | Multiple-selection Dropdown | Tất cả | x | | Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Logic filter: AND khi chọn nhiều giá trị đồng thời với các bộ lọc khác. Tham chiếu: CMR_03, CMR_07, CMR_16. |
| 4 | Mã báo cáo | Search bar | Null | x | | Nhập liệu tự do để tìm theo mã báo cáo. Kết quả hiển thị ngay khi nhập. Nếu không tìm thấy: hiển thị "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| **Khung Danh sách Kỳ hạn** | | | | | | |
| 5 | Kỳ hạn báo cáo | Label | Null | | | Hiển thị tên kỳ hạn (VD: "Quý 1 Năm 2026"). Mặc định collapse; người dùng click để expand. Tham chiếu: CMR_08. |
| 6 | Trạng thái kỳ | Label | Null | | | Trạng thái kỳ hạn: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| 7 | Lập báo cáo | Button | Null | | | Chỉ hiển thị khi kỳ ở trạng thái **Trong thời hạn**. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CF_01, CMR_18, CMR_04. |
| 8 | Nhập từ file | Button | Null | | | Hiển thị trong header của mỗi kỳ. Chỉ hiển thị khi kỳ ở trạng thái **Trong thời hạn**. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| **Khung Danh sách Báo cáo** (trong mỗi kỳ) | | | | | | |
| 9 | Mã báo cáo | Label | Null | | | Hiển thị mã báo cáo do hệ thống sinh. Tham chiếu: CMR_09. |
| 10 | Ngày cập nhật | Label | Null | | | Định dạng: dd/MM/yyyy HH:mm. |
| 11 | Trạng thái báo cáo | Label | Null | | | Tham chiếu: CMR_03. |
| 12 | Hành động | Button group | Null | | | Chi tiết tham chiếu: UC101-106.3. |

---

### 3. Mô tả các xử lý của chức năng

- Hệ thống tự động nhóm danh sách theo Kỳ hạn báo cáo (theo quý), mặc định collapse. Người dùng click để expand từng kỳ.
- Sắp xếp kỳ hạn giảm dần (kỳ mới nhất lên đầu). Báo cáo trong mỗi kỳ sắp xếp mới → cũ.
- Nút [Lập báo cáo] và [Nhập từ file] chỉ hiển thị khi kỳ ở trạng thái **Trong thời hạn**. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CF_01, CMR_18, CMR_04.
- Mỗi Bộ chỉ thấy báo cáo của Bộ mình. Tham chiếu: CMR_02.
- Tất cả bộ lọc hiển thị kết quả ngay lập tức, không cần nhấn thêm nút.
- Phân trang. Tham chiếu: CMR_10.


**CÁC BUTTON**

| #  | Tên           | Kiểu   | Điều kiện hiển thị | Phân quyền       | Mô tả                                                                                |
| -- | -------------- | ------- | ----------------------- | -------------------- | ------------------------------------------------------------------------------------- |
| B1 | Hủy           | Button | Luôn                   | Người tạo         | Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Hủy]").                                     |
| B2 | Xem trước | Button | Luôn                   | Người tạo         | Mở popup PDF Preview báo cáo (không rời màn Lập). Tham chiếu: CF_07.1.        |
| B3 | Lưu nháp     | Button | Luôn                   | Người tạo         | Tham chiếu: CF_01, CMR_18 (mục "Xử lý nút [Lưu nháp]").                                |
| B4 | Nộp báo cáo | Button | Lưu nháp, Yêu cầu CS | Người tạo         | Validate toàn bộ trường bắt buộc trước khi nộp. Tham chiếu: CF_01, CMR_18.         |
---



## UC101-106.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:
- Tên chức năng: Tạo mới báo cáo tình hình tạm ngừng, chấm dứt hoạt động dự án ĐTNN theo lĩnh vực (Mẫu A.IV.7).
- Chức năng cho phép người dùng nhập liệu, hiển thị danh sách các dự án (Phần I: Tạm ngừng, Phần II: Chấm dứt) với sự hỗ trợ auto-fill từ API của các Bộ/Ngành theo điều kiện lọc chung. Bảng dữ liệu hỗ trợ 2 chế độ:
  - **Mode A (Thủ công)** — Kích hoạt khi API Bộ/Ngành KHÔNG khả dụng (auto-detect). User nhập tay toàn bộ.
  - **Mode B (API Bộ/Ngành)** — Kích hoạt khi API khả dụng (auto-detect). Hệ thống tự auto-fill. Tất cả cột vẫn **Editable** — user được phép hiệu chỉnh. User vẫn được thêm dòng manual bổ sung.
  - **Cơ chế chuyển đổi:** Auto-detect dựa trên kết nối API, **không có toggle/switch trên UI**.

Phân quyền: Bộ Tư pháp / Bộ Công thương / Ngân hàng Nhà nước VN. Tham chiếu: CMR_02.

Truy cập chức năng: Màn danh sách báo cáo (UC101-106.1) → Nhấn nút [Lập báo cáo]

### 2. Mô tả giao diện

**Giao diện tạo mới báo cáo (Mẫu A.IV.7)**

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả |
| --- | --- | --- | --- | --- | --- | --- |
| **Phần Header** | | | | | | |
| 1 | Tên Bộ/Ngành | Label | Tự động điền | | | Tự động thay đổi theo Tổ chức của User Login (VD: Ngân hàng Nhà nước, Bộ Tư pháp, Bộ Công thương). |
| 2 | Lĩnh vực báo cáo | Dropdown | Tự động điền | x | x | Tiêu đề "TRONG LĨNH VỰC...". Gợi ý default theo tổ chức của user: Bộ Công thương → "DẦU KHÍ"; Bộ Tư pháp → "CÔNG TY LUẬT"; Ngân hàng Nhà nước VN → "NGÂN HÀNG NƯỚC NGOÀI". User có thể thay đổi. |
| **Bảng Dữ liệu (Áp dụng chung cho Phần I: Tạm ngừng và Phần II: Chấm dứt — Dynamic Table — max 200 dòng/phần)** | | | | | | Hệ thống auto lọc dự án từ API (chỉ lấy dự án đúng lĩnh vực và có Ngày QĐ rơi trọn vẹn vào Quý/Năm kỳ báo cáo đã chọn). Tất cả cột vẫn **Editable** — user được phép hiệu chỉnh dữ liệu API nếu cần. User chịu trách nhiệm cuối cùng về nội dung báo cáo. |
| 3 | STT | Integer | Auto | | | Số thứ tự tăng dần. Cập nhật lại (re-index) sau mỗi lần thêm/xóa dòng. Read-only. |
| 4 | Mã số dự án/ Số GCNĐT/ Số Giấy tờ có giá trị tương đương | Text | Auto-fill / Null | x | x | Nhập tay hoặc Auto-fill API. Text free (không validate format ký tự). Tối đa 255 ký tự. Validate cross-section: Nếu Mã dự án xuất hiện ở cả Phần I và Phần II, Ngày QĐ ở Phần II phải > Ngày QĐ ở Phần I (Lỗi: "Ngày chấm dứt của Dự án [Mã] phải sau Ngày tạm ngừng."). Không được trùng lặp Mã dự án trong cùng 1 Phần (Lỗi: "Dự án [Mã] đã có trong danh sách [Phần] của kỳ báo cáo này."). |
| 5 | Ngày cấp | Datepicker | Auto-fill / Null | x | x | Format DD/MM/YYYY. Auto-fill lấy Ngày chứng nhận lần đầu. Validate: Phải <= Ngày tại Cột 7. |
| 6 | Tên dự án / doanh nghiệp | Text | Auto-fill / Null | x | x | Tối đa 255 ký tự. Auto-fill tên pháp lý hiện tại. |
| 7 | Vốn đầu tư đăng ký (USD) | Decimal | Auto-fill / Null | x | x | **Decimal precision: tối đa 5 chữ số thập phân.** Số thực dương. Format: 1,500,000.00. Lấy vốn từ GCN điều chỉnh gần nhất (nếu có) hoặc GCNĐT gốc. Bắt buộc > 0. |
| 8 | Số QĐ/công văn tạm ngừng/chấm dứt | Text | Auto-fill / Null | x | x | Text free (không validate format ký tự). Tối đa 255 ký tự. Bắt buộc điền. *(Không áp dụng CMR_13 — theo xác nhận client feedback 2026-05-14.)* |
| 9 | Ngày QĐ/công văn tạm ngừng/chấm dứt | Datepicker | Auto-fill / Null | x | x | Format DD/MM/YYYY. Auto-fill từ Ngày ký văn bản. Validate: Phải >= Ngày cấp (Cột 3) VÀ nằm trọn trong khoảng thời gian Quý/Năm của kỳ báo cáo. Lỗi: "Ngày QĐ/Công văn phải nằm trong kỳ báo cáo [Quý X Năm YYYY]." |
| 10 | Ghi chú (nguyên nhân tạm ngừng, chấm dứt hoạt động) | Textarea | Auto-fill / Null | x | | Tối đa 3000 ký tự. Không bắt buộc. Auto-fill nguyên nhân từ CSDL (nếu có). User luôn được phép sửa/gõ tay. Lỗi: "Ghi chú không được vượt quá 3000 ký tự". |
| **Hành động thao tác** | | | | | | |
| 11 | Thêm dòng | Button | | | | Nút ở cuối mỗi Phần (I và II) để thêm dòng trống thủ công. Max 200 dòng/phần; vượt → Toast T16 *"Vượt quá số dòng tối đa cho phép (200)"*. |
| 12 | Xóa dòng | Icon Button (mỗi dòng) | | | | Chỉ hiển thị khi bảng có **≥ 2 dòng** (1 dòng → ẩn). Nhấn → xóa ngay lập tức, không hiển thị popup xác nhận. STT re-index. Tham chiếu: CMR_15. |
| 13 | Lưu nháp | Button | | | | Tham chiếu: CF_01, CMR_18. |
| 14 | Nộp báo cáo | Button | | | | Tham chiếu: CF_01, CMR_18. |
| 15 | Hủy | Button | | | | Tham chiếu: CF_01, CMR_18. |

### 3. Mô tả các xử lý của chức năng

**Điều kiện lọc chung API (Áp dụng khi load báo cáo lần đầu):**
- **Lọc theo thẩm quyền:** Chỉ bốc các dự án thuộc lĩnh vực quản lý chuyên ngành tương ứng với tổ chức của user.
- **Lọc theo kỳ báo cáo:** Chỉ bốc dự án có Ngày ký QĐ tạm ngừng/chấm dứt (Cột 9) rơi trọn vẹn vào Quý/Năm của kỳ báo cáo hiện tại.

**Cơ chế chuyển đổi Mode A/B (Auto-detect):**
- Khi mở form [Lập báo cáo] → hệ thống gọi health-check API Bộ/Ngành.
- API OK → **Mode B** kích hoạt (auto-fill toàn bộ dòng).
- API Fail/Timeout → **Mode A** kích hoạt + Toast T05. Tham chiếu: CMR_12. Enable toàn bộ form.
- **API timeout giữa chừng** (đã fill một số dòng rồi timeout): Giữ nguyên dữ liệu đã fill (không rollback), Toast T05, các dòng còn lại user nhập thủ công.
- **Không có toggle/switch trên UI**.
- **Re-open báo cáo nháp:** Khi mở lại báo cáo đã Lưu nháp, hệ thống **không re-fetch API** — giữ nguyên snapshot dữ liệu đã lưu. User tiếp tục chỉnh sửa trên dữ liệu hiện có.

**Xử lý các dòng dữ liệu:**
- **Dòng auto-fill (Mode B):** Các cột 4-10 tự động điền, tất cả vẫn **Editable** — user được phép hiệu chỉnh nếu cần. User chịu trách nhiệm cuối cùng về nội dung báo cáo.
- **Thêm dòng thủ công:** User bấm "Thêm dòng" để bổ sung dự án chưa kịp có trên API. Các trường ở trạng thái Enabled (nhập tay). Hành vi dòng manual giống Mode A.
- **Quy tắc Vốn (Cột 7 UI):** Ưu tiên lấy từ GCN điều chỉnh gần nhất (theo thời gian); nếu chưa điều chỉnh lấy từ GCNĐT gốc.

**Thay đổi "Lĩnh vực báo cáo" (Dropdown):**
- Khi user thay đổi giá trị Lĩnh vực sau khi API đã fill dữ liệu → hệ thống hiển thị popup xác nhận: "Thay đổi lĩnh vực sẽ xóa toàn bộ dữ liệu đã nhập. Bạn có chắc chắn?" [Đồng ý] / [Hủy].
- [Đồng ý]: Xóa toàn bộ dòng (API + manual) kể cả Ghi chú đã nhập → gọi lại API với lĩnh vực mới.
- [Hủy]: Giữ nguyên lĩnh vực và dữ liệu hiện tại.

**Sort:**
- Các cột có giá trị ngày hoặc số (Cột 5 Ngày cấp, Cột 7 Vốn, Cột 9 Ngày QĐ) có icon sort trên header. Click icon → toggle: Ascending ↑ / Descending ↓.
- **Mặc định sort theo Cột 9 (Ngày QĐ/Công văn): xa nhất → gần nhất (descending).**
- Dòng mới thêm vào cuối bảng, user tự sort lại nếu muốn. Sort persist khi Lưu nháp → mở lại giữ nguyên thứ tự.
- Khi API auto-fill (Mode B), hệ thống auto-sort theo default sort trước khi render.

**Validations (Kiểm tra lỗi):**
  - Ngày cấp <= Ngày QĐ.
  - Ngày QĐ phải nằm trong Quý/Năm báo cáo. Lỗi: "Ngày QĐ/Công văn phải nằm trong kỳ báo cáo [Quý X Năm YYYY]."
  - Cross-section: Nếu Mã dự án có ở cả Phần I (Tạm ngừng) và Phần II (Chấm dứt) -> Ngày QĐ Phần II bắt buộc > Ngày QĐ Phần I. Thông báo lỗi: "Ngày chấm dứt của Dự án [Mã] phải sau Ngày tạm ngừng." **Chỉ validate trong cùng kỳ báo cáo, không validate cross-quarter.**
  - Duplicate: Một dự án không được xuất hiện 2 lần trong cùng Phần I hoặc Phần II. Thông báo lỗi: "Dự án [Mã] đã có trong danh sách Tạm ngừng/Chấm dứt của kỳ báo cáo này."

**Hiển thị lỗi trong bảng nhập liệu (eForm Grid):**
  - Do không gian hạn chế trong ô lưới, lỗi **không** hiển thị dạng text bên dưới trường.
  - Thay vào đó: hiển thị **viền đỏ** quanh ô vi phạm; hover vào ô hiển thị **tooltip** chứa message lỗi tương ứng.
  - Message lỗi giữ nguyên nội dung theo các quy tắc validation ở trên.
  - Tham chiếu: CMR_05, CMR_06, CMR_07 (mục eForm Grid).

**Validate khi Lưu nháp:**
- Chỉ validate T07: "Lưu nháp không thành công - Bạn cần nhập dữ liệu trước khi lưu." (nếu cả 2 Phần đều trống).
- Không validate cross-section, không validate Ngày QĐ trong kỳ khi Lưu nháp.

**Validate khi Nộp:**
- Validate tất cả trường bắt buộc trên toàn bộ dòng.
- **Validate bảng không trống:** Nếu cả Phần I và Phần II đều 0 dòng → Toast T15 *"Vui lòng nhập ít nhất 1 dòng dữ liệu"*, chặn nộp. (Một Phần trống + Phần kia có dữ liệu = cho phép nộp.)
- Validate cross-section và date range.

**Nhập từ file:** Tham chiếu CF_02 — **Case 2** (báo cáo không có Phạm vi). File .xlsx only, max 10MB. Template gồm cả Phần I và Phần II.

---

## UC101-106.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng
Mô tả: Cho phép người dùng thực hiện các tác vụ bổ trợ tương ứng với trạng thái báo cáo (Xem chi tiết, Xem vòng đời, In, Xuất báo cáo, Nộp, Chỉnh sửa, Xóa).
Truy cập: Từ màn hình Danh sách (Cột Hành động).

### 2. Mô tả giao diện
| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Lưu nháp / Yêu cầu chỉnh sửa | Người tạo | Nộp báo cáo cho Cục ĐTNN duyệt. Tham chiếu CF_09, CF_01. |
| 2 | Chỉnh sửa | Button | Lưu nháp / Yêu cầu chỉnh sửa | Người tạo | Mở lại form Lập báo cáo với dữ liệu đã lưu (giữ snapshot, không re-fetch API). Khi ở trạng thái "Yêu cầu chỉnh sửa": user phải sửa ≥1 field trước khi nút Nộp Enabled. Tham chiếu CF_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Tất cả | View read-only. Tham chiếu CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Tất cả | Xem lịch sử thao tác/chuyển trạng thái. Tham chiếu CF_06. |
| 5 | In | Button | Tất cả trạng thái | Tất cả | Tham chiếu CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Tất cả | Kết xuất Excel. Tham chiếu CF_04. |
| 7 | Xóa | Button | Lưu nháp (chưa từng nộp) | Người tạo | Xóa bản ghi nháp. Tham chiếu CF_08. |

---

## 3.4 Acceptance Criteria (Tiêu chí nghiệm thu)

**Nhóm 1: Form & Validation**
- **AC1:** Validate ngày lập (Cột Ngày QĐ): Nhập "Ngày QĐ" nằm ngoài khoảng thời gian Quý/Năm của kỳ báo cáo hiện tại -> Hệ thống chặn nộp và báo lỗi: "Ngày QĐ/Công văn phải nằm trong kỳ báo cáo [Quý X Năm YYYY]."
- **AC2:** Validate logic Phần I & Phần II: Nhập một Mã dự án ở cả 2 phần, điền Ngày QĐ (P.II) <= Ngày QĐ (P.I) -> Hệ thống báo lỗi "Ngày chấm dứt của Dự án [Mã] phải sau Ngày tạm ngừng." Chỉ validate trong cùng kỳ, không cross-quarter.
- **AC3:** Chặn Duplicate: Nhập 2 dòng có cùng Mã dự án trong Phần I -> Hệ thống báo lỗi "Dự án [Mã] đã có trong danh sách Tạm ngừng của kỳ báo cáo này."
- **AC4:** Decimal precision: Vốn đầu tư (USD) = tối đa 5 chữ số thập phân. Validate > 0.

**Nhóm 2: API & Integration**
- **AC5:** Mode Detect: Khi mở form [Lập báo cáo], hệ thống gọi health-check API Bộ/Ngành. API OK → Mode B (auto-fill, tất cả Editable). API Fail → Mode A + Toast T05. Không có toggle/switch.
- **AC6:** Auto-fill API (Mode B): Khi user tạo báo cáo mới, hệ thống tự động bốc các dự án thuộc lĩnh vực tương ứng có ngày QĐ trong quý, điền vào form. Tất cả cột Editable — user được phép hiệu chỉnh.
- **AC7:** Cho phép thêm dòng manual: User nhấn "Thêm dòng" → dòng mới Enabled. Max 200 dòng/phần.
- **AC8:** API Fail (Toast T05): API không khả dụng → Toast T05 (Tham chiếu: CMR_12) + Enable toàn bộ form.
- **AC9:** Sort: Mặc định sort theo Cột 9 (Ngày QĐ) descending. User click icon sort trên header Cột 5/7/9 để toggle. Sort persist khi Lưu nháp.

**Nhóm 3: Lifecycle & Edge Cases**
- **AC9:** Nộp báo cáo: Ở trạng thái "Lưu nháp", nhấn Nộp -> Popup xác nhận, đổi trạng thái sang "Chờ duyệt", gửi thông báo.
- **AC10:** Lưu nháp validate: Chỉ validate T07 (bảng trống = không cho lưu). Không validate cross-section/date range khi lưu nháp.
- **AC11:** Empty table: Cả Phần I và Phần II đều 0 dòng khi nhấn [Nộp] → Toast T15 *"Vui lòng nhập ít nhất 1 dòng dữ liệu"*, chặn nộp. Một Phần trống + Phần kia có dữ liệu = cho phép.
- **AC12:** Xóa dòng: Icon Xóa chỉ hiển thị khi bảng có ≥ 2 dòng. Nhấn → xóa ngay (không popup). STT re-index. Tham chiếu: CMR_15.
- **AC13:** Thay đổi lĩnh vực: Popup xác nhận "Thay đổi lĩnh vực sẽ xóa toàn bộ dữ liệu đã nhập." [Đồng ý] xóa + gọi lại API. [Hủy] giữ nguyên.
- **AC14:** Concurrent Edit: Last Write Wins — khi 2 user cùng lưu/nộp cùng lúc, thao tác sau ghi đè thao tác trước. Cả 2 thao tác được ghi vào Lifecycle Log. Tham chiếu: CMR_02, CF_06.
- **AC15:** Nhập từ file: CF_02 Case 2 (không có Phạm vi). File .xlsx only, max 10MB.

---

## 3.5 Non-Functional Requirements (Yêu cầu phi chức năng)

1. **Hiệu năng (Performance):** 
   - Quá trình gọi API tích hợp từ các cơ quan quản lý chuyên ngành và auto-fill dữ liệu không được vượt quá 5 giây. Nếu quá 5 giây (timeout), hệ thống hiển thị Toast T05 (Tham chiếu: CMR_12) và cho phép nhập tay.
2. **Bảo mật & Dữ liệu (Security):**
   - Mọi thao tác Thêm/Sửa/Xóa và Nộp trên báo cáo phải được ghi log (Actor, Timestamp, Action, Old/New Data) để phục vụ tra soát (Audit log).
   - Chỉ lấy dữ liệu theo đúng phân quyền tổ chức của user đang thao tác (Lọc theo thẩm quyền). Mỗi Bộ/Ngành chỉ thấy báo cáo do đơn vị mình lập.
3. **Concurrency:**
   - Áp dụng Last Write Wins — khi 2 user cùng Bộ/Ngành cùng lưu/nộp cùng lúc, thao tác sau ghi đè thao tác trước. Cả 2 thao tác đều được ghi vào Lifecycle Log (Actor, Action, Timestamp). Tham chiếu: CMR_02, CF_06.

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-06 | 1.0 -> 1.1 | Thông tin chung | (Không có) | Thêm Mục tiêu, Phạm vi, Tiền/Hậu điều kiện | Hoàn thiện tài liệu theo QC Audit |
| 2026-05-06 | 1.0 -> 1.1 | Lập báo cáo | (Không có) | Thêm chương UC101-106.2 (Giao diện và Logic Mẫu A.IV.7) | Hoàn thiện tài liệu theo QC Audit |
| 2026-05-06 | 1.0 -> 1.1 | Các Tác Vụ Bổ Trợ | (Không có) | Thêm chương UC101-106.3 (Nộp, Hủy, In, Xóa...) | Hoàn thiện tài liệu theo QC Audit |
| 2026-05-06 | 1.0 -> 1.1 | Tiêu chí nghiệm thu | (Không có) | Thêm mục 3.4 Acceptance Criteria với 6 ACs | Hoàn thiện tài liệu theo QC Audit |
| 2026-05-06 | 1.0 -> 1.1 | Yêu cầu phi chức năng | (Không có) | Thêm mục 3.5 Non-Functional Requirements | Hoàn thiện tài liệu theo QC Audit |
| 2026-05-07 | 1.1 → 2.0 | Phiên bản | 1.1 | 2.0 | Cập nhật sau QC Re-Audit Round 2. |
| 2026-05-07 | 2.0 | Mô tả UC101-106.2 | (Mô tả chung) | Bổ sung Mode A/B (auto-detect API Bộ/Ngành), cơ chế chuyển đổi | QC Audit — làm rõ Mode A/B. |
| 2026-05-07 | 2.0 | Bảng dữ liệu | (Không có max) | Dynamic Table — max 200 dòng/phần | QC Audit — giới hạn dòng. |
| 2026-05-07 | 2.0 | Cột 4-9 | x* (mô tả chung) | Phân biệt dòng API (Disabled) vs dòng manual (Enabled) | QC Audit — API row locking. |
| 2026-05-07 | 2.0 | Cột 7 Vốn | (Chung) | Decimal 2dp round half up | QC Audit — decimal precision. |
| 2026-05-07 | 2.0 | Cột 8 Số QĐ | (Không có CMR_13) | Bổ sung tham chiếu CMR_13 | QC Audit — format số công văn. |
| 2026-05-07 | 2.0 | Cột 9 Ngày QĐ | (Lỗi chung) | Thêm error message cụ thể | QC Audit — error message. |
| 2026-05-07 | 2.0 | Xóa dòng | Mỗi dòng | Chỉ dòng manual, dòng API không có icon Xóa. Popup [Đồng ý]/[Hủy]. STT re-index. | QC Audit — API row protection. |
| 2026-05-07 | 2.0 | Thay đổi lĩnh vực | (Không mô tả) | Popup xác nhận khi thay đổi, xóa data cũ + gọi lại API | QC Audit — edge case. |
| 2026-05-07 | 2.0 | Validate | (Chung) | Lưu nháp chỉ T07; Nộp validate full + empty table + cross-section. Không cross-quarter. | QC Audit — validate scope. |
| 2026-05-07 | 2.0 | Nhập từ file | (Chung) | CF_02 Case 2, .xlsx only, max 10MB | QC Audit — làm rõ CF_02. |
| 2026-05-07 | 2.0 | AC | AC1-AC6 | AC1-AC16 (thêm Mode detect, API rows, API partial, decimal, empty table, lĩnh vực, concurrent) | QC Audit — bổ sung AC. |
| 2026-05-07 | 2.0 | NFR | Performance, Security | Thêm Concurrency (optimistic locking), phân quyền Bộ/Ngành | QC Audit — concurrent edit. |
| 2026-05-08 | 2.0 → 2.1 | Tên nút Submit | Nộp báo cáo (1 lần) | Nộp báo cáo | Thống nhất tên nút toàn hệ thống |
| 2026-05-11 | 1.0→1.1 | Quy tắc sinh mã báo cáo | `DTNN_A4_7_[ID]` | `FDI_AIV7_[ID]` | Chuẩn hóa prefix và mã theo appendices.md v2.0 (INS-10) |
| 2026-05-11 | 1.2 → 1.3 | Toast T05 (Mode A fallback) | Nội dung toast tự viết | Tham chiếu CMR_12 (T05 chuẩn) | QC Feedback — chuẩn hóa toast. |
| 2026-05-11 | 1.2 → 1.3 | API Partial Failure | Có mục + AC8 + toast warning | Xóa — không có cơ chế phát hiện data thiếu/đủ | QC Feedback — logic không khả thi. |
| 2026-05-11 | 1.2 → 1.3 | AC | AC1-AC16 (có AC8 API Partial) | AC1-AC15 (bỏ AC8, đánh lại số) | QC Feedback — đồng bộ với xóa API Partial. |
| 2026-05-11 | 1.2 → 1.3 | AC15 + NFR Concurrency | Optimistic locking — conflict + refresh | Last Write Wins theo CMR_02 — thao tác sau ghi đè, cả 2 ghi Lifecycle Log | QC Feedback — đồng bộ CMR_02, CF_06. |
| 2026-05-14 | 1.3 → 1.4 | Lĩnh vực mặc định | Bộ Tư pháp: "HÀNH NGHỀ LUẬT SƯ"; Bộ Công thương: "THƯƠNG MẠI/NHƯỢNG QUYỀN THƯƠNG MẠI"; NHNN: "NGÂN HÀNG" | Bộ Công thương: "DẦU KHÍ"; Bộ Tư pháp: "CÔNG TY LUẬT"; NHNN: "NGÂN HÀNG NƯỚC NGOÀI" | Client feedback — cập nhật tên lĩnh vực. |
| 2026-05-14 | 1.4 | C4 (Mã dự án) validation | Tối đa 50 ký tự | Text free (không validate format), max 50 ký tự | Client feedback — nới lỏng format. |
| 2026-05-14 | 1.4 | C7 (Vốn) decimal | 2 chữ số thập phân, round half up | Tối đa 5 chữ số thập phân | Client feedback — tăng precision. |
| 2026-05-14 | 1.4 | C8 (Số QĐ) validation | Max 50 ký tự | Text free (không validate format), max 50 ký tự | Client feedback — nới lỏng format. |
| 2026-05-14 | 1.4 | Dòng API | Disabled (cột 4-9 không sửa, không xóa), có tag "API" | Tất cả Editable, cho xóa, bỏ tag "API" — user chịu trách nhiệm cuối | Client feedback — cho phép hiệu chỉnh dữ liệu API. |
| 2026-05-14 | 1.4 | Sort | Không có | Thêm icon sort cho Cột 5, 7, 9. Mặc định sort Cột 9 descending. Persist khi Lưu nháp | Client feedback — thêm sort. |
| 2026-05-14 | 1.4 | AC | AC5-AC6 (dòng API Disabled), AC12 (chỉ manual xóa) | AC5-AC6 (Editable), AC9 (Sort), AC12 (tất cả xóa) | Đồng bộ với thay đổi API Editable + Sort. |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (2 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them CMR_18 vao tham chieu CF_01 | Tuan thu CMR_18 Tab Navigation tren form nhap lieu |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-21 | 1.4 → 1.5 | Cột 8 (Số QĐ/công văn) | Tham chiếu CMR_13 | Bỏ tham chiếu CMR_13 — Text free, không validate format. Theo xác nhận client feedback. | QC Audit — fix conflict C-01 |
| 2026-05-21 | 1.4 → 1.5 | Xóa dòng (Dòng 12) + AC12 | Hiển thị tất cả dòng, popup xác nhận [Đồng ý]/[Hủy] | Chỉ hiển thị khi ≥ 2 dòng, xóa ngay không popup. Tham chiếu CMR_15. | QC Audit — fix conflict C-02, đồng bộ CMR_15 |
| 2026-05-21 | 1.4 → 1.5 | Thông tin chung — Tham chiếu CMR_02 | "Phạm vi dữ liệu hiển thị theo CMR_02" | Bỏ tham chiếu CMR_02 (không áp dụng cho báo cáo Bộ/Ngành) | QC Audit — fix conflict C-05 |
| 2026-05-21 | 1.4 → 1.5 | Filter Dropdown mặc định (Dòng 2, 3) | Giá trị mặc định: Null | Giá trị mặc định: Tất cả. Tham chiếu CMR_16. | QC Audit — fix gap G-01 |
| 2026-05-21 | 1.4 → 1.5 | Hiển thị lỗi eForm Grid | (Không có) | Bổ sung mục "Hiển thị lỗi trong bảng nhập liệu": viền đỏ + tooltip. Tham chiếu CMR_05/06/07 (eForm Grid). | QC Audit — fix gap G-04 |
| 2026-05-22 | 1.5 → 1.6 | Tiền điều kiện — Giới hạn BC/kỳ | (Không có) | Tối đa 1 bản nộp/Bộ/kỳ. Nhiều user cùng tạo → user lưu trước thắng, user sau báo lỗi "đã tồn tại" | QC Audit — resolve Q1, Q2 |
| 2026-05-22 | 1.6 | Re-open báo cáo nháp | (Không mô tả) | Giữ snapshot đã lưu, không re-fetch API | QC Audit — resolve Q3 |
| 2026-05-22 | 1.6 | Đổi lĩnh vực — Ghi chú | (Không rõ) | Xóa toàn bộ kể cả Ghi chú đã nhập | QC Audit — resolve Q4 |
| 2026-05-22 | 1.6 | API timeout giữa chừng | (Không mô tả) | Giữ data đã fill, không rollback + Toast T05 + manual phần còn lại | QC Audit — resolve Q5, CMR_12 |
| 2026-05-22 | 1.6 | Chỉnh sửa (YC chỉnh sửa) | (Không mô tả) | User phải sửa ≥1 field → nút Nộp Enabled. Tham chiếu CF_03 | QC Audit — resolve Q7 |
| 2026-05-22 | 1.6 | Filter logic (AND/OR) | Chưa mô tả | Logic filter: AND khi chọn nhiều giá trị đồng thời | QC Audit — clarify filter combination |
